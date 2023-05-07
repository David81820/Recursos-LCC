```Python

"""
Um exemplo de um problema que pode ser resolvido de forma eficiente com 
programação dinâmica consiste em determinar, dada uma sequência arbitrária de 
números não negativos, se existe uma sub-sequência (não necessariamente contígua) 
cuja soma é um determinado valor. Implemente uma função que dado um valor e uma
listas de listas de números não negativos, devolva a lista com as listas com uma
sub-sequência cuja soma é o valor dado.
"""


def aux(sum,lst):
    conjunto = {0}
    for i in lst:
        aux = set()
        for e in conjunto:
            aux.add(e+i)
        conjunto = conjunto | aux
    return sum in conjunto
    

def validas(soma,listas):
    res = []
    for lista in listas:
        if aux(soma,lista):
           res.append(lista) 
    
    return res

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)