# Desenvolvimento de aplicação para cálculo estrutural em telhados de estufas 🍂

## Conceitos aplicados 🧠
 
O programa elaborado representa uma rotina de cálculo para estruturas de treliça em <em>green houses</em>. Escolheu-se Python como linguagem a ser utilizada para os cálculos da aplicação. A partir disso, é visado vincular o retorno do programa com ferramentas <em>web</em> para estender a abstração do programa de forma acessível a diferentes públicos, de modo a permitir que, em especial, o pequeno produtor familiar, que em muitos casos é desprovido de alto nível tecnológico em sua propriedade, possa elaborar sua própria estrutura a partir da análise feita pelo <em>website</em>.

## Bibliotecas do programa 📙

Utilizaram-se os módulos `itertools` e `numpy` para a primeira parte do algoritmo. O primeiro é uma ferramenta funcional para criar e usar iteradores. Aplicando o método `product` foi possível criar combinações de dois números visando a inserção dos valores de constante de rigidez dos elementos na matriz de rigidez global com base nos índices associados aos nós dos mesmos. O código a seguir fornece um exemplo da utilização deste recurso

### Código 💻
````python
from itertools import * 

coords = []
print('Coordenadas (Duplo <enter> finaliza o input)')
print('nós conectados')

i = input()

while i != '':
    coords.append([float(s) for s in i.split()])
    i = input()

lista_posicoes = []         

for i in coords:
    lista_posicoes.append(list(product(i, repeat=2)))
print("lista_posicoes: {}".format(lista_posicoes))
````

### Esquema de saída 📤
````python
lista_com_nos = [[1, 2], [2, 3], [1, 3], [3, 4]]

lista_de_tuplas_de_saida = [
    [(1, 1), (1, 2), (2, 1), (2, 2)],
    [(2, 2), (2, 3), (3, 2), (3, 3)],
    [(1, 1), (1, 3), (3, 1), (3, 3)],
    [(3, 3), (3, 4), (4, 3), (4, 4)]
]
````

### Construindo a matriz de rigidez global 
Nesta etapa, criou-se uma lista que representa a matriz de rigidez global com a dimensão sendo dada a partir do produto entre o número de elementos da estrutura e os graus de liberdade de cada nó. Dessa forma, para 4 elementos e 2 graus de liberdade obtem-se a matriz 8x8 definida como `listaGlobal`.

Com relação a matriz de rigidez de cada elemento foi feito a criação de uma lista que armazena sublistas com as matrizes 4x4 de cada elemento visando melhorar a consulta dos valores do método iterativo.

```python
listaGlobal = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
lista = [
    [
        [0, 0, 0, 0],
        [0, 166.7, 0, -166.7],
        [0, 0, 0, 0],
        [0, -166.7, 0, 166.7],
    ],
    [
        [64, -48, -64, 48],
        [-48, 36, 48, -36],
        [-64, 48, 64, -48],
        [48, -36, -48, 36]
    ],
    [
        [0, 0, 0, 0],
        [0, 166.7, 0, -166.7],
        [0, 0, 0, 0],
        [0, -166.7, 0, 166.7],
    ],
    [
        [125, 0, -125, 0],
        [0, 0, 0, 0],
        [-125, 0, 125, 0],
        [0, 0, 0, 0],
    ]
]
```

Com base na interação que cada elemento tem com os nós a ele associados, foi feito o incremento dos valores presentes em cada sublista (matriz de rigidez do elemento) à respectiva posição na `listaGlobal`. Para a situação analisada a `listaGlobal` após o processo iterativo deve apresentar os seguintes valores

````python
listaGlobal = [
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 166.7, 0, -166.7, 0, 0, 0, 0], 
    [0, 0, 189, -48, -125, 0, -64, 48], 
    [0, -166.7, -48, 202.7, 0, 0, 48, -36], 
    [0, 0, -125, 0, 125, 0, 0, 0], 
    [0, 0, 0, 0, 0, 166.7, 0, -166.7], 
    [0, 0, -64, 48, 0, 0, 64, -48], 
    [0, 0, 48, -36, 0, -166.7, -48, 202.7]
]
````

Entretanto, para chegar a essa passo o algoritmo precisa incrementar o valor da constante de rigidez de `lista[k][i][j]` a `listaGlobal[i][j]`. Para que isso ocorra, o laço de repetição deve apresentar as seguintes saídas

````python
listaGlobal = ["lista de listas"]
lista = ["lista com as matrizes de rigidez de cada elemento"]

listaGlobal[0][0] += lista[0][0][0]
listaGlobal[0][1] += lista[0][0][1]
listaGlobal[0][2] += lista[0][0][2]
listaGlobal[0][3] += lista[0][0][3]
listaGlobal[1][0] += lista[0][1][0]
listaGlobal[1][1] += lista[0][1][1]
listaGlobal[1][2] += lista[0][1][2]
listaGlobal[1][3] += lista[0][1][3]
listaGlobal[2][0] += lista[0][2][0]
listaGlobal[2][1] += lista[0][2][1]
listaGlobal[2][2] += lista[0][2][2]
listaGlobal[2][3] += lista[0][2][3]
listaGlobal[3][0] += lista[0][3][0]
listaGlobal[3][1] += lista[0][3][1]
listaGlobal[3][2] += lista[0][3][2]
listaGlobal[3][3] += lista[0][3][3]
````

A notação utilizada é uma forma resumida de incrementar um valor a uma posição de lista, podendo também ser encontrado da seguinte forma
````python
listaGlobal = ["lista de listas"]
lista = ["lista com as matrizes de rigidez de cada elemento"]

listaGlobal[0][0] = listaGlobal[0][0] + lista[0][0][0]
````

O laço de repetição que constrói os incrementos acima é

````python
listaGlobal = ["lista de listas"]
lista = ["lista com as matrizes de rigidez de cada elemento"]

indicesElementos = [[1, 2], [2, 4], [3, 4], [2, 3]]
linha = [1, 1, 2, 2, 3, 3, 4, 4]
indices = [[0, 1, 2, 3], [2, 3, 6, 7], [4, 5, 6, 7], [2, 3, 4, 5]]

for k in range(len(lista)):
    for (newItem, i) in zip(indices[k], range(0, 4, 1)):
        for (item, j) in zip(indices[k], range(0, 4, 1)):
            listaGlobal[newItem][item] += lista[k][i][j]
````

