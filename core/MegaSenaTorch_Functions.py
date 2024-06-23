import torch

from core.Loteria import Loteria


def gerar_aposta(loteria: Loteria, esperados: list, expurgo: list, ratio_minimo: float, limite_duplicados: int):
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


def aposta_to_tensor(aposta: list):
    template = list(range(1, 61))
    tensor = torch.zeros(1, 60)

    for n in aposta:
        x = template.index(n)
        tensor[0][x] = 1

    return tensor


def features_to_tensor(features: list):
    template = list(range(1, 61))

    tensors = torch.zeros(len(features), 60)

    for i, data in enumerate(features):
        for n in data:
            x = template.index(n)
            tensors[i][x] = 1

    return tensors


def label_to_tensor(labels: list):
    tensors = torch.zeros(len(labels), 1)

    for i, label in enumerate(labels):
        tensors[i][0] = label[0]

    return tensors
