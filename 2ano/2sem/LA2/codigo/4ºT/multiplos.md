```Python

'''
Implemente uma função que determina quantas permutações dos n primeiros digitos 
são múltiplas de um dado número d. Por exemplo se n for 3 temos as seguintes 
permutações: 123, 132, 213, 231, 312, 321. Se neste caso d for 3 então todas 
as 6 permutações são múltiplas.
'''


# testa se o candidato c está completo
def complete(p,c):
    return len(c) == p

# enumera as extensões válidas para o candidato parcial c
def extensions(p,c):
    return [x for x in range(1, p+1) if x not in c]

# testa se um candidato c é uma solução válida para p
def valid(p,c,d):
    return int("".join(map(lambda i : str(i), c)))%d==0

def aux(p,c,d):
    if complete(p,c) and valid(p,c,d):
        return 1
    r = 0
    for x in extensions(p,c):
        c.append(x)
        r += aux(p,c,d)
        c.pop()
    return r
    
def multiplos(n,d):
    return aux(n,[],d)

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)