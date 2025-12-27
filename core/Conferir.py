apostas = [
    [3, 13, 33, 48, 56, 57],
    [8, 12, 21, 26, 32, 54],
    [1, 5, 6, 23, 48, 54],
    [5, 8, 22, 31, 53, 59]
]

resultado = [6, 13, 15, 19, 32, 60]

for aposta in apostas.__iter__():
    acertos = set(aposta).intersection(resultado)
    print(list(acertos))
