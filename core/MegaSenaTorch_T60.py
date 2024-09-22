from builtins import set, list

import torch
from torch import Tensor, FloatTensor
from torch.utils.data import TensorDataset, random_split

from core.Loteria import Loteria
from core.MegaSenaTorch_Functions import gerar_aposta, features_to_tensor, label_to_tensor, aposta_to_tensor
from core.MegaSena_Updates import atualizar_base_historica
from core.networks.LoteriaNNTorch import LoteriaNNTorch
from repository.ApostaCandidataRepository import ApostaCandidataRepository
from repository.MySQLDatabase import MySQLDatabase
from repository.ResultadoRepository import MegaSenaResultadoRepository

# todo Regulagem de parâmetros
parameters = {
    "network": {
        "input_size": 60,
        "hidden_size": 256,
        "output_size": 1,
        "layers": 8,
        "learning_rate": 0.01,
        "weight_decay": 0.0009,
        "train_epochs": 500,
        "state_path": "./networks/state"
    },
    "quantidade_jogos": 4,
    "expurgo_apostas_recentes": 0,
    "expurgo": 5000,
    "limite_duplicados": 1,
    "ratio_minimo": 100.0,
    "taxa_classificacao": 0.60,
    "fazer_previsao": True,
    "inferir_chutes": True,
    "atualizar_base_resultados": False,
    "modo_treino": False
}

network = LoteriaNNTorch(input_size=parameters["network"]["input_size"],
                         hidden_size=parameters["network"]["hidden_size"],
                         output_size=parameters["network"]["output_size"],
                         layers=parameters["network"]["layers"])

database = MySQLDatabase()
database.open_connection()

resultadoRepository = MegaSenaResultadoRepository(database=database)
apostaCandidataRepository = ApostaCandidataRepository(database=database)

loteria = Loteria(quantidade_numeros=6, quantidade_apostas=parameters["quantidade_jogos"])
loteria.set_template_aposta(primeiro_numero=1, ultimo_numero=60)

esperados = list()
acertos = list()

if parameters["atualizar_base_resultados"]:
    atualizar_base_historica(database=database)

download = resultadoRepository.listar_resultados("Coluna1, Coluna2, Coluna3, Coluna4, Coluna5, Coluna6, Ganhadores")

k = len(download)
kt = k - 50
x_data = list()
y_data = list()
for row in download.__iter__():
    x_data.append(list(row[:6]))
    y_data.append(list(row[6:]))

dataset = TensorDataset(features_to_tensor(x_data),
                        label_to_tensor(y_data))
train_set, test_set = random_split(dataset, [kt, k - kt])

if parameters["modo_treino"]:
    network.calibrate_loss(train_set,
                           parameters["network"]["train_epochs"],
                           parameters["network"]["learning_rate"],
                           parameters["network"]["weight_decay"])

    network.export_network(parameters["network"]["state_path"])

    print("\n")
    for i, data in enumerate(test_set, 0):
        data_test, result_test = data
        predict = network(data_test)
        print(f"Previsão de {float(predict) :.4} e era {int(result_test)}")
else:
    network.load_state_dict(torch.load(f"{parameters['network']['state_path']}/state_network"))

    expectativa = [10, 16, 35, 46, 49, 60]

    while len(loteria.apostas) < parameters["quantidade_jogos"]:
        if parameters["inferir_chutes"]:
            gerar_aposta(loteria=loteria,
                         esperados=x_data,
                         expurgo=parameters["expurgo"],
                         ratio_minimo=parameters["ratio_minimo"],
                         limite_duplicados=parameters["limite_duplicados"])
        else:
            loteria.gerar_aposta()

        if parameters["fazer_previsao"]:
            tensor_aposta = aposta_to_tensor(loteria.aposta_candidata.copy())
            predict: FloatTensor = network(Tensor(tensor_aposta))
            if float(predict) >= parameters["taxa_classificacao"]:
                print(f"Previsão: {float(predict) :.2}")

                loteria.apostas.append(loteria.aposta_candidata)
                esperados.append(loteria.aposta_candidata)

                apostaCandidataRepository.cadastrar_aposta_candidata(loteria.aposta_candidata, f"{float(predict):.2f}")
        else:
            loteria.apostas.append(loteria.aposta_candidata)
            esperados.append(loteria.aposta_candidata)

    if not parameters["modo_treino"]:
        print("\n")
        for aposta in loteria.apostas.__iter__():
            expectativa_realizada = list(set(aposta).intersection(expectativa))
            print(f"{aposta} Teria exito de: {expectativa_realizada}")
            acuracia = (len(expectativa_realizada) / 6) * 100
            print(f"Acurácia: {acuracia:.1f}\n")

    loteria.mostrar_apostas_selecionadas()
