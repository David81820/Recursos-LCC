<h1 style="text-align: center;">LA2 | Treino 2 | Continente</h1>

```Python

'''
O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.
'''

def build(vizinhos):
    adj = {}
    for fronteira in vizinhos:
        for pais in fronteira:
            if pais not in adj:
                adj[pais] = set()
            for pais2 in fronteira:
                if pais != pais2:
                    if pais2 not in adj:
                        adj[pais2] = set()
                    adj[pais].add(pais2)
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

def maior(vizinhos):
    adj = build(vizinhos)
    vis = []
    tamanho = 0
    for fronteira in vizinhos:
        for pais in fronteira:
            if pais not in vis:
                continente = bfs(adj,pais)
                vis.append(list(continente))
                tamanho = max(tamanho, len(continente))
    return tamanho


################################
#    Also possible with DFS    #
################################

def dfs(adj,o):
    return dfs_aux(adj,o,set())

def dfs_aux(adj,o,vis):
    vis.add(o)
    for d in adj[o]:
        if d not in vis:
            dfs_aux(adj,d,vis)
    return vis

def maior(vizinhos):
    adj = build(vizinhos)
    vis = []
    tamanho = 0
    for fronteira in vizinhos:
        for pais in fronteira:
            if pais not in vis:
                continente = dfs(adj,pais)
                vis.append(list(continente))
                tamanho = max(tamanho, len(continente))
    return tamanho
################################

```


<br>


## Testes

```Python
# 1
vizinhos = [["Portugal","Espanha"],["Espanha","França"],["França","Bélgica","Alemanha","Luxemburgo"],["Canada","Estados Unidos"]]
> Resultado = 6

# 2
vizinhos = [["Portugal","Espanha"],["Espanha","França"]]
> Resultado = 3
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)