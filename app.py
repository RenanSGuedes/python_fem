import streamlit as st
from PIL import Image
import numpy as np
from sympy import pi, sin, cos, symbols, acos
import matplotlib as mpl
import matplotlib.pyplot as plt
import array_to_latex as a2l
from mpl_toolkits.mplot3d import axes3d


def bmatrix(a):
    """Returns a LaTeX bmatrix

    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv += [r'\end{bmatrix}']
    return '\n'.join(rv)


x = symbols("x")

fis, Ls, Es, As = [], [], [], []
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
                                         value="0",
                                         key='x_key{}'.format(i),
                                         placeholder='x(p1)'), st.text_input('y(p1)',
                                                                             value="0",
                                                                             key='x_key{}'.format(i),
                                                                             type="default",
                                                                             placeholder='y(p1)'),

                xp2, yp2, Ei, D = [
                    st.text_input('x(p2)',
                                  value="0",
                                  key='x_key{}'.format(i),
                                  placeholder='x(p2)',
                                  disabled=False),
                    st.text_input('y(p2)',
                                  value="0",
                                  key='x_key{}'.format(i),
                                  placeholder='y(p2)',
                                  disabled=False),
                    st.text_input('Ei',
                                  value="0",
                                  key='x_key{}'.format(i),
                                  placeholder='Módulo de elasticidade',
                                  disabled=False),
                    st.text_input('D',
                                  value="0",
                                  key='x_key{}'.format(i),
                                  placeholder='Diâmetro da barra',
                                  disabled=False)
                ]
    else:
        with col2:
            with st.expander("Elemento {}".format(i + 1)):
                st.subheader("Elemento {}".format(i + 1))
                xp1, yp1 = st.text_input('x(p1)',
                                         value="0",
                                         key='x_key{}'.format(i),
                                         placeholder='x(p1)'), st.text_input('y(p1)',
                                                                             value="0",
                                                                             key='x_key{}'.format(i),
                                                                             type="default",
                                                                             placeholder='y(p1)'),

                xp2, yp2, Ei, D = [
                    st.text_input('x(p2)',
                                  value="0",
                                  key='x_key{}'.format(i),
                                  placeholder='x(p2)',
                                  disabled=False),
                    st.text_input('y(p2)',
                                  value="0",
                                  key='x_key{}'.format(i),
                                  placeholder='y(p2)',
                                  disabled=False),
                    st.text_input('Ei',
                                  value="0",
                                  key='x_key{}'.format(i),
                                  placeholder='Módulo de elasticidade',
                                  disabled=False),
                    st.text_input('D',
                                  value="0",
                                  key='x_key{}'.format(i),
                                  placeholder='Diâmetro da barra',
                                  disabled=False)
                ]

    xp1s.append(float(xp1))
    yp1s.append(float(yp1))
    xp2s.append(float(xp2))
    yp2s.append(float(yp2))

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

elevation = st.slider('Rotação 1', 0, 90, 0)
azimuth = st.slider('Rotação 2', 0, 360, 0)

fig = plt.figure(figsize=(8, 8))
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)
ax.plot3D(x, y, z, 'green')

ax.view_init(elevation, azimuth)

st.pyplot(fig)

