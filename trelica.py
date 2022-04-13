from math import *
import sympy as sym
from sympy import *
from sympy.matrices import *

x = symbols("x")

# Matriz de rigidez do elemento


"""
k = E*A/L * [
    [cos2(x), cos(x)*sin(x), -cos2(x), -cos(x)*sin(x)],
    [cos(x)*sin(x), sin2(x), -cos(x)*sin(x), -sin2(x)],
    [-cos2(x), -cos(x)*sin(x), cos2(x), cos(x)*sin(x)],
    [-cos(x)*sin(x), -sin2(x), cos(x)*sin(x), sin2(x)]
]
"""

fis = [pi/2, 2.5, pi/2, pi]

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
