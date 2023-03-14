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

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)