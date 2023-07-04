<h1 style="text-align: center;">LA2 | Torneio 4 (2022/2023) | Segredo</h1>

```Python

'''
Implemente a uma função que dada uma palavra s só com minúsculas 
descubra a menor palavra com os mesmos caracteres que esteja à distância k
de s. A distância entre duas palavras com o mesmo tamanho é o número de
caracteres diferentes na mesma posição.
'''


def val(s1, s2, k):
    dist = 0
    for i1, i2 in zip(s1, s2):
        dist += abs(ord(i2) - ord(i1))
    return dist == k

def pal(s, k, x, v, u):
    if len(x) == len(s):
        if val(s, x, k):
            v.add(x)
        return
    for i in range(len(s)):
        if not u[i]:
            u[i] = True
            pal(s, k, x + s[i], v, u)
            u[i] = False

def search(s, k):
    p = set()
    falso = [False] * len(s)
    pal(s, k, "", p, falso)
    return p


def segredo(s, k):
    res = list(search(s, k))
    res.sort()
    return res[0]

```

<br>


## Testes

```Python
# 1
s = "abc"
k = 4
> Resultado = "bca"

# 2
s = "batata"
k = 36
> Resultado = "tabata"
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)