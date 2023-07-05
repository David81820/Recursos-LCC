<h1 style="text-align: center;">LA2 | Treino 2 | Viagem</h1>

```Python

'''
Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.
'''

def build(rotas):
    adj = {}
    for rota in rotas:
        for i in range(0,len(rota)-2,2):
            c1 = rota[i]
            p = rota[i+1]
            c2 = rota[i+2]
            if c1 not in adj:
                adj[c1] = {}
            if c2 not in adj:
                adj[c2] = {}
            adj[c1][c2] = p
            adj[c2][c1] = p
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


def viagem(rotas,o,d):
    adj = build(rotas)
    if not len(adj):    # verifica se o grafo não está vazio
        return 0
    res = fw(adj)
    return res[o][d]

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)