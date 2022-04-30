coords = 3

n_elementos_matriz_de_forcas = 2*coords

forcas = []

for i in range(coords):
    print('Nó {}'.format(i + 1))
    resposta = input('Restrições: x [X], y [Y], x e y [XY], livre [L]: ')

    if resposta == 'X':
        novaResposta = float(input('Fy = '))
        forcas.append([0])
        forcas.append([novaResposta])
    elif resposta == 'Y':
        novaResposta = float(input('Fx = '))
        forcas.append([novaResposta])
        forcas.append([0])
    elif resposta == 'XY':
        for j in (['x', 'y']):
            forcas.append(['R{}'.format(j)])
    else:
        for j in (['x', 'y']):
            novaResposta = float(input('F{} = '.format(j)))
            forcas.append([novaResposta])

forcasFiltrado = []

for i in range(len(forcas)):
    if forcas[i] != ['Rx'] and forcas[i] != ['Ry']:
        forcasFiltrado.append(forcas[i])

print('forcas = {}'.format(forcas))
print('forcasFiltrado = {}'.format(forcasFiltrado))
