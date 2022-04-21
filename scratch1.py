from sympy import pi, sin, cos, symbols, acos
# Subs in matrix: https://docs.sympy.org/latest/modules/matrices/matrices.html#operations-on-entries

x = symbols("x")

fis = []
Ls = []

x1 = 1
y1 = 0

n_elementos = int(input("n_elementos: "))
vvs = []

xp1s = []
yp1s = []
xp2s = []
yp2s = []

for i in range(n_elementos):
    print("Elemento {}".format(i + 1))
    xp1 = float(input("x(p1): "))
    yp1 = float(input("y(p1): "))
    print(15*"-")
    xp2 = float(input("x(p2): "))
    yp2 = float(input("y(p2): "))

    xp1s.append(xp1)
    yp1s.append(yp1)
    xp2s.append(xp2)
    yp2s.append(yp2)

    comprimento = ((xp2 - xp1)**2 + (yp2 - yp1)**2)**.5

    vvs.append([xp2 - xp1, yp2 - yp1])
    Ls.append(comprimento)

print("vvs:", vvs)

for i in range(len(vvs)):
    cosAlpha = (x1*vvs[i][0] + y1*vvs[i][1])/(((x1**2 + y1**2)**.5)*((vvs[i][0]**2+vvs[i][1]**2)**.5))

    if (vvs[i][0] >= 0 and vvs[i][1] >= 0) or (vvs[i][0] <= 0 <= vvs[i][1]):
        fis.append(float(acos(cosAlpha)*180/pi))
    elif vvs[i][0] <= 0 and vvs[i][1] <= 0:
        fis.append(float(acos(cosAlpha)*180/pi + 2*(180 - acos(cosAlpha)*180/pi)))
    elif vvs[i][0] >= 0 >= vvs[i][1]:
        fis.append(float(acos(cosAlpha)*180/pi + 360 - 2*acos(cosAlpha)*180/pi))
    else:
        fis.append("ok")

print("ângulos: {}".format(fis))
print("comprimentos: {}".format(Ls))

Es = [30*10**6, 30*10**6, 30*10**6, 30*10**6]  # SI
As = [.0490874, .0490874, .0490874, .0490874]  # SI

lista = []

for i in range(len(fis)):
    fi = float(fis[i]*pi/180)
    E = float(Es[i])
    A = float(As[i])
    L = float(Ls[i])

    cte = E*A/L*.001

    aA = cte*(cos(x) ** 2).subs(x, fi)
    bB = cte*(cos(x)*sin(x)).subs(x, fi)
    cC = cte*(-cos(x)**2).subs(x, fi)
    dD = cte*(-cos(x)*sin(x)).subs(x, fi)
    eE = cte*(cos(x)*sin(x)).subs(x, fi)
    fF = cte*(sin(x)**2).subs(x, fi)
    gG = cte*(-cos(x)*sin(x)).subs(x, fi)
    hH = cte*(-sin(x)**2).subs(x, fi)
    iI = cte*(-cos(x)**2).subs(x, fi)
    jJ = cte*(-cos(x)*sin(x)).subs(x, fi)
    kK = cte*(cos(x)*sin(x)).subs(x, fi)
    lL = cte*(cos(x)**2).subs(x, fi)
    mM = cte*(-cos(x)*sin(x)).subs(x, fi)
    nN = cte*(-sin(x)**2).subs(x, fi)
    oO = cte*(cos(x)*sin(x)).subs(x, fi)
    pP = cte*(sin(x)**2).subs(x, fi)

    k = [
        [aA, bB, cC, dD],
        [eE, fF, gG, hH],
        [iI, jJ, kK, lL],
        [mM, nN, oO, pP]
    ]
    lista.append(k)

    print('Elemento {}: {}'.format(i + 1, k))


listaGlobal = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

linha = []

for i in range(n_elementos):
    linha.append(i + 1)
    linha.append(i + 1)

indicesElementos = []
# indicesElementos = [[1, 2], [2, 4], [3, 4], [2, 3]]

print("Elementos e nós associados: ")
print(30*"-")
for i in range(n_elementos):
    print("Elemento {}: ".format(i + 1))
    n1 = int(input("Nó 1: "))
    n2 = int(input("Nó 2: "))
    print(30*"-")
    indicesElementos.append([n1, n2])

print(indicesElementos)

indices = [[0, 1, 2, 3], [2, 3, 4, 5]]  # Para cada elemento

"""
for j in range(len(indicesElementos)):
    for i in indicesElementos[j]:
        for item in range(len(linha)):
            if linha[item] == i:
                indices[j].append(item)
"""

print("indices =", indices)

for k in range(len(lista)):
    for (newItem, i) in zip(indices[k], range(0, 4, 1)):
        for (item, j) in zip(indices[k], range(0, 4, 1)):
            listaGlobal[newItem][item] += lista[k][i][j]

print(listaGlobal)










