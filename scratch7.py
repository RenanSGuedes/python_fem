import numpy as np

deslocamentosComUeV = [['u2', -0.21721157925048828],
                       ['v2', 0.9176144192570522],
                       ['u3', -0.43442315850097657],
                       ['u4', -0.21721157925048828],
                       ['v4', 0.9176144192570522]]

forcas = [['u1', 'R'],
          ['v1', 'R'],
          ['u2', 0],
          ['v2', -100],
          ['u3', 0],
          ['v3', 'R'],
          ['u4', 0],
          ['v4', 0]]

forcas[0][1] = 0
forcas[1][1] = 0
forcas[2][1] = -0.21721157925048828
forcas[3][1] = 0.9176144192570522
forcas[4][1] = -0.43442315850097657
forcas[5][1] = 0
forcas[6][1] = -0.21721157925048828
forcas[7][1] = 0.9176144192570522

for i in range(len(forcas)):
    for j in range(len(deslocamentosComUeV)):
        if forcas[i][1] == 'R':
            forcas[i][1] = 0
        elif forcas[i][0] == deslocamentosComUeV[j][0]:
            forcas[i][1] = deslocamentosComUeV[j][1]

"""
deslocamentosAgrupados = [
   [2, -0.21721157925048828, 0.9176144192570522],
   [3, -0.43442315850097657, 0],
   [4, -0.21721157925048828, 0.9176144192570522] 
]
"""

deslocamentosAgrupados = []

print(forcas)

for i in range(0, len(forcas) - 1, 2):
    if list(forcas[i][0])[0] == 'u' and list(forcas[i + 1][0])[0] == 'v':
        deslocamentosAgrupados.append(
            [int(list(forcas[i][0])[1]), forcas[i][1], forcas[i + 1][1]])
    elif list(forcas[i][0])[0] == 'v':
        deslocamentosAgrupados.append(
            [int(list(forcas[i][0])[1]), 0, forcas[i + 1][1]])
    else:
        deslocamentosAgrupados.append(
            [int(list(forcas[i][0])[1]), forcas[i][1], 0])

print(deslocamentosAgrupados)
