indicesElementos = [[1, 2], [2, 4], [3, 4], [2, 3]]
deslocamentosComUeV = [['u2', 0.9681178212530336], ['v2', 0.22925263640531865], ['u3', 1.375615783763221], ['v3', 0]]
elements = [[[0, 0, 0], [0, 9, 0]], [[0, 9, 0], [12, 0, 0]], [[12, 9, 0], [12, 0, 0]], [[0, 9, 0], [12, 9, 0]]]
elementsComNos = [[[1, 0, 0], [2, 0, 9]], [[2, 0, 9], [4, 12, 0]], [[3, 12, 9], [4, 12, 0]], [[2, 0, 9], [3, 12, 9]]]

deslocamentosAgrupados = []

for i in range(0, len(deslocamentosComUeV), 2):
    deslocamentosAgrupados.append(
        [int(list(deslocamentosComUeV[i][0])[1]), deslocamentosComUeV[i][1], deslocamentosComUeV[i + 1][1]])

"""
elementsComNos = [[[1, 0, 0], [2, 0, 9]], [[2, 0, 9], [4, 12, 0]], [[3, 12, 9], [4, 12, 0]], [[2, 0, 9], [3, 12, 9]]]
deslocamentosAgrupados = [[2, 0.9681178212530336, 0.22925263640531865], [3, 1.375615783763221, 0]]
"""
elementsComNos = [[[1, 0, 0], [2, 12, 8]], [[2, 12, 8], [3, 12, 0]]]
deslocamentosAgrupados = [[2, 0.8277357145490972, -0.18091114689216928]]

for i in range(len(elementsComNos)):
    for j in range(len(deslocamentosAgrupados)):
        for k in range(2):
            if elementsComNos[i][k][0] == deslocamentosAgrupados[j][0]:
                elementsComNos[i][k][1] += deslocamentosAgrupados[j][1]
                elementsComNos[i][k][2] += deslocamentosAgrupados[j][2]

print(elementsComNos)

for i in range(len(elementsComNos)):
    for j in range(2):
        del elementsComNos[i][j][0]

print(elementsComNos)
