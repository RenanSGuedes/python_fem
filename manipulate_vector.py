"""
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

"""
