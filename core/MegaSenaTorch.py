from builtins import set, list

import torch
from torch import Tensor
from torch.utils.data import TensorDataset, random_split

from core.Loteria import Loteria
from core.MegaSenaTorch_Functions import gerar_aposra
from core.MegaSena_Updates import atualizar_base_historica
from core.networks.LoteriaNNTotch import LoteriaNNTorch
from repository.ApostaCandidataRepository import ApostaCandidataRepository
from repository.MySQLDatabase import MySQLDatabase
from repository.ResultadoRepository import MegaSenaResultadoRepository

# todo Regulagem de parâmetros
parameters = {
    "network": {
        "input_size": 6,
        "hidden_size": 30,
        "output_size": 1,
        "learning_rate": 0.001,
        "train_epochs": 300,
        "state_path": "./networks/state"
    },
    "quantidade_jogos": 7,
    "expurgo_apostas_recentes": 0,
    "expurgo": 100,
    "limite_duplicados": 1,
    "ratio_minimo": 100.0,
    "taxa_classificacao": 0.25,
    "atualizar_base_resultados": False,
    "modo_treino": False
}

network = LoteriaNNTorch(input_size=parameters["network"]["input_size"],
                         hidden_size=parameters["network"]["hidden_size"],
                         output_size=parameters["network"]["output_size"])

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
kt = k - 10
x_data = list()
y_data = list()
for row in download.__iter__():
    x_data.append(list(row[:6]))
    y_data.append(list(row[6:]))

dataset = TensorDataset(Tensor(x_data), Tensor(y_data))
train_set, test_set = random_split(dataset, [kt, k - kt])

if parameters["modo_treino"]:
    network.calibrate_loss(train_set, parameters["network"]["train_epochs"], parameters["network"]["learning_rate"])
    network.export_network(parameters["network"]["state_path"])

    print("\n")
    for i, data in enumerate(test_set, 0):
        data_test, result_test = data
        predict = network(data_test)
        print(f"{data_test} com Previsão de {float(predict) :.4} e era {int(result_test)}")
else:
    network.load_state_dict(torch.load(f"{parameters['network']['state_path']}/state_netwirk"))

    while len(loteria.apostas) < parameters["quantidade_jogos"]:
        gerar_aposra(loteria=loteria,
                     esperados=x_data,
                     expurgo=parameters["expurgo"],
                     ratio_minimo=parameters["ratio_minimo"],
                     limite_duplicados=parameters["limite_duplicados"])

        predict = network(Tensor(loteria.aposta_candidata))

        if float(predict) <= parameters["taxa_classificacao"]:
            print(f"Previsão33333333: {float(predict) :.4}")

            expectativa = set([2, 10, 16, 32, 45, 49])
            expectativa_realizada = list(set(loteria.aposta_candidata).intersection(expectativa))
            print(f"Teria exito de: {expectativa_realizada}")

            loteria.apostas.append(loteria.aposta_candidata)

    loteria.mostrar_apostas_selecionadas()
