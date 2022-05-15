newElements = [
    [[0, 0, 0], [13.656068809997848, 7.637834395668932, 0]],
    [[12, 0, 0], [13.656068809997848, 7.637834395668932, 0]]
]

midPointNewElements = []

for i in range(len(newElements)):
    midPointNewElements.append([])

for j in range(3):
    for i in range(len(newElements)):
        midPoint = (newElements[i][0][j] + newElements[i][1][j])*.5
        midPointNewElements[i].append(midPoint)

print(midPointNewElements)