<h1 style="text-align: center;">LA2 | Treino 3 | Crescente</h1>

```Python

"""
Implemente uma função que dada uma sequência de inteiros, determinar o 
comprimento da maior sub-sequência (não necessariamente contígua) que se 
encontra ordenada de forma crescente.
Sugere-se que comece por implementar uma função auxiliar recursiva que determina 
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.
"""

#############################################
#  Resolução 1 = 90%
#############################################

def aux(i,l):
    n = 1
    last = i
    for x in l:
        if last<=x:
            n += 1
            last = x
    return n

def crescente(lista):
    if len(lista)==0:
        return 0
    elif len(lista)==1:
        return 1
    res = []
    for i in range(1, len(lista)):
        res.append(aux(lista[0],lista[i:]))
    return max(res)


#############################################
#  Resolução 2 = 100%
#############################################

def crescente(lista):
    n = len(lista)
    if n == 0:
        return 0
    dic = {n-1:1}
    i = n-2
    while i>=0:
        dic[i] = 1
        mx = 0
        for j in range(i+1, n):
            if (lista[i]<=lista[j] and dic[j]>mx):
                mx = dic[j]
        dic[i] += mx
        i-=1
    return max(dic.values())


#############################################
#  Resolução 3 = 100%
#############################################

def crescente(lista):
    n = len(lista)
    if n == 0:
        return 0
    cache = [1 for x in range(n+1)]
    cache[0] = 0
    maxSub = 1
    for x in range(2, n+1):
        for y in range(x-1, 0, -1):
            if lista[x-1] >= lista[y-1]:
                cache[x] = max(cache[x], cache[y] + 1)
        
        maxSub = max(maxSub, cache[x])
        return maxSub

```


<br>


## Testes

```Python
# 1
lista = [5,2,7,4,3,8]
> Resultado = 3

# 2
lista = [15,27,14,38,26,55,46,65,85]
> Resultado = 6
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)