from math import *
from sympy import *
from sympy.matrices import *

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

f1 = cos(x)**2
f2 = cos(x)*sin(x)
f3 = -cos(x)**2
f4 = -cos(x)*sin(x)
f5 = cos(x)*sin(x)
f6 = sin(x)**2
f7 = -cos(x)*sin(x)
f8 = -sin(x)**2
f9 = -cos(x)**2
f10 = -cos(x)*sin(x)
f11 = cos(x)**2
f12 = cos(x)*sin(x)
f13 = -cos(x)*sin(x)
f14 = -sin(x)**2
f15 = cos(x)*sin(x)
f16 = sin(x)**2

for i in range(len(fis)):
    fi = fis[i]
    E = Es[i]
    A = As[i]
    L = Ls[i]

    k = E*A*10**(-3)/L*Matrix([
        [f1.subs(x, fi), f2.subs(x, fi), f3.subs(x, fi), f4.subs(x, fi)],
        [f5.subs(x, fi), f6.subs(x, fi), f7.subs(x, fi), f8.subs(x, fi)],
        [f9.subs(x, fi), f10.subs(x, fi), f11.subs(x, fi), f12.subs(x, fi)],
        [f13.subs(x, fi), f14.subs(x, fi), f15.subs(x, fi), f16.subs(x, fi)]
    ])
    print('Elemento {}: {}'.format(i + 1, k))
