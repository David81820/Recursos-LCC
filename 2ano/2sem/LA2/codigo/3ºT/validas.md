<h1 style="text-align: center;">LA2 | Treino 3 | Válidas</h1>

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


<br>


## Testes

```Python
# 1
soma = 10
listas = [[8,1,7,3,3,6,3,5],[1,1,1,2,3,1,2],[3,3,3,3]]
> Resultado = [[8,1,7,3,3,6,3,5],[1,1,1,2,3,1,2]]

# 2
capacidade = 5
listas = [[1,1,1,1,1],[2],[3,3,3,3,3,3,3],[4],[5,5,5,5,5]]
> Resultado = [[1,1,1,1,1],[5,5,5,5,5]]
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)