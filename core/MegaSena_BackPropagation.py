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
    trainer = BackpropTrainer(network, dataset)
    for i in range(10):
        TTR = float(trainer.train())
        print(f"Fase do Treinamento | Margem de Erro :: {TTR}%")

    print("\n")


def montar_intervalo_exclusivo():
    print("Intervalo de numeros para análise")
    for row in download[(k - expurgo):].__iter__():
        esperados.append(row[:6])
        print(f"{row[:6]}")
    print("\n")


def comparar_numeros_repetidos(aposta: list, limite_duplicados: int = 1):
    for row in esperados.__iter__():
        acertos = list(set(row).intersection(aposta))
        if acertos.__len__() > limite_duplicados:
            print(f"{loteria.aposta_candidata} foi descartada por EXCESSO DE OCORRÊNCIAS com {acertos}")
            break


def gerar_aposra():
    continuar = True
    while continuar:
        ativado = 0
        loteria.aposta_candidata = loteria.gerar_aposta()
        for row in esperados.__iter__():
            acertos = list(set(row).intersection(loteria.aposta_candidata))
            if acertos.__len__() > limite_duplicados:
                print(f"{loteria.aposta_candidata} foi descartada por EXCESSO DE OCORRÊNCIAS com {acertos}")
                continuar = True
                break
            else:
                ativado += 1

        ratio = (ativado / expurgo) * 100

        if ratio >= ratio_minimo:
            continuar = False


# todo Regulagem de parâmetros
# Intervalo para exprgar / ultimos jogos + Criterio de aceite de previsão
quantidade_jogos = 7
expurgo_apostas_recentes = 1
expurgo = 10
probabilidade_minima = 0.0
limite_duplicados = 0
ratio_minimo = 100.0
atualizar_base_resultados = False

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

# Expurgar jogos recentes
loteria.expurgar_template_chute(dataset=download, expurga_ultimos_jogos=expurgo_apostas_recentes)

# TODO Inicializar camadas da rede
# Gerar rede neural
network = buildNetwork(6, 30, 1, bias=True)

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
            print(f"{loteria.aposta_candidata} :: {previsao}")
            i = i + 1
        else:
            print(f"{loteria.aposta_candidata} :: {previsao} foi descartado por EXCESSO DE OCORRÊNCIAS")
    else:
        print(f"{loteria.aposta_candidata} :: {previsao} foi descartado por BAIXA PROBABILIDADE")

    acertos.clear()

# Fibalizar conexão com a base de dados
database.close_connection()

# Mostrar conjunto de dados
loteria.mostrar_apostas_selecionadas()
