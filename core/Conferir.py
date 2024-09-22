apostas = [
    [3, 6, 7, 9, 20, 56],
    [4, 10, 16, 33, 41, 46],
    [7, 13, 17, 21, 27, 39],
    [17, 28, 33, 49, 58, 59]
]

resultado = [10, 16, 35, 46, 49, 60]

for aposta in apostas.__iter__():
    acertos = set(aposta).intersection(resultado)
    print(list(acertos))