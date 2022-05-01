coords = int(input('coords: '))

n_elementos_matriz_de_forcas = 2*coords

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

forcasFiltrado = []

for i in range(int(len(forcas))):
    if type(forcas[i][1]) == float:
        forcasFiltrado.append(forcas[i])

print('forcas = {}'.format(forcas))
print('forcasFiltrado = {}'.format(forcasFiltrado))
