<h1 style="text-align: center;">LA2 | Treino 4 | Amigos</h1>

```Python

'''
Implemente uma função que descubra o maior conjunto de pessoas que se conhece 
mutuamente. A função recebe receber uma sequências de pares de pessoas que se 
conhecem e deverá devolver o tamanho do maior conjunto de pessoas em que todos 
conhecem todos os outros.
'''


# testa se o candidato c está completo
def complete(p,c,k):
    return len(c) == k


# enumera as extensões válidas para o candidato parcial c
def extensions(p,c,l,g):
    if len(c) == 0:
        return l
    else:
        r = list()
        for new in filter(lambda x: x>c[-1], l):
            for old in c:
                if new not in g[old] or old not in g[new]:
                    break
            else:
                r.append(new)
        return r


# testa se um candidato c é uma solução válida para p
def valid(p,c):
    return True


def aux(p,c,k,l,g):
    if complete(p,c,k):
        return valid(p,c)
    for x in extensions(p,c,l,g):
        c.append(x)
        if aux(p,c,k,l,g):
            return True
        c.pop()
    return False


def amigos(conhecidos):
    grafo = {}
    for x,y in conhecidos:
        if x not in grafo:
            grafo[x] = set()
        if y not in grafo:
            grafo[y] = set()
        grafo[x].add(y)
        grafo[y].add(x)
    
    for i in range(len(grafo.keys()), 0, -1):
        c = []
        if aux(conhecidos, c, i, (list(grafo.keys())), grafo):
            return i
    return 0

```


<br>


## Testes

```Python
# 1
conhecidos = {('pedro','maria'),('pedro','jose'),('pedro','manuel'),('maria','jose'),('maria','francisca'),('jose','francisca'),('francisca','manuel')}
> Resultado = 3

# 2
conhecidos = {('pedro','maria'),('jose','francisca'),('manuel','pedro')}
> Resultado = 2
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)