<h1 style="text-align: center;">LA2 | Torneio 5 (2020/2021) | Número</h1>

```Python

"""
Implemente uma função que dados 0 < n <= 9 e k >= 0 devolva o menor número 
com exactamente duas ocorrências de todos os digitos entre 1 e n,
estando essas duas ocorrências à distância 1+k uma da outra.
"""


def distCerta(n,k,ls,i,oc,x):
    if len(oc[x]) == 0:
        return True
    if len(oc[x]) >= 2:
        return False
        
    return abs(oc[x][0] - i) == x+k

def valid(n,k,ls,i, oc):
    return True
    
def extensions(n,k,ls,i, oc):
    return [x for x in range(1,n+1) if distCerta(n,k,ls,i,oc,x)]
    
def search(n, k, ls, i, oc):
    if i == n*2:
        return valid(n,k,ls,i, oc)
        
    for x in extensions(n,k,ls,i, oc):
        ls.append(x)
        oc[x].append(i)
        if search(n,k,ls,i+1, oc):
            return True
        oc[x].pop()
        ls.pop()
    return False

def numero(n,k):
    ls = []
    oc = {}
    for x in range(1,n+1):
        oc[x] = []
    if search(n,k,ls,0, oc):
        return int("".join(map(str, ls)))

```

<br>


## Testes

```Python
# 1
n = 3
k = 1
> Resultado = 231213

# 2
n = 4
l = 0
> Resultado = 11342324
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)