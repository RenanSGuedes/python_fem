from math import *

"""
    cos(alpha) = (x1*x2 + y1*y2)/((x1**2 + y1**2)**(-.5)(x2**2+y2**2)**(-.5))  
"""

x1 = 1
y1 = 0
x2 = float(input("x2: "))
y2 = float(input("y2: "))

cosAlpha = (x1*x2 + y1*y2)/(((x1**2 + y1**2)**.5)*((x2**2+y2**2)**.5))

if (x2 >= 0 and y2 >= 0) or (x2 <= 0 and y2 >= 0):
    print(acos(cosAlpha)*180/pi)
elif x2 <= 0 and y2 <= 0:
    print(acos(cosAlpha)*180/pi + 2*(180 - acos(cosAlpha)*180/pi))
elif x2 >= 0 and y2 <= 0:
    print(acos(cosAlpha)*180/pi + 360 - 2*acos(cosAlpha)*180/pi)
else:
    print("Excecao")


