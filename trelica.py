
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

for i in range(len(fis)):
    fi = fis[i]
    E = Es[i]
    A = As[i]
    L = Ls[i]

    k = E*A*10**(-3)/L*Matrix([
        [(cos(x) ** 2).subs(x, fi), (cos(x) * sin(x)).subs(x, fi), (-cos(x) ** 2).subs(x, fi), (-cos(x) * sin(x)).subs(x, fi)],
        [(cos(x) * sin(x)).subs(x, fi), (sin(x) ** 2).subs(x, fi), (-cos(x) * sin(x)).subs(x, fi), (-sin(x) ** 2).subs(x, fi)],
        [(-cos(x) ** 2).subs(x, fi), (-cos(x) * sin(x)).subs(x, fi), (cos(x) ** 2).subs(x, fi), cos(x) * sin(x).subs(x, fi)],
        [(-cos(x) * sin(x)).subs(x, fi), (-sin(x) ** 2).subs(x, fi), (cos(x) * sin(x)).subs(x, fi), (sin(x) ** 2).subs(x, fi)]
    ])
    print('Elemento {}: {}'.format(i + 1, k))
