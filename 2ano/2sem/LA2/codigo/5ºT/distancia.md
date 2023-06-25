<h1 style="text-align: center;">Torneio 5 (2020/2021) | Distância</h1>

```Python

"""
Neste problema pretende-se calcular a distância mais curta entre cidades
num mapa. O mapa consiste numa matriz (definida como uma lista de listas) onde
uma letra representa uma cidade e um número uma estrada de largura igual a esse
número. A função a implementar, para além do mapa, da cidade origem, e da
cidade destino, recebe também a largura do veículo em que se pretende
fazer a viagem. Assuma que as cidades dadas existem no mapa, que o mapa está
bem formado, que os carros apenas se deslocam na horizontal e na vertical, e
que numa cidade consegue circular um carro de qualquer largura.

A função deve devolver -1 se não existir caminho entre as duas cidades.
Deve devolver -2 se existir caminho, mas não usando um carro da largura dada.
Noutro caso deve devolver o tamanho do caminho mais curto entre as duas cidades.
"""


def distancia(mapa,tamanho,origem,destino):

```

<br>


## Testes

```Python
# 1
mapa = ["   C43",
        "   2 3",
        "A33B45",
        "5  5  ",
        "4255  "]
tamanho = 3
origem = 'A'
destino = 'C'
> Resultado = 9

# 2
mapa = ["   C43",
        "   2 3",
        "A33B45",
        "5  5  ",
        "4255  "]
tamanho = 9
origem = 'A'
destino = 'C'
> Resultado = -2
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)