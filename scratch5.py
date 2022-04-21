listaGlobal = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

lista = [
    [
        [0, 0, 0, 0],
        [0, 166.7, 0, -166.7],
        [0, 0, 0, 0],
        [0, -166.7, 0, 166.7],
    ],
    [
        [64, -48, -64, 48],
        [-48, 36, 48, -36],
        [-64, 48, 64, -48],
        [48, -36, -48, 36]
    ],
    [
        [0, 0, 0, 0],
        [0, 166.7, 0, -166.7],
        [0, 0, 0, 0],
        [0, -166.7, 0, 166.7],
    ],
    [
        [125, 0, -125, 0],
        [0, 0, 0, 0],
        [-125, 0, 125, 0],
        [0, 0, 0, 0],
    ]
]

"""
listaGlobal[0][0] += lista[0][0][0]
listaGlobal[0][1] += lista[0][0][1]
listaGlobal[0][2] += lista[0][0][2]
listaGlobal[0][3] += lista[0][0][3]

listaGlobal[1][0] += lista[0][1][0]
listaGlobal[1][1] += lista[0][1][1]
listaGlobal[1][2] += lista[0][1][2]
listaGlobal[1][3] += lista[0][1][3]

listaGlobal[2][0] += lista[0][2][0]
listaGlobal[2][1] += lista[0][2][1]
listaGlobal[2][2] += lista[0][2][2]
listaGlobal[2][3] += lista[0][2][3]

listaGlobal[3][0] += lista[0][3][0]
listaGlobal[3][1] += lista[0][3][1]
listaGlobal[3][2] += lista[0][3][2]
listaGlobal[3][3] += lista[0][3][3]
"""

linha = []

for i in range(4):
    linha.append(i + 1)
    linha.append(i + 1)

n_elementos = 4
indicesElementos = []
# indicesElementos = [[1, 2], [2, 4], [3, 4], [2, 3]]

print("Elementos e nós associados: ")
print(30*"-")
for i in range(n_elementos):
    print("Elemento {}: ".format(i + 1))
    n1 = int(input("Nó 1: "))
    n2 = int(input("Nó 2: "))
    print(30*"-")
    indicesElementos.append([n1, n2])

print(indicesElementos)

indices = [[], [], [], []]  # Para cada elemento

for j in range(len(indicesElementos)):
    for i in indicesElementos[j]:
        for item in range(len(linha)):
            if linha[item] == i:
                indices[j].append(item)

print("indices =", indices)

for k in range(len(lista)):
    for (newItem, i) in zip(indices[k], range(0, 4, 1)):
        for (item, j) in zip(indices[k], range(0, 4, 1)):
            listaGlobal[newItem][item] += lista[k][i][j]

print(listaGlobal)
