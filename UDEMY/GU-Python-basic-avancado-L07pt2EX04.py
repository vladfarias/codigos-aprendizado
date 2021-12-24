#  GEEK UNIVERSITY - Programação em Python do básico ao avançado
#  EXERCÍCIO 4 LISTA  07 parte 2
#  Imprimir uma matriz e retornar a localização do maior valor

import random

matriz4x4 = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(random.randint(0, 100))
    matriz4x4 = matriz4x4 + [linha]

print(matriz4x4)

linha_maximo = matriz4x4.index(max(matriz4x4))
coluna_maximo = matriz4x4[linha_maximo].index(max(matriz4x4[linha_maximo]))

print(linha_maximo, coluna_maximo)
