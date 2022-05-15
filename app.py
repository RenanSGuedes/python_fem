import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np
from sympy import pi, sin, cos, symbols, acos
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import copy


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

fis, Ls, Es, As, points, elements, elementsComNos, indicesElementos, Ds, deslocamentosAgrupados, = [], [], [], [], [], \
                                                                                                   [], [], [], [], []

x1, y1 = 1, 0

rows = []
vvs = []

xp1s, yp1s, xp2s, yp2s = [], [], [], []

with st.sidebar:
    st.title("Bem vindo!")
    image = Image.open('./images/bridge.png')
    st.image(image, use_column_width=True)

with st.sidebar.expander("Exemplos"):
    st.text('Básico')
    image = Image.open('./images/estrutura_2.png')
    st.image(image, use_column_width=True)
    with open('./csv_files/estrutura_2.csv', 'rb') as f:
        st.download_button('Baixar', f, file_name='estrutura_2.csv')

    st.text('Deformações')
    image = Image.open('./images/estrutura_11.png')
    st.image(image, use_column_width=True)
    with open('./csv_files/estrutura_11.csv', 'rb') as f:
        st.download_button('Baixar', f, file_name='estrutura_11.csv')

    st.text('Tensões + Deslocamentos')
    image = Image.open('./images/estrutura_36.png')
    st.image(image, use_column_width=True)
    with open('./csv_files/estrutura_36.csv', 'rb') as f:
        st.download_button('Baixar', f, file_name='estrutura_36.csv')

st.title('Método dos Elementos Finitos')
image = Image.open('./struc.png')
st.image(image, use_column_width=True)

st.header('Especificando os elementos')

image = Image.open('./images/structure.png')
st.image(image, use_column_width=True)

st.write('A primeira parte considera a quantidade de elementos e coordenadas presentes na estrutura. Aqui os '
         'elementos representam a quantidade de barras da estrutura da treliça, enquanto que as coordenadas são os '
         'nós que ligam as barras entre si.')

uploaded_file = st.file_uploader("Escolha um arquivo")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # Can be used wherever a "file-like" object is accepted:
    @st.cache(suppress_st_warning=True)
    def readCSVFile(file):
        return pd.read_csv(file)

    pandasToPythonList = readCSVFile(uploaded_file).values.tolist()

    for row in pandasToPythonList:
        rows.append(row)

