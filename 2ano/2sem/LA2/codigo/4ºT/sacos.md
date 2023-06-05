```Python

'''
Os sacos de um supermercado tem um limite de peso que conseguem levar. 
Implemente uma função que o ajude a determinar o número mínimo de sacos que 
necessita para levar todas as compras. A função recebe o peso máximo que os
sacos conseguem levar e uma lista com os pesos de todos os items que pretende 
comprar. Deverá devolver o número mínimo de sacos que necessita para levar 
todas as compras.
'''


def sacos(peso,compras):
    if len(compras) == 0:
        return 0
    minimo = sum(compras)//peso
    for i in range(minimo,len(compras)+1):
        if aux(peso, compras, [peso]*i):
            return i
            

def extensions(produto, list):
    return [i for i in range(len(list)) if list[i]-produto >=0]
    

def aux(peso, compras, list):
    if not compras:
        return True
    produto = compras.pop()
    for indexSaco in extensions(produto, list):
        list[indexSaco] -= produto
        if aux(peso, compras, list):
            return True
        list[indexSaco] += produto
    compras.append(produto)
    return False

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)