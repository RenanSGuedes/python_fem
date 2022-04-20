from sympy import pi, sin, cos, symbols, acos
# Subs in matrix: https://docs.sympy.org/latest/modules/matrices/matrices.html#operations-on-entries

x = symbols("x")

fis = []

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

    vvs.append([xp2 - xp1, yp2 - yp1])

print("vvs:", vvs)

for i in range(len(vvs)):
    cosAlpha = (x1*vvs[i][0] + y1*vvs[i][1])/(((x1**2 + y1**2)**.5)*((vvs[i][0]**2+vvs[i][1]**2)**.5))

    if (vvs[i][0] >= 0 and vvs[i][1] >= 0) or (vvs[i][0] <= 0 <= vvs[i][1]):
        fis.append(acos(cosAlpha)*180/pi)
    elif vvs[i][0] <= 0 and vvs[i][1] <= 0:
        fis.append(acos(cosAlpha)*180/pi + 2*(180 - acos(cosAlpha)*180/pi))
    elif vvs[i][0] >= 0 >= vvs[i][1]:
        fis.append(acos(cosAlpha)*180/pi + 360 - 2*acos(cosAlpha)*180/pi)
    else:
        fis.append("ok")

print(fis)

Es = [30*10**10, 30*10**10]  # SI
As = [pi*((.25*10**(-2))**2)/4, pi*((.25*10**(-2))**2)/4, pi*((.25*10**(-2))**2)/4, 4.91*10**(-2)]  # SI
Ls = [((12*10**(-2))**2 + (8*10**(-2))**2)**.5, 8*10**(-2), 9, 12]

lista = []

for i in range(len(fis)):
    fi = float(fis[i]*pi/180)
    E = float(Es[i])
    A = float(As[i])
    L = float(Ls[i])

    cte = E*A/L*.01

    aA = float("{:.2f}".format(cte*(cos(x) ** 2).subs(x, fi)))
    bB = float("{:.2f}".format(cte*(cos(x)*sin(x)).subs(x, fi)))
    cC = float("{:.2f}".format(cte*(-cos(x)**2).subs(x, fi)))
    dD = float("{:.2f}".format(cte*(-cos(x)*sin(x)).subs(x, fi)))
    eE = float("{:.2f}".format(cte*(cos(x)*sin(x)).subs(x, fi)))
    fF = float("{:.2f}".format(cte*(sin(x)**2).subs(x, fi)))
    gG = float("{:.2f}".format(cte*(-cos(x)*sin(x)).subs(x, fi)))
    hH = float("{:.2f}".format(cte*(-sin(x)**2).subs(x, fi)))
    iI = float("{:.2f}".format(cte*(-cos(x)**2).subs(x, fi)))
    jJ = float("{:.2f}".format(cte*(-cos(x)*sin(x)).subs(x, fi)))
    kK = float("{:.2f}".format(cte*(cos(x)*sin(x)).subs(x, fi)))
    lL = float("{:.2f}".format(cte*(cos(x)**2).subs(x, fi)))
    mM = float("{:.2f}".format(cte*(-cos(x)*sin(x)).subs(x, fi)))
    nN = float("{:.2f}".format(cte*(-sin(x)**2).subs(x, fi)))
    oO = float("{:.2f}".format(cte*(cos(x)*sin(x)).subs(x, fi)))
    pP = float("{:.2f}".format(cte*(sin(x)**2).subs(x, fi)))

    k = [
        [aA, bB, cC, dD],
        [eE, fF, gG, hH],
        [iI, jJ, kK, lL],
        [mM, nN, oO, pP]
    ]
    lista.append(k)

    print('Elemento {}: {}'.format(i + 1, k))

