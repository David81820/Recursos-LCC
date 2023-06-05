```Python

'''
Implemente uma função que dada uma lista de conjuntos de inteiros determine qual
o menor número desses conjuntos cuja união é idêntica à união de todos os 
conjuntos recebidos.
'''


# testa se o candidato c está completo
def complete(p,c,i,ind):
    return len(c) == i

# enumera as extensões válidas para o candidato parcial c
def extensions(p,c,ind):
    return [a for a in p if p.index(a)>ind and a not in c]

# testa se um candidato c é uma solução válida para p
def valid(p,c,m):
    new = set()
    for cand in c:
        new = new.union(cand)
    return len(new) == len(m)


def aux(p,c,i,m, ind):
    if complete(p,c,i,ind):
        return valid(p,c,m)
    
    for x in extensions(p,c,ind):
        c.append(x)
        if aux(p,c,i,m,p.index(x)):
            return True
        c.pop()
    return False


def uniao(sets):
    flag = True
    max_set = set()
    
    for sett in sets:
        if max_set.intersection(sett):
            flag = False
        max_set = max_set.union(sett)
        
    if flag:
        return len(sets)
    
    for i in range(0, len(sets)+1):
        if aux(sets, [], i, max_set, -1):
            return i
    return len(sets)

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)