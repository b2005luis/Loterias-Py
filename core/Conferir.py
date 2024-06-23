apostas = [
   [21, 25, 26, 27, 29, 57],
   [14, 18, 34, 35, 42, 53],
   [15, 24, 45, 48, 52, 56],
   [30, 34, 37, 44, 46, 51],
   [3, 21, 26, 34, 37, 43],
   [9, 19, 23, 39, 40, 46]
]

resultado = [21, 27, 35, 48, 59, 60]

for aposta in apostas.__iter__():
    acertos = set(aposta).intersection(resultado)
    print(list(acertos))