coords = []
print('Coordenadas (Duplo <enter> finaliza o input)')
print('nós conectados')
i = input()

while i != '':
    coords.append([float(s) for s in i.split()])
    i = input()

print(coords)
