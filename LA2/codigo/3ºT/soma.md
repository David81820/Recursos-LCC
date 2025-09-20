<h1 style="text-align: center;">LA2 | Treino 3 | Soma</h1>

```Python

"""
Implemente uma função que calula qual a subsequência (contígua e não vazia) de 
uma sequência de inteiros (também não vazia) com a maior soma. A função deve 
devolver apenas o valor dessa maior soma.

Sugere-se que começe por implementar (usando recursividade) uma função que 
calcula o prefixo de uma sequência com a maior soma. Tendo essa função 
implementada, é relativamente adaptá-la para devolver também a maior soma de toda
a lista.
"""


def maxsoma(lista):
    sum = lista
    for i in range(1,len(lista)):
        sum[i] = max(sum[i-1]+lista[i], sum[i])
    return max(sum)

```


<br>


## Testes

```Python
# 1
lista = [-2,1,-3,4,-1,2,1,-5,4]
> Resultado = 6

# 2
lista = [1,2,3,4,-11,1,2,3,4,5]
> Resultado = 15
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)