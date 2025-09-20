<h1 style="text-align: center;">LA2 | Torneio 5 (2022/2023) | Centros</h1>

```Python

"""
Implemente uma função que determina os pontos centrais de uma figura.
Um ponto é central se a distância ao ponto mais afastado da
figura é a menor possível.
A lista com o resultado deve estar ordenada.
"""


def vertices(mapa):
    res = []
    aux = []
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if (mapa[i][j] == '#'):
                res.append((j, i))
                aux.append((j, i))
    
    final = [] 
    for vRes in res: 
        for vAux in aux:
            if vRes != vAux:
                if ( abs(vAux[0] - vRes[0]) == 1 ) and ( abs(vAux[1] - vRes[1]) == 0 ):
                    if (not (vRes, vAux, 1) in final) and (not (vAux, vRes, 1) in final):
                        final.append((vRes, vAux, 1))
                if ( abs(vAux[1] - vRes[1]) == 1 ) and ( abs(vAux[0] - vRes[0]) == 0 ):
                    if (not (vRes, vAux, 1) in final) and (not (vAux, vRes, 1) in final):
                        final.append((vRes, vAux, 1))
    return final



def build(arestas):
    adj = {}
    for o,d,p in arestas:
        if o not in adj:
            adj[o] = {}
        if d not in adj:
            adj[d] = {}
        adj[o][d] = p
        adj[d][o] = p
    return adj


def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist



def centros(mapa):
    v = vertices(mapa)
    b = build(v)
    aux = fw(b)

    dMin = 100000
    res = []
    for vfw in aux:
        dMax = 0
        for i in aux[vfw]:
            if aux[vfw][i] > dMax:
                dMax = aux[vfw][i]
        if dMax < dMin:
            dMin = dMax
        res.append([vfw,dMax])
    if dMin == float("inf"):
        return []

    res = sorted(res, key=lambda x: x[0])
    res = [x[0] for x in res if x[1] == dMin]

    return res

```

<br>


## Testes

```Python
# 1
mapa = ["..#..",
        "#####",
        "..#.."]
> Resultado = [(2,1)]

# 2
mapa = ["###",
        "#.#",
        "###."]
> Resultado = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)