```Python

'''
O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca de 1500 artigos, grande parte deles em 
pareceria com outros autores. O número de Erdos de Paul Erdos é 0. 
Para qualquer outro autor, o seu número de Erdos é igual ao menor 
número de Erdos de todos os seus co-autores mais 1. Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menores que um determinado 
valor. A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.
'''

def build(artigos):
    adj = {}
    for autores in artigos.values():
        for a1 in autores:
            for a2 in autores:
                if a1 != a2:
                    if a1 not in adj:
                        adj[a1] = set()
                    if a2 not in adj:
                        adj[a2] = set()
                    adj[a1].add(a2)
                    adj[a2].add(a1)
    return adj


def bfs(adj,o):
    vis = {}
    vis[o] = 0
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis[d] = vis[v]+1
                queue.append(d)
    return vis


def erdos(artigos,n):
    adj = build(artigos)
    g = bfs(adj,"Paul Erdos")
    res = [x for x,y in sorted( g.items(), key=lambda x:(x[1],x[0]) ) if y<=n]
    return res

```