apostas = [
    [4, 17, 32, 40, 47, 59],
    [2, 4, 16, 17, 21, 33],
    [2, 7, 8, 11, 19, 40],
    [4, 12, 24, 32, 38, 46],
    [2, 5, 8, 28, 52, 57],
    [1, 11, 16, 22, 53, 55],
    [10, 19, 23, 32, 45, 58]
]

resultado = [6, 17, 29, 35, 45, 48]

for aposta in apostas.__iter__():
    acertos = set(aposta).intersection(resultado)
    print(list(acertos))