for i in range(int(len(rows))):
    xp1, yp1, xp2, yp2, Ei, D = [
                        rows[i][0],
                        rows[i][1],
                        rows[i][2],
                        rows[i][3],
                        rows[i][4],
                        rows[i][5],
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
    Ds.append(D)
    As.append(pi / 4 * float(D) ** 2)

# -------------------------------------------------------------------------------------------
with st.sidebar.expander("Propriedades dos elementos"):

    if st.checkbox("Diâmetro"):
        modificarQuaisElementos = st.text_input(
            "Elementos (1 a {})".format(len(elements)),
            value='1',
            key='check_d',
            placeholder='1, 2, 4'
        )
        novoDiametro = st.number_input("D (m)", value=Ds[1])

        for i in range(len(modificarQuaisElementos.split(','))):
            Ds[int(modificarQuaisElementos.split(',')[i]) - 1] = novoDiametro
            As[int(modificarQuaisElementos.split(',')[i]) - 1] = pi / 4 * float(novoDiametro) ** 2

    if st.checkbox("Módulo de elasticidade"):
        modificarQuaisElementos = st.text_input(
            "Elementos (1 a {})".format(len(elements)),
            value='1',
            key='check_E',
            placeholder='1, 2, 4'
        )
        novoModuloE = st.number_input("E (MPa)", value=Es[1])

        for i in range(len(modificarQuaisElementos.split(','))):
            Es[int(modificarQuaisElementos.split(',')[i]) - 1] = novoModuloE

listaP, pontoNo = [], []

for item in elements:
    for j in range(2):
        listaP.append(item[j])

for i in range(len(listaP)):
    if listaP[i] not in pontoNo:
        pontoNo.append(listaP[i])

pontoNoAgrupado = []

for i in range(len(pontoNo)):
    pontoNoAgrupado.append([pontoNo[i], i + 1])

indicesElementos = copy.deepcopy(elements)

for i in range(len(elements)):
    for j in range(2):
        for k in range(len(pontoNoAgrupado)):
            if elements[i][j] == pontoNoAgrupado[k][0]:
                indicesElementos[i][j] = pontoNoAgrupado[k][1]

for i in range(len(indicesElementos)):
    elementsComNos.append([[indicesElementos[i][0], elements[i][0][0], elements[i][0][1]],
                           [indicesElementos[i][1], elements[i][1][0], elements[i][1][1]]])

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

with st.expander("Matriz de rigidez de cada elemento"):
    st.header("Matriz de rigidez de cada elemento")
    image = Image.open('./images/truss.png')
    st.image(image, use_column_width=True)
    for i in range(len(fis)):
        fi = float(fis[i] * pi / 180)
        E = float(Es[i])
        A = float(As[i])
        L = float(Ls[i])

        cte = E * A / L

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
        st.latex(r'''
            \textbf k_{}={}
        '''.format("{}".format("{" + str(i + 1) + "}"), bmatrix(kLaTeXForm))
                 )

# Define listaGlobal
listaGlobal = []

# Insere linhas em listaGlobal
for i in range(2 * len(pontoNo)):
    listaGlobal.append([])

# Insere zeros nas linhas de listaGlobal
for i in range(2 * len(pontoNo)):
    for j in range(2 * len(pontoNo)):
        listaGlobal[i].append(0)

# Cria uma lista com os índices duplos que servirão de referência aos índices do python
linha = []

for i in range(len(pontoNo)):
    linha.append(i + 1)
    linha.append(i + 1)

# indicesElementos = [[1, 2], [2, 4], [3, 4], [2, 3]]

indices = []

for i in range(len(rows)):
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

with st.expander("Matriz de rigidez global"):
    st.header('Matrix de rigidez global')
    image = Image.open('images/clock.png')
    st.image(image, use_column_width=True)
    st.latex(r"""
        \textbf K={}
        """.format(
        bmatrix(listaGlobalNumpy)
    ))

# -------------------------------

# PLOT ANTERIOR

# ----------------------------------------------------------------------------------------------------------------------

n_elementos_matriz_de_forcas = 2 * len(pontoNo)

forcas = []

col1, col2 = st.columns(2)

for i in range(len(pontoNo)):
    if i % 2 == 0:
        with col1:
            with st.expander("Nó {}".format(i + 1,
                                            pontoNo[i][0],
                                            pontoNo[i][1],
                                            pontoNo[i][2]
                                            )):
                resposta = st.radio("Quais as restrições?", ('X', 'Y', 'XY', 'L'), key="radio_{}".format(i),
                                    index=3)

                if resposta == 'X':
                    forcas.append(['u{}:'.format(i + 1), "R"])
                    forcas.append(['v{}:'.format(i + 1), 0])
                elif resposta == 'Y':
                    forcas.append(['u{}:'.format(i + 1), 0])
                    forcas.append(['v{}:'.format(i + 1), "R"])
                elif resposta == 'XY':
                    for j in (['u', 'v']):
                        forcas.append(['{}{}'.format(j, i + 1), 'R'])
                else:
                    for (m, n) in zip(['x', 'y'], ['u', 'v']):
                        novaResposta = st.number_input(
                            "F{} (N)".format(m),
                            value=0,
                            key="nr{}".format(i),
                        )
                        forcas.append(['{}{}'.format(n, i + 1), novaResposta])
    else:
        with col2:
            with st.expander("Nó {}".format(i + 1,
                                            pontoNo[i][0],
                                            pontoNo[i][1],
                                            pontoNo[i][2]
                                            )):
                resposta = st.radio("Quais as restrições?", ('X', 'Y', 'XY', 'L'), key="radio_{}".format(i),
                                    index=3)

                if resposta == 'X':
                    forcas.append(['u{}:'.format(i + 1), "R"])
                    forcas.append(['v{}:'.format(i + 1), 0])
                elif resposta == 'Y':
                    forcas.append(['u{}:'.format(i + 1), 0])
                    forcas.append(['v{}:'.format(i + 1), "R"])
                elif resposta == 'XY':
                    for j in (['u', 'v']):
                        forcas.append(['{}{}'.format(j, i + 1), 'R'])
                else:
                    for (m, n) in zip(['x', 'y'], ['u', 'v']):
                        novaResposta = st.number_input(
                            "F{} (N)".format(m),
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

ccs = []

for item in forcas:
    if item[1] == 'R':
        ccs.append(forcas.index(item))

a = np.delete(listaGlobalNumpy, ccs, axis=1)
a = np.delete(a, ccs, axis=0)

numpyListInverse = np.linalg.inv(a)

deslocamentosNumpy = np.matmul(numpyListInverse, forcasFiltrado)

deslocamentosArray = deslocamentosNumpy.tolist()
deslocamentosComUeV = []

for i in range(len(forcasFiltradoComUeV)):
    deslocamentosComUeV.append(('{}'.format(forcasFiltradoComUeV[i][0]), deslocamentosArray[i]))

for i in range(len(forcas)):
    for j in range(len(deslocamentosComUeV)):
        if forcas[i][1] == 'R':
            forcas[i][1] = 0
        elif forcas[i][0] == deslocamentosComUeV[j][0]:
            forcas[i][1] = deslocamentosComUeV[j][1]

for i in range(0, len(forcas), 1):
    del forcas[i][0]

deslocamentosAgrupados = []

for (i, j) in zip(range(0, len(forcas), 2), range(len(forcas))):
    deslocamentosAgrupados.append([j + 1, forcas[i][0], forcas[i + 1][0]])

col1, col2 = st.columns(2)

containerDeslocamentos = st.container()

with containerDeslocamentos.expander("Deslocamentos"):
    for i in range(len(deslocamentosAgrupados)):
        st.subheader("Nó {}".format(i + 1))
        st.write("u{}: {} m".format(i + 1, format(deslocamentosAgrupados[i][1], ".8f")))
        st.write("v{}: {} m".format(i + 1, format(deslocamentosAgrupados[i][2], ".8f")))

newElements = copy.deepcopy(elementsComNos)

for i in range(len(newElements)):
    for j in range(len(deslocamentosAgrupados)):
        for k in range(2):
            if newElements[i][k][0] == deslocamentosAgrupados[j][0]:
                newElements[i][k][1] += deslocamentosAgrupados[j][1]
                newElements[i][k][2] += deslocamentosAgrupados[j][2]

# Deleta os índices da primeira posição usados como referência
for i in range(len(newElements)):
    for j in range(2):
        del newElements[i][j][0]

# Acrescenta o 0 da terceira coordenada para a plotagem em 3D
for i in range(len(newElements)):
    for j in range(2):
        newElements[i][j].append(0)

novoComprimento = []
for i in range(len(newElements)):
    for j in range(1):
        comprimento = ((newElements[i][j][0] - newElements[i][j + 1][0]) ** 2 +
                       (newElements[i][j][1] - newElements[i][j + 1][1]) ** 2) ** .5

        novoComprimento.append(comprimento)

deformacoes = []

for i in range(len(novoComprimento)):
    epsilon = (novoComprimento[i] - Ls[i]) / Ls[i]

    deformacoes.append(epsilon)

tensoes = []

for i in range(len(deformacoes)):
    sigma = Es[i] * deformacoes[i]

    tensoes.append(sigma)

newPointsWithRep = copy.deepcopy(newElements)
for i in range(len(newElements)):
    for j in range(2):
        del newPointsWithRep[i][j][2]
        newPointsWithRep[i][j].append(0)

newPoints = []

for i in range(len(newPointsWithRep)):
    for j in range(2):
        if newPointsWithRep[i][j] not in newPoints:
            newPoints.append(newPointsWithRep[i][j])

# Tensão nos elementos

# ----------------------------------------------------------------------------------------------------

with st.expander("Gráfico"):
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111, projection="3d")

    with st.sidebar.expander("Visualização"):
        col1, col2 = st.columns(2)

        with col1:
            colorEstrutura = st.color_picker('Cor da estrutura', '#7159c1')
        with col2:
            colorDeformacao = st.color_picker('Cor da deformação', '#00f900')

        resposta = st.radio(
            "Gráficos",
            ('Estrutura', 'Estrutura + Deslocamentos', 'Estrutura + Deslocamentos + Tensões'))
        numerar = st.checkbox("Numerar nós")
        numerarPosDeformacao = st.checkbox("Numerar nós deslocados")
        numerarElems = st.checkbox("Numerar elementos")
        cotas = st.checkbox("Cotas e Grid")

        st.write("Rotação")
        elevation = st.slider('Elevação', 0, 90, 90)
        azimuth = st.slider('Azimute', 0, 360, 270)

    if resposta == 'Estrutura':
        for i in range(len(elements)):
            xs, ys, zs = zip(elements[i][0], elements[i][1])
            ax.plot(xs, ys, zs, color=colorEstrutura, linewidth=Ds[i] * 5)

        for i in range(len(points)):
            ax.scatter(float(points[i][0]), float(points[i][1]), points[i][2], s=10)

    elif resposta == 'Estrutura + Deslocamentos':
        for i in range(len(elements)):
            xs, ys, zs = zip(elements[i][0], elements[i][1])
            ax.plot(xs, ys, zs, color=(0, 0, 1, .1), linewidth=Ds[i] * 5)

        for i in range(len(points)):
            ax.scatter(float(points[i][0]), float(points[i][1]), points[i][2], s=5)

        for i in range(len(newElements)):
            xs, ys, zs = zip(newElements[i][0], newElements[i][1])
            ax.plot(xs, ys, zs, color=colorDeformacao, linewidth=Ds[i] * 5)
    else:
        for k in range(len(elements)):
            xs, ys, zs = zip(elements[k][0], elements[k][1])
            ax.plot(xs, ys, zs, color=(0, 0, 0, .1), linewidth=Ds[k] * 5)

        for i in range(len(newElements)):
            xs, ys, zs = zip(newElements[i][0], newElements[i][1])

            red_patch = mpatches.Patch(color='red', label='Maior tração')
            green_patch = mpatches.Patch(color=(0, 1, 0), label='Neutro')
            blue_patch = mpatches.Patch(color='blue', label='Maior compressão')

            for j in range(len(newPoints)):
                ax.scatter(float(newPoints[j][0]), float(newPoints[j][1]), newPoints[j][2], s=10)

            ax.legend(handles=[red_patch, green_patch, blue_patch])

            if tensoes[i] > .1*max(tensoes):
                ax.plot(xs, ys, zs, color=(tensoes[i] / max(tensoes), 0, 0), linewidth=Ds[i] * 5)
            elif tensoes[i] < .1*min(tensoes):
                ax.plot(xs, ys, zs, color=(0, 0, abs(tensoes[i] / min(tensoes))), linewidth=Ds[i] * 5)
            elif .1*max(tensoes) > tensoes[i] >= .1*min(tensoes):
                ax.plot(xs, ys, zs, color=(0, 1, 0), linewidth=Ds[i] * 5)

    xsMinMax, ysMinMax, zsMinMax = [], [], []

    for i in range(len(newElements)):
        for j in range(2):
            xsMinMax.append(newElements[i][j][0])
            ysMinMax.append(newElements[i][j][1])
            zsMinMax.append(newElements[i][j][2])

    if numerar:
        for i in range(len(pontoNo)):
            ax.text(pontoNo[i][0] + .2, pontoNo[i][1] + .2, pontoNo[i][2] + .2,
                    "{}".format(i + 1), color='black', ha='left', va='bottom', size=5)

    # Numerando os elementos
    midPointNewElements = []

    for i in range(len(newElements)):
        midPointNewElements.append([])

    for j in range(3):
        for i in range(len(newElements)):
            midPoint = (newElements[i][0][j] + newElements[i][1][j]) * .5
            midPointNewElements[i].append(midPoint)

    if numerarElems:
        for i in range(len(midPointNewElements)):
            ax.text(midPointNewElements[i][0] + .2, midPointNewElements[i][1] + .2, midPointNewElements[i][2] + .2,
                    "{}".format(i + 1), color='black', ha='left', va='bottom', size=4)

    if numerarPosDeformacao:
        for m in range(len(newPoints)):
            ax.text(newPoints[m][0] + .2, newPoints[m][1] + .2, newPoints[m][2] + .2,
                    "{}'".format(m + 1), color='black', ha='left', va='bottom', size=5)

    ax.set_xlim(min(xsMinMax) - 2, max(xsMinMax) + 2)
    ax.set_ylim(min(ysMinMax) - 2, max(ysMinMax) + 2)
    ax.set_zlim(min(zsMinMax) - 2, max(zsMinMax) + 2)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    if not cotas:
        ax.set_yticks([])
        ax.set_xticks([])
        ax.set_zticks([])

    ax.view_init(elevation, azimuth)

    st.pyplot(fig)

with st.sidebar.expander("Ajuda"):
    with open('./instructions/instructions.pdf', 'rb') as f:
        st.download_button('Documentação', f, file_name='instructions.pdf')

# -----------------------------------------------------------------------------------------------------------