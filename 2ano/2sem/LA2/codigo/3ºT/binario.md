<h1 style="text-align: center;">LA2 | Torneio 3 (2021/2022) | Binário</h1>

```Python

'''
Implemente uma função que calcula quantas sequências de n bits existem onde
não aparecem dois 1s seguidos.
Sugere-se que começe por definir uma função recursiva que calcula quantas 
sequências de n bits começadas por um dado bit existem onde não aparecem 
dois 1s seguidos.
'''


#####################
#        80%        #
#####################
def binario(n):
    if n == 0:
        return 0
    return aux(n-1, 0, {}) + aux(n-1, 1, {})
    
def aux(n, inicial, d):
    if (n, inicial) in d:
        return d[(n, inicial)]
    if n == 1:
        if inicial == 0:
            d[(n, inicial)] = 2
            return 2
        else:
            d[(n, inicial)] = 1
            return 1
        
    if inicial == 0:
        d[(n, inicial)] = aux(n-1, 0, d) + aux(n-1, 1, d)
        return d[(n, inicial)]
    else:
        d[(n, inicial)] = aux(n-1, 0, d)
        return d[(n, inicial)]
    
```


<br>


## Testes

```Python
# 1
n = 5
> Resultado = 13

# 2
n = 10
> Resultado = 144
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)