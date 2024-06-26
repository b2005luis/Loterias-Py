from core.Loteria import Loteria


def gerar_aposra(loteria: Loteria, esperados: list, expurgo: list, ratio_minimo: float, limite_duplicados: int):
    k = len(esperados)
    ativado = 0
    continuar = True
    while continuar:
        loteria.gerar_aposta()
        for row in esperados[k - expurgo:].__iter__():
            acertos = list(set(row).intersection(loteria.aposta_candidata))
            if acertos.__len__() <= limite_duplicados:
                ativado += 1

        ratio = float(ativado / expurgo) * 100

        if ratio >= ratio_minimo:
            print(f"{loteria.aposta_candidata} com ativação de {ratio}%")
            continuar = False
