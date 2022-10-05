from pybrain3.datasets import SupervisedDataSet
from pybrain3.supervised import BackpropTrainer
from pybrain3.tools.shortcuts import buildNetwork

from core.Loteria import Loteria
from core.MegaSena_Updates import atualizar_base_historic
from repository.ApostaCandidataRepository import ApostaCandidataRepository
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
    for i in range(1):
        TTR = float(trainer.train())
        print(f"{i}ª Fase do Treinamento | Margem de Erro :: {TTR:.2f}% \n")


def remover_numeros_recentes(numero_jogos: int = 1):
    for j in download[(k - numero_jogos):]:
        for z in j[:6]:
            if loteria.template_aposta.__contains__(z):
                loteria.template_aposta.remove(z)
                print(f"REMOVER {z}")
    print("\n")


def montar_intervalo_exclusivo():
    print("Intervalo de numeros para análise")
    for row in download[(k - expurgo):].__iter__():
        esperados.append(row[:6])
        print(f"{row[:6]}")
    print("\n")


def comparar_numeros_repetidos(aposta: list, limite_duplicados: int = 1):
    for row in esperados.__iter__():
        for e in row:
            if aposta.__contains__(e):
                acertos.append(e)
        if acertos.__len__() > limite_duplicados:
            break


# Inicializar bases de dados
resultadoRepository = MegaSenaResultadoRepository()
apostaCandidataRepository = ApostaCandidataRepository()

# Inicializar Loteria
loteria = Loteria(quantidade_numeros=6, quantidade_apostas=10)
loteria.set_template_aposta(primeiro_numero=1, ultimo_numero=60)

# Intervalo para exprgar / ultimos jogos + Criterio de aceite de previsão
expurgo = 10
probabilidade_minima = 0.0
limite_duplicados = 1

# Listas de apoio
esperados = list()
acertos = list()

# Atualizar base de dados historica
atualizar_base_historic()

# Carregar dados
download = resultadoRepository.listar_resultados("Coluna1, Coluna2, Coluna3, Coluna4, Coluna5, Coluna6, Ganhadores")

# Tamanho do dataset
k = download.__len__()

# Expurgar jogos recentes
loteria.expurgar_template_chute(dataset=download, expurga_ultimos_jogos=1)

# Gerar rede neural
network = buildNetwork(6, 30, 1, bias=True)

# Remover jogos que provavelmente não sairão
remover_numeros_recentes(numero_jogos=1)

# Montar intervalo de numeros que não devem repetir nos chutes
montar_intervalo_exclusivo()

# Inicializar as análises de cjutes
i = 1
while i <= loteria.quantidade_apostas:
    loteria.aposta_candidata = loteria.gerar_aposta()

    previsao = float(network.activate(loteria.aposta_candidata))

    if previsao > probabilidade_minima:
        comparar_numeros_repetidos(aposta=loteria.aposta_candidata)

        if acertos.__len__() <= limite_duplicados:
            apostaCandidataRepository.cadastrar_aposta_candidata(loteria.aposta_candidata, previsao)
            loteria.apostas.append(loteria.aposta_candidata)
            print(f"{loteria.aposta_candidata} :: {previsao}")
            i = i + 1
        else:
            print(f"{loteria.aposta_candidata} :: {previsao} foi descartado por EXCESSO DE OCORRÊNCIAS")
    else:
        print(f"{loteria.aposta_candidata} :: {previsao} foi descartado por BAIXA PROBABILIDADE")

    acertos.clear()

# Mostrar conjunto de dados
loteria.mostrar_apostas_selecionadas()
