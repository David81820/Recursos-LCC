<h1 style="text-align: center;">LA2 | Torneio 2 (2021/2022) | Distância</h1>

```Python

'''
Neste problema pretende-se que implemente uma função que calcula a distância
entre duas cidades num mapa.
O mapa é rectangular e definido por uma lista de strings de igual comprimento,
onde um caracter 'X' marca a existência de uma cidade e um '#' uma estrada.
Neste mapa só é possível viajar na horizontal ou na vertical. As cidades de
origem e destino são identificadas pelas respectivas coordenadas horizontal e
vertical, medidas a partir do canto superior esquerdo. Se as coordenadas destino
e origem não forem cidades a função deverá retornar None. Se não houver
caminho entre as duas cidades deverá retornar float("inf").
'''

def build(mapa):
    adj = {}
    length = len(mapa)
    width = len(mapa[0])

    for y in range(length):
        for x in range(width):
            if mapa[y][x] == ' ':
                continue
            if (x,y) not in adj:
                adj[(x,y)] = set()
            if 0 < x-1 < width and (mapa[y][x-1] == '#' or mapa[y][x-1] == 'X'):
                if (x-1,y) not in adj:
                    adj[(x-1,y)] = set()
                adj[(x,y)].add((x-1,y))
                adj[(x-1,y)].add((x,y))
            if 0 < x+1 < width and (mapa[y][x+1] == '#' or mapa[y][x+1] == 'X'):
                if (x+1,y) not in adj:
                    adj[(x+1,y)] = set()
                adj[(x,y)].add((x+1,y))
                adj[(x+1,y)].add((x,y))
            if 0 < y-1 < length and (mapa[y-1][x] == '#' or mapa[y-1][x] == 'X'):
                if (x,y-1) not in adj:
                    adj[(x,y-1)] = set()
                adj[(x,y)].add((x,y-1))
                adj[(x,y-1)].add((x,y))
            if 0 < y+1 < length and (mapa[y+1][x] == '#' or mapa[y+1][x] == 'X'):
                if (x,y+1) not in adj:
                    adj[(x,y+1)] = set()
                adj[(x,y)].add((x,y+1))
                adj[(x,y+1)].add((x,y))

    return adj


def bfs(adj,o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return pai


def caminho(adj,o,d):
    pai = bfs(adj,o)
    caminho = [d]
    while d in pai:
        d = pai[d]
        caminho.insert(0,d)
    return caminho


def distancia(mapa,o,d):
    if o[1] < 0 or o[1] >= len(mapa):
        return float("inf")
    if o[0] < 0 or o[0] >= len(mapa[0]):
        return float("inf")
    if d[1] < 0 or d[1] >= len(mapa):
        return float("inf")
    if d[0] < 0 or d[0] >= len(mapa[0]):
        return float("inf")

    if mapa[o[1]][o[0]] !=  'X':
        return None
    if mapa[d[1]][d[0]] !=  'X':
        return None

    adj = build(mapa)
    caminhofinal = caminho(adj, o, d)

    if caminhofinal[0] == d:
        return float("inf")
    else:
        return len(caminhofinal) -1

```


<br>


## Testes

```Python
# 1
mapa = ["#X###X",
        "#  #  ",
        "#X##  ",
        "     X",
        "  X###"]
o = (1,0)
d = (1,2)
> Resultado = 4

# 2
mapa = ["#X###X",
        "#  #  ",
        "#X##  ",
        "     X",
        "  X###"]
o = (1,0)
d = (1,1)
> Resultado = None
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)