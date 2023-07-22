from builtins import range

from pybrain3.datasets import SupervisedDataSet
from pybrain3.supervised import BackpropTrainer
from pybrain3.tools.shortcuts import buildNetwork

from core.Loteria import Loteria
from core.MegaSena_Updates import atualizar_base_historica
from repository.ApostaCandidataRepository import ApostaCandidataRepository
from repository.MySQLDatabase import MySQLDatabase
from repository.ResultadoRepository import MegaSenaResultadoRepository


def treinar_rede():
    # DataSet model.
    dataset = SupervisedDataSet(6, 1)
    for row in download.__iter__():
        in_value = row[:6]
        out_value = row[6:][0]
        dataset.addSample(in_value, out_value)

    # Treinar rede com dataset carregado
    trainee = BackpropTrainer(network, dataset, 0.10)
    for i in range(50):
        TTR = trainee.train().__float__()
        print(f"Fase {i + 1} do Treinamento | Margem de Erro :: {TTR}%")

    print("\n")


def montar_intervalo_exclusivo():
    print("Intervalo de numeros para análise")
    for row in download[(k - expurgo):].__iter__():
        esperados.append(row[:6])
        print(f"{row[:6]}")
    print("\n")


def gerar_aposra():
    continuar = True
    while continuar:
        ativado = 0
        loteria.gerar_aposta()
        for row in esperados.__iter__():
            acertos = list(set(row).intersection(loteria.aposta_candidata))
            if acertos.__len__() <= limite_duplicados:
                ativado += 1

        ratio = (ativado / expurgo) * 100

        if ratio >= ratio_minimo:
            print(f"{loteria.aposta_candidata} com ativação de {ratio}%")
            continuar = False


# todo Regulagem de parâmetros
# Intervalo para exprgar / ultimos jogos + Criterio de aceite de previsão
quantidade_jogos = 7
expurgo_apostas_recentes = 1
expurgo = 4
limite_duplicados = 1
probabilidade_minima = 0.1
ratio_minimo = 100.0
atualizar_base_resultados = False
modo_treino = True

# Inicializar bases de dados
database = MySQLDatabase()
database.open_connection()

resultadoRepository = MegaSenaResultadoRepository(database=database)
apostaCandidataRepository = ApostaCandidataRepository(database=database)

# Inicializar Loteria
loteria = Loteria(quantidade_numeros=6, quantidade_apostas=quantidade_jogos)
loteria.set_template_aposta(primeiro_numero=1, ultimo_numero=60)

# Listas de apoio
esperados = list()
acertos = list()

# Atualizar base de dados historica
if atualizar_base_resultados:
    atualizar_base_historica(database=database)

# Carregar dados
download = resultadoRepository.listar_resultados("Coluna1, Coluna2, Coluna3, Coluna4, Coluna5, Coluna6, Ganhadores")

# Tamanho do dataset
k = download.__len__()
if modo_treino:
    download = download[:(k - expurgo_apostas_recentes)]
    k = download.__len__()

# Expurgar jogos recentes
loteria.expurgar_template_chute(dataset=download, expurga_ultimos_jogos=expurgo_apostas_recentes)

# todo Regulagem de camadas de neurônios
# Gerar rede neural
network = buildNetwork(6, 60, 1, bias=True)

# Montar intervalo de numeros que não devem repetir nos chutes
montar_intervalo_exclusivo()

# Treinar rede
treinar_rede()

# Inicializar as análises de cjutes
i = 1
while i <= loteria.quantidade_apostas:
    gerar_aposra()

    previsao = float(network.activate(loteria.aposta_candidata))

    if previsao >= probabilidade_minima:
        if acertos.__len__() <= limite_duplicados:
            apostaCandidataRepository.cadastrar_aposta_candidata(loteria.aposta_candidata, previsao)
            loteria.apostas.append(loteria.aposta_candidata)
            esperados.append(loteria.aposta_candidata)
            # print(f"{loteria.aposta_candidata} :: {previsao}")
            i = i + 1
        else:
            pass  # print(f"{loteria.aposta_candidata} :: {previsao} foi descartado por EXCESSO DE OCORRÊNCIAS")
    else:
        pass  # print(f"{loteria.aposta_candidata} :: {previsao} foi descartado por BAIXA PROBABILIDADE")

    acertos.clear()

# Fibalizar conexão com a base de dados
database.close_connection()

# Mostrar conjunto de dados
loteria.mostrar_apostas_selecionadas()

if modo_treino:
    spect = list(download)[k - 1:][:6]
    ultimo_resultado = set(spect)
    print(f'A sequência esperada era: {sorted(ultimo_resultado, reverse=False)}\n')
    for a in loteria.apostas:
        acuidade = list(set(a).intersection(ultimo_resultado))
        acuidade = sorted(acuidade, reverse=False)
        print(f"Aposta {a} | Com {len(acuidade) / len(a)} acertos {acuidade}")
        acuidade = list()
