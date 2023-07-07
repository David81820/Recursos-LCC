<h1 style="text-align: center;">LA2 | Torneio 3 (2020/2021) | Quadrado</h1>

```Python

"""
Dadas duas strings de igual tamanho s1 e s2 a distância entre elas d(s1,s2) 
pode ser determinada pelo número de substituições de caracteres necessárias 
para transformar uma na outra (ou seja, o número de caracteres diferentes 
na mesma posição). Por exemplo d("cama","maca") == 2. 

Implemente uma função que, dado um conjunto de strings s1, ..., sn de igual 
tamanho (apenas com letras minúsculas), determine uma nova string s desse 
tamanho que seja o "centro" desse conjunto, isto é, tal que d(s,si) <= k 
para todo 1 <= i <= n e tal que k seja o menor possível. Se existir mais do 
que uma string nessas condições devolva a menor em ordem lexicográfica.
"""


def centro(strings):

```


<br>


## Testes

```Python
# 1
strings = ["ola","ole","elo"]
> Resultado = "olo"

# 2
strings = ["cama","saca","soca"]
> Resultado = "aaca"
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)