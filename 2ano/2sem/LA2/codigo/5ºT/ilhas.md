<h1 style="text-align: center;">Torneio 5 (2021/2022) | Ilhas</h1>

```Python

'''
Neste problema pretende-se que implemente uma função que calcula quantas
ilhas existem num mapa.

O mapa é rectangular e definido por uma lista de strings de igual comprimento,
onde um caracter '#' marca uma quadrícula com terra e um ' ' uma quadrícula com 
mar. A função deve devolver o número de ilhas no mapa.
'''


def ilhas(mapa):
    if mapa=="":
        return 0
    
    ilhas = []
    
    for i in mapa:
        if (i[0]=='#' and i[1]==' '):
            ilhas.append(i[0])
        elif (i[-1]=='#' and i[-2]==' '):
            ilhas.append(i[-1])
        else:
            t=len(i)
            x=1
            while x<t:
                if (i[x-1]==' ' and i[x]=='#' and i[x+1]==' '):
                    ilhas.append(i[x])
                x+=1
    
    r = len(ilhas)
    
    return r+1


###################################
# Resolução Alternativa
###################################

def bfs(c,adj, o, tamanhoX, tamanhoY):
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        anda = map(lambda x,y: (x[0]+y[0], x[1]+y[1]), [v]*4, [(0,1),(0,-1),(1,0),(-1,0)])
        for d in filter(lambda z: 0<=z[0]<tamanhoX and 0<=z[1]<tamanhoY,anda):
            if d not in vis:
                if adj[d[1]][d[0]] == '#':
                    vis.add(d)
                    queue.append(d)
    return vis

def ilhas(mapa):
    if not mapa:
        return 0
    tamanhoX = len(mapa[0])
    tamanhoY = len(mapa)
    cor = set()
    cori = 0
    for i,j in [(x,y) for x in range(tamanhoX) for y in range(tamanhoY)]:
        if mapa[j][i] == "#" and (i,j) not in cor:
            cori += 1
            cor = cor.union(bfs(cori, mapa, (i,j), tamanhoX, tamanhoY))
    return cori

```

<br>


## Testes

```Python
# 1
mapa = ["## ###",
        "## #  ",
        "#  #  ",
        "      ",
        "   ###"]
> Resultado = 3

# 2
mapa = ["## ###",
        "####  ",
        "#  #  ",
        "###   ",
        "   ###"]
> Resultado = 2
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)