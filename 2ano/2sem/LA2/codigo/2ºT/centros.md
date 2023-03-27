```Python

'''
Neste problema pertende-se calcular quais os vértices centrais
de um grafo pesado não orientado.
A excentricidade de um vértice é a distância desse vértice
ao vértice mais afastado. Os vértices centrais (ou centros) de
um grafo são os que tem excentricidade mínima.
Os vértices do grado são identificados por letras do alfabeto.
O grafo será descrito através de uma sequência de arestas. Cada
aresta é descrita por uma string onde o primeiro e último caracteres
identificam os vértices adjacentes e os digitos no meio o peso da 
respectiva aresta.
A função deverá devolver a lista com todos os centros ordenados
alfabeticamente.
Se o grafo não for ligado deve devolver None.
'''

def build(arestas):   
    adj = {}
    for aresta in arestas:
        if len(aresta) == 0:
            continue
        if len(aresta) <= 2:
            adj[aresta[0]] = {}
        else:
            if aresta[0] not in adj:
                adj[aresta[0]] = {}
            if aresta[-1] not in adj:
                adj[aresta[-1]] = {}
            if aresta[-1] in adj[aresta[0]]:
                if adj[aresta[0]][aresta[-1]] < int(aresta[1:-1]):
                    continue
            adj[aresta[0]][aresta[-1]] = int(aresta[1:-1])
            adj[aresta[-1]][aresta[0]] = int(aresta[1:-1])
    
    return adj


def bfs(adj,o):
    vis = {o}
    queue = [o]
    while queue:
         v = queue.pop(0)
         for d in adj[v]:
             if d not in vis:
                 vis.add(d)
                 queue.append(d)
    return vis


def ligado(adj): 
    for v in adj.keys():
        pai = bfs(adj, v)
        if len(pai) == len(adj.keys()):
            continue
        else:
            return False
        
    
    return True


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


def centros(arestas):
    if len(arestas) == 0:
        return []

    adj = build(arestas)

    if not ligado(adj):
        return None

    dist = fw(adj)
    minCentro = {}

    for centro, dists in dist.items():
        maxCentro = -1
        for centro2, distancia in dists.items():
            if centro == centro2:
                continue
            maxCentro = max(maxCentro, distancia)
        minCentro[centro] = maxCentro

    final = [ x for x in sorted(minCentro.items(), key = lambda x: x[1])]
    mindist = final[0][1]
    final2 = [x[0] for x in final if x[1] == mindist]

    final2.sort()
    return final2

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)