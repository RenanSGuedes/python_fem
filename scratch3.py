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

# listaGlobal[0, 1,..., 7][0, 1,..., 7]

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
coluna = [1, 1, 2, 2, 3, 3, 4, 4]

indicesL = [linha.index(1), linha.index(2), linha.index(3), linha.index(4)]  # [0, 2, 4, 6]
indicesC = [coluna.index(1), coluna.index(2), coluna.index(3), coluna.index(5)]

print("indices =", indicesL)

# Elemento 1 ≥ Interage com 1 e 2 [(1, 1), (1, 2), (2, 1), (2, 2)]
listaGlobal[1 - 1][0] += lista[0][0][0]
listaGlobal[1 - 1][1] += lista[0][0][1]
listaGlobal[1 - 1][2] += lista[0][0][2]
listaGlobal[1 - 1][3] += lista[0][0][3]

listaGlobal[2 - 1][0] += lista[0][1][0]
listaGlobal[2 - 1][1] += lista[0][1][1]
listaGlobal[2 - 1][2] += lista[0][1][2]
listaGlobal[2 - 1][3] += lista[0][1][3]

listaGlobal[3 - 1][0] += lista[0][2][0]
listaGlobal[3 - 1][1] += lista[0][2][1]
listaGlobal[3 - 1][2] += lista[0][2][2]
listaGlobal[3 - 1][3] += lista[0][2][3]

listaGlobal[4 - 1][0] += lista[0][3][0]
listaGlobal[4 - 1][1] += lista[0][3][1]
listaGlobal[4 - 1][2] += lista[0][3][2]
listaGlobal[4 - 1][3] += lista[0][3][3]

# Elemento 2 ≥ Interage com 2 e 4
listaGlobal[2][2] += lista[1][0][0]
listaGlobal[2][3] += lista[1][0][1]
listaGlobal[2][6] += lista[1][0][2]
listaGlobal[2][7] += lista[1][0][3]

listaGlobal[3][2] += lista[1][1][0]
listaGlobal[3][3] += lista[1][1][1]
listaGlobal[3][6] += lista[1][1][2]
listaGlobal[3][7] += lista[1][1][3]

listaGlobal[6][2] += lista[1][2][0]
listaGlobal[6][3] += lista[1][2][1]
listaGlobal[6][6] += lista[1][2][2]
listaGlobal[6][7] += lista[1][2][3]

listaGlobal[7][2] += lista[1][3][0]
listaGlobal[7][3] += lista[1][3][1]
listaGlobal[7][6] += lista[1][3][2]
listaGlobal[7][7] += lista[1][3][3]

# Elemento 3 ≥ Interage com 3 e 4
listaGlobal[4][4] += lista[2][0][0]
listaGlobal[4][5] += lista[2][0][1]
listaGlobal[4][6] += lista[2][0][2]
listaGlobal[4][7] += lista[2][0][3]

listaGlobal[5][4] += lista[2][1][0]
listaGlobal[5][5] += lista[2][1][1]
listaGlobal[5][6] += lista[2][1][2]
listaGlobal[5][7] += lista[2][1][3]

listaGlobal[6][4] += lista[2][2][0]
listaGlobal[6][5] += lista[2][2][1]
listaGlobal[6][6] += lista[2][2][2]
listaGlobal[6][7] += lista[2][2][3]

listaGlobal[7][4] += lista[2][3][0]
listaGlobal[7][5] += lista[2][3][1]
listaGlobal[7][6] += lista[2][3][2]
listaGlobal[7][7] += lista[2][3][3]

# Elemento 4 ≥ Interage com 2 e 3
listaGlobal[2][2] += lista[3][0][0]
listaGlobal[2][3] += lista[3][0][1]
listaGlobal[2][4] += lista[3][0][2]
listaGlobal[2][5] += lista[3][0][3]

listaGlobal[3][2] += lista[3][1][0]
listaGlobal[3][3] += lista[3][1][1]
listaGlobal[3][4] += lista[3][1][2]
listaGlobal[3][5] += lista[3][1][3]

listaGlobal[4][2] += lista[3][2][0]
listaGlobal[4][3] += lista[3][2][1]
listaGlobal[4][4] += lista[3][2][2]
listaGlobal[4][5] += lista[3][2][3]

listaGlobal[5][2] += lista[3][3][0]
listaGlobal[5][3] += lista[3][3][1]
listaGlobal[5][4] += lista[3][3][2]
listaGlobal[5][5] += lista[3][3][3]

print(listaGlobal)
