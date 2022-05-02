import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from sympy import pi, sin, cos, symbols, acos
import array_to_latex as a2l

x = symbols("x")

fis, Ls, Es, As = [], [], [], []
x1, y1 = 1, 0

vvs = []

xp1s, yp1s, xp2s, yp2s = [], [], [], []

st.title('Método dos Elementos Finitos')
image = Image.open('./greenhouse.jpg')
st.image(image, use_column_width=True)

st.write('A primeira parte considera a quantidade de elementos e coordenadas presentes na estrutura. Aqui os '
         'elementos representam a quantidade de barras da estrutura da treliça, enquanto que as coordenadas são os '
         'nós que ligam as barras entre si.')

col1, col2 = st.columns(2)

with col1:
    n_elementos = st.text_input('Número de elementos',
                                value="0",
                                max_chars=None,
                                key='123',
                                type="default",
                                help=None,
                                autocomplete=None,
                                on_change=None,
                                args=None,
                                kwargs=None,
                                placeholder='Elementos',
                                disabled=False)

with col2:
    coords = st.text_input('Número de coordenadas',
                           value="0",
                           max_chars=None,
                           key='345',
                           type="default",
                           help=None,
                           autocomplete=None,
                           on_change=None,
                           args=None,
                           kwargs=None,
                           placeholder='Coordenadas',
                           disabled=False)

st.header('Especificando os elementos')

for i in range(int(n_elementos)):
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

st.header(vvs)
