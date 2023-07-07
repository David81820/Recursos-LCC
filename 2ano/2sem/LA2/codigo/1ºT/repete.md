<h1 style="text-align: center;">LA2 | Treino 1 | Repete</h1>

```Python

'''
Implemente uma função que determine qual a menor sequência de caracters que
contém n repetições de uma determinada palavra
'''

def repete(palavra,n):
    maxeq = 0
    for i in range(1,len(palavra)):
        if palavra[:i] == palavra[-i:]:
            maxeq = i
    final = palavra
    final += (n-1) * palavra[maxeq:]
    
    if n != 0:   #Caso para 0 repeticoes (deve haver solucoes melhores)
        return final
    else:
        return ''

```


<br>


## Testes

```Python
# 1
palavra = "amanha"
n = 2
> Resultado = "amanhamanha"

# 2
palavra = "ola"
n = 3
> Resultado = "olaolaola"
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)