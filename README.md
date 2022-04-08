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