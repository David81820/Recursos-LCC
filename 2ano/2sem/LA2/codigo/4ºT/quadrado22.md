<h1 style="text-align: center;">LA2 | Torneio 3 (2020/2021) | Quadrado</h1>

```Python

'''
O objectivo deste problema é descobir um quadrado latino. Um quadrado latino
de dimensão N é preenchido com número entre 1 e N, não podendo ter números
repetidos em nenhuma linha nem em nenhuma coluna.
Irá receber um quadrado parcialmente preenchido, representado como uma lista
de linhas, onde um 0 representa uma posição ainda não preenchida.
A função deverá prencher as posições com 0 por forma a obter um quadrado
latino. Assuma que tal é sempre possível.
Se houver mais do que um quadrado possível então deverá devolver o menor em
ordem lexicográfica.
'''


def quadrado(q):

```


<br>


## Testes

```Python
# 1
q = [[3,0,0],[0,0,0],[0,1,0]]
> Resultado = [[3, 2, 1], [1, 3, 2], [2, 1, 3]]

# 2
q = [[0,1],[0,0]]
> Resultado = [[2, 1], [1, 2]]
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)