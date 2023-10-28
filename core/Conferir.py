apostas = [
   [12, 33, 35, 37, 44, 48],
   [13, 21, 27, 33, 38, 55],
   [3, 4, 10, 12, 20, 58],
   [13, 17, 25, 33, 44, 47],
   [3, 18, 20, 21, 25, 47],
   [3, 6, 37, 39, 54, 56]
]

resultado = [5, 10, 27, 38, 56, 57]

for aposta in apostas.__iter__():
    acertos = set(aposta).intersection(resultado)
    print(list(acertos))