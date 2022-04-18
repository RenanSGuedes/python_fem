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

linha = [1, 1, 2, 2, 3, 3, 4, 4]

indicesElementos = [[1, 2], [2, 4], [3, 4], [2, 3]]

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
