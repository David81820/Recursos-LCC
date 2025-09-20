<h1 style="text-align: center;">LA2 | Treino 2 | Erdos</h1>

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


########################
    Resolução 80%
########################

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


########################
    Resolução 100%
########################

def erdos(artigos, n):
    coautores = {}
    for artigo, autores in artigos.items():
        for autor in autores:
            if autor not in coautores:
                coautores[autor] = set()
            coautores[autor].add(artigo)
    
    queue = ["Paul Erdos"]
    visited = set(queue)
    dist = {"Paul Erdos": 0}
    while queue:
        atual = queue.pop(0)
        if dist[atual] >= n:
            break
        for artigo in coautores.get(atual, set()):
            for autor in artigos[artigo]:
                if autor not in visited:
                    dist[autor] = dist[atual] + 1
                    visited.add(autor)
                    queue.append(autor)
    
    dist = sorted(dist.items(), key=lambda x: (x[1], x[0]))
    dist = [x[0] for x in dist]
    return dist

```


<br>


## Testes

```Python
# 1
artigos = {"Adaptive register allocation with a linear number of registers": {"Carole Delporte-Gallet","Hugues Fauconnier","Eli Gafni","Leslie Lamport"},
           "Oblivious collaboration": {"Yehuda Afek","Yakov Babichenko","Uriel Feige","Eli Gafni","Nati Linial","Benny Sudakov"},
           "Optima of dual integer linear programs": {"Ron Aharoni","Paul Erdos","Nati Linial"}}
n = 2
> Resultado = ['Paul Erdos', 'Nati Linial', 'Ron Aharoni', 'Benny Sudakov', 'Eli Gafni', 'Uriel Feige', 'Yakov Babichenko', 'Yehuda Afek']

# 2
artigos = {"Specifying systems": {"Leslie Lamport"}, "Optima of dual integer linear programs": {"Ron Aharoni","Paul Erdos","Nati Linial"}}
n = 1
> Resultado = ['Paul Erdos', 'Nati Linial', 'Ron Aharoni']
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)