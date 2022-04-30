import array_to_latex as a2l
import numpy as np

listaGlobal = [
    [70.7, 47.1, -70.7, -47.1, 0.0, 0.0],
    [47.1, 31.4, -47.1, -31.4, 0.0, 0.0],
    [-70.7, -47.1, 70.7, 47.1, 0.0, 0.0],
    [-47.1, -31.4, 47.1, 215.5, 0.0, -184.1],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, -184.1, 0.0, 184.1]
]

a = np.array(listaGlobal)
a = np.delete(a, [0, 1, 4, 5], axis=1)
a = np.delete(a, [0, 1, 4, 5], axis=0)

print(a)

numpyListInverse = np.linalg.inv(a)
forces = np.array([[50], [0]])

print(forces)

print(np.matmul(numpyListInverse, forces))
