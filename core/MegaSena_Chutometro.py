from core.Loteria import Loteria
from core.MegaSena_Updates import atualizar_base_historica
from repository.ApostaCandidataRepository import ApostaCandidataRepository
from repository.MySQLDatabase import MySQLDatabase
from repository.ResultadoRepository import MegaSenaResultadoRepository


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
    global ratio_minimo
    continuar = True
    while continuar:
        ativado = 0
        loteria.aposta_candidata = loteria.gerar_aposta()
        for row in esperados.__iter__():
            acertos = list(set(row).intersection(loteria.aposta_candidata))
            if acertos.__len__() <= limite_duplicados:
                ativado += 1
            else:
                print(f"{loteria.aposta_candidata} :: {acertos} acertos descartado por OCORRÊNCIAS")

        ratio = (ativado / expurgo) * 100

        if ratio >= ratio_minimo:
            print(f"Finalizado com ativação de {ratio}%")
            continuar = False
        else:
            ratio_minimo = ratio_minimo.__sub__(0.5)


# todo Regulagem de parâmetros
# Intervalo para exprgar / ultimos jogos + Criterio de aceite de previsão
quantidade_jogos = 7
expurgo_apostas_recentes = 1
expurgo = 3000
limite_duplicados = 1
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
    download = download[:(k - 1)]
    k = download.__len__()

# Expurgar jogos recentes
loteria.expurgar_template_chute(dataset=download, expurga_ultimos_jogos=expurgo_apostas_recentes)

# Montar intervalo de numeros que não devem repetir nos chutes
montar_intervalo_exclusivo()

# Inicializar as análises de cjutes
i = 1
while i <= loteria.quantidade_apostas:
    gerar_aposra()

    if acertos.__len__() <= limite_duplicados:
        apostaCandidataRepository.cadastrar_aposta_candidata(loteria.aposta_candidata, 0.00)
        loteria.apostas.append(loteria.aposta_candidata)
        esperados.append(loteria.aposta_candidata)
        print(f"{loteria.aposta_candidata} :: {0.00}")
        i = i + 1
    else:
        print(f"{loteria.aposta_candidata} :: foi descartado por EXCESSO DE OCORRÊNCIAS")

    acertos.clear()

# Fibalizar conexão com a base de dados
database.close_connection()

# Mostrar conjunto de dados
loteria.mostrar_apostas_selecionadas()

if modo_treino:
    spect = download[k-1:][:6]
    ultimo_resultado = set(spect)
    print(f'A sequência esperada era: {sorted(ultimo_resultado, reverse=False)}\n')
    for a in loteria.apostas:
        acuidade = list(set(a).intersection(ultimo_resultado))
        acuidade = sorted(acuidade, reverse=False)
        print(f"Aposta {a} | Com {len(acuidade)} acertos {acuidade}")
        acuidade = list()
