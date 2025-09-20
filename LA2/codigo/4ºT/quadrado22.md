<h1 style="text-align: center;">LA2 | Torneio 3 (2020/2021) | Quadrado</h1>

```Python

'''
O objectivo deste problema é descobir um quadrado latino. Um quadrado latino
de dimensão N é preenchido com número entre 1 e N, não podendo ter números
repetidos em nenhuma linha nem em nenhuma coluna.
Irá receber um quadrado parcialmente preenchido, representado como uma lista
de linhas, onde um 0 representa uma posição ainda não preenchida.
A função deverá prencher as posições com 0 por forma a obter um quadrado
latino. Assuma que tal é sempre possível.
Se houver mais do que um quadrado possível então deverá devolver o menor em
ordem lexicográfica.
'''


def complete(quadrado, N, linha, coluna):
    return linha > N - 1


def valid(quadrado, N):
    for i in range(N):
        l = quadrado[i]
        s = set(l)
        if len(l) != len(set(s)):
            return False
        c = [x[i] for x in quadrado]
        s = set(c)
        if len(c) != len(set(s)):
            return False
    return True


def extensions(quadrado, linha, coluna, N):
    listaLinha = quadrado[linha]
    listaColuna = [l[coluna] for l in quadrado]
    
    return [x for x in range(1, N+1) if x not in listaLinha and x not in listaColuna]


def proxPos(N, linha, coluna):
    if coluna == N - 1:
        return linha+1, 0
    return linha, coluna + 1


def aux(quadrado, linha, coluna, N):
    if complete(quadrado, N, linha, coluna):
        return valid(quadrado, N)
    l, c = proxPos(N, linha, coluna)
    
    if quadrado[linha][coluna] != 0:
        return aux(quadrado, l, c, N)
        
    for x in extensions(quadrado, linha, coluna, N):
        quadrado[linha][coluna] = x
        if aux(quadrado, l, c, N):
            return True
        quadrado[linha][coluna] = 0
        
    return False


def quadrado(q):
    aux(q, 0, 0, len(q))
    return q

```


<br>


## Testes

```Python
# 1
q = [[3,0,0],[0,0,0],[0,1,0]]
> Resultado = [[3, 2, 1], [1, 3, 2], [2, 1, 3]]

# 2
q = [[0,1],[0,0]]
> Resultado = [[2, 1], [1, 2]]
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)