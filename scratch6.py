import numpy as np

listaGlobal = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 163.6, 0.0, -163.6, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 185.5, -47.1, -122.7, 0.0, -62.8, 47.1],
    [0.0, -163.6, -47.1, 198.9, 0.0, 0.0, 47.1, -35.3],
    [0.0, 0.0, -122.7, 0.0, 122.7, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 163.6, 0.0, -163.6],
    [0.0, 0.0, -62.8, 47.1, 0.0, 0.0, 62.8, -47.1],
    [0.0, 0.0, 47.1, -35.3, 0.0, -163.6, -47.1, 198.9]
]

a = np.array(listaGlobal)

coords = int(input('coords: '))

n_elementos_matriz_de_forcas = 2 * coords

forcas = []

for i in range(coords):
    print('Nó {}'.format(i + 1))
    resposta = input('Restrições: x [X], y [Y], x e y [XY], livre [L]: ')

    if resposta == 'X':
        novaResposta = float(input('Fy = '))
        forcas.append(['u{}:'.format(i + 1), 0])
        forcas.append(['v{}:'.format(i + 1), novaResposta])
    elif resposta == 'Y':
        novaResposta = float(input('Fx = '))
        forcas.append(['u{}:'.format(i + 1), novaResposta])
        forcas.append(['v{}:'.format(i + 1), 0])
    elif resposta == 'XY':
        for j in (['u', 'v']):
            forcas.append(['{}{}'.format(j, i + 1), 'R'])
    else:
        for (m, n) in zip(['x', 'y'], ['u', 'v']):
            novaResposta = float(input('F{} = '.format(m)))
            forcas.append(['{}{}'.format(n, i + 1), novaResposta])

forcasFiltradoComUeV = []
forcasFiltrado = []

for i in range(int(len(forcas))):
    if type(forcas[i][1]) == float:
        forcasFiltradoComUeV.append(forcas[i])

for i in range(int(len(forcas))):
    if type(forcas[i][1]) == float:
        forcasFiltrado.append(forcas[i][1])

print('forcas = {}'.format(forcas))
print('forcasFiltradoComUeV = {}'.format(forcasFiltradoComUeV))
print('forcasFiltrado = {}'.format(forcasFiltrado))

print(np.array(forcasFiltrado))

ccs = []

for item in forcas:
    if item[1] == 'R':
        ccs.append(forcas.index(item))

a = np.delete(a, ccs, axis=1)
a = np.delete(a, ccs, axis=0)

print(a)

numpyListInverse = np.linalg.inv(a)

deslocamentosNumpy = np.matmul(numpyListInverse, forcasFiltrado)
deslocamentosArray = deslocamentosNumpy.tolist()

print(deslocamentosArray)

deslocamentosComUeV = []


for i in range(len(forcasFiltradoComUeV)):
    deslocamentosComUeV.append(('{}'.format(forcasFiltradoComUeV[i][0]), deslocamentosArray[i]))

print(deslocamentosComUeV)


