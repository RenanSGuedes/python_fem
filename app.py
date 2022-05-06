import streamlit as st
from PIL import Image
import numpy as np
from sympy import pi, sin, cos, symbols, acos
import matplotlib.pyplot as plt


def bmatrix(par):
    """Returns a LaTeX bmatrix

    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(par.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(par).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv += [r'\end{bmatrix}']
    return '\n'.join(rv)


x = symbols("x")

fis, Ls, Es, As, points, elements = [], [], [], [], [], []
x1, y1 = 1, 0

vvs = []

xp1s, yp1s, xp2s, yp2s = [], [], [], []

st.title('Método dos Elementos Finitos')
image = Image.open('./struc.png')
st.image(image, use_column_width=True)

st.header('Especificando os elementos')

image = Image.open('./images/structure.png')
st.image(image, use_column_width=True)

st.write('A primeira parte considera a quantidade de elementos e coordenadas presentes na estrutura. Aqui os '
         'elementos representam a quantidade de barras da estrutura da treliça, enquanto que as coordenadas são os '
         'nós que ligam as barras entre si.')

col1, col2 = st.columns(2)

with col1:
    n_elementos = st.number_input('Número de elementos',
                                  min_value=1,
                                  max_value=100,
                                  value=1,
                                  step=1,
                                  key='id_n_elementos')

with col2:
    coords = st.number_input('Número de coordenadas',
                             min_value=1,
                             max_value=100,
                             value=1,
                             step=1,
                             key='id_coords')

for i in range(int(n_elementos)):
    if i % 2 == 0:
        with col1:
            with st.expander("Elemento {}".format(i + 1)):
                st.subheader("Elemento {}".format(i + 1))
                xp1, yp1 = st.text_input('x(p1)',
                                         value="{}".format(i + 1),
                                         key='x_key{}'.format(i),
                                         placeholder='x(p1)'), st.text_input('y(p1)',
                                                                             value="{}".format(i + 2),
                                                                             key='x_key{}'.format(i),
                                                                             type="default",
                                                                             placeholder='y(p1)'),

                xp2, yp2, Ei, D = [
                    st.text_input('x(p2)',
                                  value="{}".format(i + 3),
                                  key='x_key{}'.format(i),
                                  placeholder='x(p2)',
                                  disabled=False),
                    st.text_input('y(p2)',
                                  value="{}".format(i + 4),
                                  key='x_key{}'.format(i),
                                  placeholder='y(p2)',
                                  disabled=False),
                    st.text_input('Ei',
                                  value="30000000",
                                  key='x_key{}'.format(i),
                                  placeholder='Módulo de elasticidade',
                                  disabled=False),
                    st.text_input('D',
                                  value="0.25",
                                  key='x_key{}'.format(i),
                                  placeholder='Diâmetro da barra',
                                  disabled=False)
                ]
    else:
        with col2:
            with st.expander("Elemento {}".format(i + 1)):
                st.subheader("Elemento {}".format(i + 1))
                xp1, yp1 = st.text_input('x(p1)',
                                         value="{}".format(i + 1),
                                         key='x_key{}'.format(i),
                                         placeholder='x(p1)'), st.text_input('y(p1)',
                                                                             value="{}".format(i + 2),
                                                                             key='x_key{}'.format(i),
                                                                             type="default",
                                                                             placeholder='y(p1)'),

                xp2, yp2, Ei, D = [
                    st.text_input('x(p2)',
                                  value="{}".format(i + 3),
                                  key='x_key{}'.format(i),
                                  placeholder='x(p2)',
                                  disabled=False),
                    st.text_input('y(p2)',
                                  value="{}".format(i + 4),
                                  key='x_key{}'.format(i),
                                  placeholder='y(p2)',
                                  disabled=False),
                    st.text_input('Ei',
                                  value="30000000",
                                  key='x_key{}'.format(i),
                                  placeholder='Módulo de elasticidade',
                                  disabled=False),
                    st.text_input('D',
                                  value="0.25",
                                  key='x_key{}'.format(i),
                                  placeholder='Diâmetro da barra',
                                  disabled=False)
                ]

    xp1s.append(float(xp1))
    yp1s.append(float(yp1))
    xp2s.append(float(xp2))
    yp2s.append(float(yp2))

    if [xp1, yp1] not in points:
        points.append([xp1, yp1, 0])
    if [xp2, yp2] not in points:
        points.append([xp2, yp2, 0])

    elements.append([[float(xp1), float(yp1), 0], [float(xp2), float(yp2), 0]])

    comprimento = ((float(xp2) - float(xp1)) ** 2 + (float(yp2) - float(yp1)) ** 2) ** .5

    vvs.append([float(xp2) - float(xp1), float(yp2) - float(yp1)])
    Ls.append(comprimento)
    Es.append(Ei)
    As.append(pi / 4 * float(D) ** 2)

for i in range(len(vvs)):
    cosAlpha = (x1 * vvs[i][0] + y1 * vvs[i][1]) / (
            ((x1 ** 2 + y1 ** 2) ** .5) * ((vvs[i][0] ** 2 + vvs[i][1] ** 2) ** .5))

    if (vvs[i][0] >= 0 and vvs[i][1] >= 0) or (vvs[i][0] <= 0 <= vvs[i][1]):
        fis.append(float(acos(cosAlpha) * 180 / pi))
    elif vvs[i][0] <= 0 and vvs[i][1] <= 0:
        fis.append(float(acos(cosAlpha) * 180 / pi + 2 * (180 - acos(cosAlpha) * 180 / pi)))
    elif vvs[i][0] >= 0 >= vvs[i][1]:
        fis.append(float(acos(cosAlpha) * 180 / pi + 360 - 2 * acos(cosAlpha) * 180 / pi))
    else:
        fis.append("ok")

lista = []

st.header("Matriz de rigidez de cada elemento")
image = Image.open('./images/truss.png')
st.image(image, use_column_width=True)
for i in range(len(fis)):
    fi = float(fis[i] * pi / 180)
    E = float(Es[i])
    A = float(As[i])
    L = float(Ls[i])

    cte = E * A / L * .001

    aA = cte * (cos(x) ** 2).subs(x, fi)
    bB = cte * (cos(x) * sin(x)).subs(x, fi)
    cC = cte * (-cos(x) ** 2).subs(x, fi)
    dD = cte * (-cos(x) * sin(x)).subs(x, fi)
    eE = cte * (cos(x) * sin(x)).subs(x, fi)
    fF = cte * (sin(x) ** 2).subs(x, fi)
    gG = cte * (-cos(x) * sin(x)).subs(x, fi)
    hH = cte * (-sin(x) ** 2).subs(x, fi)
    iI = cte * (-cos(x) ** 2).subs(x, fi)
    jJ = cte * (-cos(x) * sin(x)).subs(x, fi)
    kK = cte * (cos(x) ** 2).subs(x, fi)
    lL = cte * (cos(x) * sin(x)).subs(x, fi)
    mM = cte * (-cos(x) * sin(x)).subs(x, fi)
    nN = cte * (-sin(x) ** 2).subs(x, fi)
    oO = cte * (cos(x) * sin(x)).subs(x, fi)
    pP = cte * (sin(x) ** 2).subs(x, fi)

    k = [
        [aA, bB, cC, dD],
        [eE, fF, gG, hH],
        [iI, jJ, kK, lL],
        [mM, nN, oO, pP]
    ]

    lista.append(k)

    for n in range(len(k)):
        for j in range(len(k)):
            k[n][j] = float(format(float(k[n][j]), ".1f"))

    kLaTeXForm = np.array(k)

    st.subheader('Matrix de rigidez do elemento {}'.format(i + 1))
    st.latex("k_{}={}".format(
        i + 1,
        bmatrix(kLaTeXForm)
    ))

# Define listaGlobal
listaGlobal = []

# Insere linhas em listaGlobal
for i in range(2 * int(coords)):
    listaGlobal.append([])

# Insere zeros nas linhas de listaGlobal
for i in range(2 * int(coords)):
    for j in range(2 * int(coords)):
        listaGlobal[i].append(0)

# Cria uma lista com os índices duplos que servirão de referência aos índices do python
linha = []

for i in range(int(coords)):
    linha.append(i + 1)
    linha.append(i + 1)

indicesElementos = []
# indicesElementos = [[1, 2], [2, 4], [3, 4], [2, 3]]

for i in range(int(n_elementos)):
    if i % 2 == 0:
        with col1:
            with st.expander("Elemento {}".format(i + 1)):
                n1 = st.number_input('n1',
                                     min_value=1,
                                     max_value=int(coords),
                                     value=1,
                                     step=1,
                                     key='id_n1_{}'.format(i))

                n2 = st.number_input('n2',
                                     min_value=1,
                                     max_value=int(coords),
                                     value=1,
                                     step=1,
                                     key='id_n2_{}'.format(i))

                indicesElementos.append([n1, n2])
    else:
        with col2:
            with st.expander("Elemento {}".format(i + 1)):
                n1 = st.number_input('n1',
                                     min_value=1,
                                     max_value=int(coords),
                                     value=1,
                                     step=1,
                                     key='id_n1_{}'.format(i))

                n2 = st.number_input('n2',
                                     min_value=1,
                                     max_value=int(coords),
                                     value=1,
                                     step=1,
                                     key='id_n2_{}'.format(i))

                indicesElementos.append([n1, n2])

indices = []

for i in range(int(n_elementos)):
    indices.append([])

for j in range(len(indicesElementos)):
    for i in indicesElementos[j]:
        for item in range(len(linha)):
            if linha[item] == i:
                indices[j].append(item)

for k in range(len(lista)):
    for (newItem, i) in zip(indices[k], range(0, 4, 1)):
        for (item, j) in zip(indices[k], range(0, 4, 1)):
            listaGlobal[newItem][item] += lista[k][i][j]

for i in range(len(listaGlobal)):
    for j in range(len(listaGlobal)):
        listaGlobal[i][j] = float(format(float(listaGlobal[i][j]), ".1f"))

listaGlobalNumpy = np.array(listaGlobal)

st.header('Matrix de rigidez global')
image = Image.open('images/clock.png')
st.image(image, use_column_width=True)
st.latex("K={}".format(
    bmatrix(listaGlobalNumpy)
))

# -------------------------------

elevation = st.slider('Elevação', 0, 90, 90)
azimuth = st.slider('Azimute', 0, 360, 0)

fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111, projection="3d")

for i in range(len(elements)):
    xs, ys, zs = zip(elements[i][0], elements[i][1])
    ax.plot(xs, ys, zs, color="blue", linewidth='3')

for i in range(len(points)):
    ax.scatter(float(points[i][0]), float(points[i][1]), points[i][2])

ax.set_xlim(-2, 13)
ax.set_ylim(-2, 13)
ax.set_zlim(-2, 13)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.grid(False)

ax.view_init(elevation, azimuth)

st.pyplot(fig)

# ----------------------------------------------------------------------------------------------------------------------

n_elementos_matriz_de_forcas = 2 * coords

forcas = []

for i in range(int(coords)):
    if i % 2 == 0:
        with col1:
            with st.expander("Nó {}".format(i + 1)):
                resposta = st.radio("Quais as restrições?", ('X', 'Y', 'XY', 'L'), key="radio_{}".format(i))

                if resposta == 'X':
                    novaResposta = st.number_input(
                        "Fy",
                        min_value=0,
                        max_value=100,
                        value=0,
                        key="nr{}".format(i),
                    )
                    forcas.append(['u{}:'.format(i + 1), 0])
                    forcas.append(['v{}:'.format(i + 1), novaResposta])
                elif resposta == 'Y':
                    novaResposta = st.number_input(
                        "Fx",
                        min_value=0,
                        max_value=100,
                        value=0,
                        key="nr{}".format(i),
                    )
                    forcas.append(['u{}:'.format(i + 1), novaResposta])
                    forcas.append(['v{}:'.format(i + 1), 0])
                elif resposta == 'XY':
                    for j in (['u', 'v']):
                        forcas.append(['{}{}'.format(j, i + 1), 'R'])
                else:
                    for (m, n) in zip(['x', 'y'], ['u', 'v']):
                        novaResposta = st.number_input(
                            "F{}".format(m),
                            min_value=0,
                            max_value=100,
                            value=0,
                            key="nr{}".format(i),
                        )
                        forcas.append(['{}{}'.format(n, i + 1), novaResposta])
    else:
        with col2:
            with st.expander("Nó {}".format(i + 1)):
                resposta = st.radio("Quais as restrições?", ('X', 'Y', 'XY', 'L'), key="radio_{}".format(i))

                if resposta == 'X':
                    novaResposta = st.number_input(
                        "Fy",
                        min_value=0,
                        max_value=100,
                        value=0,
                        key="nr{}".format(i),
                    )
                    forcas.append(['u{}:'.format(i + 1), 0])
                    forcas.append(['v{}:'.format(i + 1), novaResposta])
                elif resposta == 'Y':
                    novaResposta = st.number_input(
                        "Fx",
                        min_value=0,
                        max_value=100,
                        value=0,
                        key="nr{}".format(i),
                    )
                    forcas.append(['u{}:'.format(i + 1), novaResposta])
                    forcas.append(['v{}:'.format(i + 1), 0])
                elif resposta == 'XY':
                    for j in (['u', 'v']):
                        forcas.append(['{}{}'.format(j, i + 1), 'R'])
                else:
                    for (m, n) in zip(['x', 'y'], ['u', 'v']):
                        novaResposta = st.number_input(
                            "F{}".format(m),
                            min_value=0,
                            max_value=100,
                            value=0,
                            key="nr{}".format(i),
                        )
                        forcas.append(['{}{}'.format(n, i + 1), novaResposta])

forcasFiltradoComUeV = []
forcasFiltrado = []

for i in range(int(len(forcas))):
    if type(forcas[i][1]) == float or type(forcas[i][1]) == int:
        forcasFiltradoComUeV.append(forcas[i])

for i in range(int(len(forcas))):
    if type(forcas[i][1]) == float or type(forcas[i][1]) == int:
        forcasFiltrado.append(forcas[i][1])

st.write('forcas = {}'.format(forcas))
st.write('forcasFiltradoComUeV = {}'.format(forcasFiltradoComUeV))
st.write('forcasFiltrado = {}'.format(forcasFiltrado))

st.write(np.array(forcasFiltrado))

ccs = []

for item in forcas:
    if item[1] == 'R':
        ccs.append(forcas.index(item))

a = np.delete(listaGlobalNumpy, ccs, axis=1)
a = np.delete(a, ccs, axis=0)

numpyListInverse = np.linalg.inv(a)

deslocamentosNumpy = np.matmul(numpyListInverse, forcasFiltrado)
deslocamentosArray = deslocamentosNumpy.tolist()

st.write("deslocamentosArray", deslocamentosArray)

deslocamentosComUeV = []


for i in range(len(forcasFiltradoComUeV)):
    deslocamentosComUeV.append(('{}'.format(forcasFiltradoComUeV[i][0]), deslocamentosArray[i]))

st.write("deslocamentosComUeV", deslocamentosComUeV)

