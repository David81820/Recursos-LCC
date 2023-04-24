```Python

"""
Um ladrão assalta uma casa e, dado que tem uma capacidade de carga limitada, 
tem que decidir que objectos vai levar por forma a maximizar o potencial lucro. 

Implemente uma função que ajude o ladrão a decidir o que levar.
A função recebe a capacidade de carga do ladrão (em Kg) seguida de uma lista 
dos objectos existentes na casa, sendo cada um um triplo com o nome, o valor de 
venda no mercado negro, e o seu peso. Deve devolver o máximo lucro que o ladrão
poderá  obter para a capacidade de carga especificada.
"""


def sack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    
    if (wt[n-1] > W):
        return sack(W, wt[:n-1], val[:n-1], n-1)
    else:
        return max(val[n-1] + sack(W-wt[n-1], wt[:n-1], val[:n-1], n-1), sack(W, wt[:n-1], val[:n-1], n-1))


def ladrao(lim,obj):
    n = len(obj)
    v = []
    w = []
    for o in obj:
        v.append(o[1])
        w.append(o[2])
    res = sack(lim, w, v, n)
    return res

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)