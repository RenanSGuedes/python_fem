from sympy import *

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

Es = [5*10**6, 5*10**6, 5*10**6, 5*10**6]
As = [4.91*10**(-2), 4.91*10**(-2), 4.91*10**(-2), 4.91*10**(-2)]
Ls = [9, 15, 9, 12]

for i in range(len(fis)):
    fi = fis[i]*pi/180
    E = Es[i]
    A = As[i]
    L = Ls[i]

    cte = E*A/L*10**(-3)

    k = [
        [cte*(cos(x)**2).subs(x, fi), cte*(cos(x)*sin(x)).subs(x, fi),
         cte*(-cos(x)**2).subs(x, fi), cte*(-cos(x)*sin(x)).subs(x, fi)],
        [cte*(cos(x)*sin(x)).subs(x, fi), cte*(sin(x)**2).subs(x, fi),
         cte*(-cos(x)*sin(x)).subs(x, fi), cte*(-sin(x)**2).subs(x, fi)],
        [cte*(-cos(x)**2).subs(x, fi), cte*(-cos(x)*sin(x)).subs(x, fi),
         cte*(cos(x)**2).subs(x, fi), cte*(cos(x)*sin(x)).subs(x, fi)],
        [cte*(-cos(x)*sin(x)).subs(x, fi), cte*(-sin(x)**2).subs(x, fi),
         cte*(cos(x)*sin(x)).subs(x, fi), cte*(sin(x)**2).subs(x, fi)]
    ]
    print('Elemento {}: {}'.format(i + 1, k))
