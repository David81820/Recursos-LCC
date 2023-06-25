<h1 style="text-align: center;">LA2 | Algoritmos de Grafos | Viagem 2022/2023</h1>

```Python

'''
Alguém pretende realizar uma viagem com início num determinado
aeroporto, e visitando em cada momento o aeroporto mais distante que
ainda não visitou. Implemente uma função que calcule o itinerário
que deve ser seguido. Para além do aeroporto de partida, irá receber uma 
lista com a descrição dos ligações existentes entre aeroportos, 
sendo que cada ligação consiste numa string com os dois códigos dos 
aeroportos, intercalados pela distância entre os mesmos. Se num determinado
ponto da viagem existirem dois aeroportos não visitados à mesma distância 
máxima deve ser visitado primeiro o que tiver o código mais pequeno 
em ordem lexicográfica.
'''


def build(voos):
    adj = {}
    for o, m, d in voos:
        if o not in adj:
            adj[o] = {}
        if d not in adj:
            adj[d] = {}
        adj[o][d] = m
        adj[d][o] = m
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


def div(voos):
    res = []
    for v in range(len(voos)):
        o = voos[v][:3]
        d = voos[v][-3:]
        m = voos[v][3:-3]
        res.append((o, int(m), d))
    return res


def cal(dist, inicio):
    res = [inicio]
    unvisited = set(dist.keys()) - {inicio}
    while unvisited:
        max_dist = float("-inf")
        next_airport = None
        for airport in unvisited:
            if dist[inicio][airport] > max_dist:
                max_dist = dist[inicio][airport]
                next_airport = airport
            elif dist[inicio][airport] == max_dist and airport < next_airport:
                next_airport = airport
        res.append(next_airport)
        inicio = next_airport
        unvisited.remove(next_airport)
    return res


def viagem(inicio, voos):
    if not voos:
        return []
    new = div(voos)
    adj = build(new)
    dist = fw(adj)
    res = cal(dist, inicio)
    return res

```

<br>


## Testes

```Python
# 1
voos = ["OPO300LIS","LIS150FAO","OPO500MAD","MAD500LIS"]
inicio = "OPO"
resultado = ["OPO","MAD","FAO","LIS"]

# 2
voos = ["OPO300LIS","LIS200FAO","OPO500MAD","MAD500LIS"]
inicio = "LIS"
resultado = ["LIS","MAD","FAO","OPO"]
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)