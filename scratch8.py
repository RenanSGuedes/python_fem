forcas = [['u1', 'R'], ['v1', 'R'], ['u2', 0.0], ['v2', 0.0], ['u3', 50.0], ['v3', 0.0], ['u4', 'R'], ['v4', 'R']]

ccs = []

for item in forcas:
    if item[1] == 'R':
        ccs.append(forcas.index(item))

print(ccs)