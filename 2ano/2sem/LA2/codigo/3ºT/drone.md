<h1 style="text-align: center;">LA2 | Torneio 3 (2021/2022) | Drone</h1>

```Python

"""
Num armazém rectangular pretende-se usar um drone para recolher caixas de
objectos. O drone consegue transportar uma caixa de cada vez e apenas
consegue deslocar-se para a frente/trás ou para a esquerda/direita.
O armazém é descrito por um mapa onde um * assinala a posição para onde
devem ser recolhidas as caixas (e onde se encontra o drone inicialmente)
e um digito uma posição onde se encontra uma caixa, sendo o digito o
número de objectos contido na caixa. Para se deslocar uma posição o drone
demora 0.5 segundos. Implemente uma função que dado o mapa e o tempo de
autonomia do drone calcule o número máximo de objectos que ele irá 
conseguir recolher.
"""


import collections


def bfsLAux(grid, start, finish):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if x == finish[0] and y == finish[1]:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid) and grid[y2][x2] != '*' and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


def drone(mapa,tempo):
    
    aut = tempo*2
    pi = [0,0] # Posição inicial

    for i in range(0, len(mapa[0])): # Percorrer as linhas
        for j in range(0, len(mapa)): # Percorrer as colunas
            if (mapa[j][i] == '*'):
                pi[0], pi[1] = i, j
                break

    pi = tuple(pi)

    peso = []
    valor = []

    # Percorrer o mapa e encontrar a distancia de cada caixa e colocar em 'peso' e colocar o numero encontrado em 'valor'
    for i in range(0, len(mapa[0])): # Percorrer as linhas
        for j in range(0, len(mapa)): # Percorrer as colunas
            if (mapa[j][i] != ' ') and (mapa[j][i] != '*'):
                peso.append(2*(len(bfsLAux(mapa, pi, (i, j))) - 1))
                valor.append(int(mapa[j][i]))

    n = len(peso)

    return aux(aut, peso, valor, n)


def aux(W, wt, val, n):
 
    if n == 0 or W == 0:
        return 0
 
    if (wt[n-1] > W):
        return aux(W, wt, val, n-1)
 
    else:
        return max(val[n-1] + aux(W-wt[n-1], wt, val, n-1), aux(W, wt, val, n-1))

```


<br>


## Testes

```Python
# 1
mapa = ["*  5 8",
        "24    "]
tempo = 8
> Resultado = 14

# 2
mapa = [" 1 ",
        "2*2",
        " 1 "]
tempo = 2
> Resultado = 4
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)