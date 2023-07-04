<h1 style="text-align: center;">LA2 | Torneio 3 (2022/2023) | Duplica</h1>

```Python

'''
Optimize a seguinte função.
'''


def duplica(lista, dic={}):
    if len(lista) == 0:
        return 0
    if len(lista) == 1:
        return 2 * lista[0]

    if tuple(lista) in dic:
        return dic[tuple(lista)]

    a = lista[0] + duplica(lista[1:], dic)
    b = 2 * lista[0] + lista[1] + duplica(lista[2:], dic)
    res = max(a, b)
    dic[tuple(lista)] = res
    return res



#==================================
#           TESTES

# 1
lista = [5,1,3,4,5,3,1,3,3,5,5,1,2,3,4,5,1,3,4,5,3,1,3,3,5,5,1,2,3,4]
resultado = 149

# 2
lista = list(range(100))
restultado = 7450

# 3
lista = [5,3,2,4]
resultado = 23

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)