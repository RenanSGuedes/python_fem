# Sympy, Numpy

from itertools import *
from numpy import zeros

# computa quantos elementos

elementos = int(input('Elementos: '))

# cria uma matriz quadrada com a ordem do número de elementos

matriz_inicial = zeros((elementos, elementos))

k = [400, 500, 500, 300, 500]

# print(matriz_inicial)

# Definição dos nós associados aos elementos

coord = []
print('Coordenadas (Duplo <enter> finaliza o input)')
print('nos conectados')
i = input()
while i != '':
    coord.append([float(s) for s in i.split()])
    i = input()

# Combinação dos elementos para construção da matriz de rigidez global

lista_posicoes = []

for i in coord:
    lista_posicoes.append(list(product(i, repeat=2)))
print(lista_posicoes)

for i in range(len(matriz_inicial)):
    for j in range(len(matriz_inicial)):
        matriz_inicial[int(lista_posicoes[i][j][0]) - 1][int(lista_posicoes[i][j][1]) - 1] += k[i]

print(matriz_inicial)

for i in range(len(matriz_inicial)):
    for j in range(len(matriz_inicial)):
        if i != j:
            matriz_inicial[i][j] *= -1

print(matriz_inicial)


