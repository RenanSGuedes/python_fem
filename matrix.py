# Sympy, Numpy

from itertools import *
from numpy import zeros

# computa quantos elementos (obs: A matriz inicial deve se basear no número de nós)

elementos = int(input('Numero de nos: '))

# cria uma matriz quadrada com a ordem do número de elementos

matriz_inicial = zeros((elementos, elementos))
print("matriz_inicial (antes): {}".format(matriz_inicial))

k = [400, 500, 500, 300, 400, 500]

# Definição dos nós associados aos elementos

coords = []
print('Coordenadas (Duplo <enter> finaliza o input)')
print('nós conectados')
i = input()

while i != '':
    coords.append([float(s) for s in i.split()])
    i = input()

# Combinação dos elementos para construção da matriz de rigidez global

lista_posicoes = []

for i in coords:
    lista_posicoes.append(list(product(i, repeat=2)))
print("lista_posicoes: {}".format(lista_posicoes))

for i in range(len(matriz_inicial) - 1):
    for j in range(len(matriz_inicial) - 1):
        matriz_inicial[int(lista_posicoes[i][j][0]) - 1][int(lista_posicoes[i][j][1]) - 1] += k[i]

# Troca o sinal da diagonal principal

for i in range(len(matriz_inicial)):
    for j in range(len(matriz_inicial)):
        if i != j:
            matriz_inicial[i][j] *= -1

print("matriz_inicial (depois): {}".format(matriz_inicial))
