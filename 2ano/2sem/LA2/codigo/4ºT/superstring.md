```Python

'''
Implemente um função que calcula a menor string que contém todas as palavras 
recebidas na lista de input. Assuma que todas as palavras são disjuntas entre si, 
ou seja, nunca haverá inputs onde uma das palavras está contida noutra.
'''


def complete(p,c,i):
    s = 0
    for palavra in p:
        if palavra not in c:
            return False
        s += c[palavra]
    return s == i

# enumera as extensões válidas para o candidato parcial c
def extensions(p,c,k,ind):
    if not ind:
        return [(palavra, len(palavra)) for palavra in p]
    l = list()
    last = ind[-1]
    for palavra in p:
        if palavra not in c:
            for j in range(len(palavra)-1, -1, -1):
                if last.endswith(palavra[:j]) and sum(c.values())+len(palavra)-j<=k:
                    l.append((palavra, len(palavra)-j))
    return l

# testa se um candidato c é uma solução válida para p
def valid(p,c):
    return True

def aux(p,c,k,ind):
    if complete(p,c,k):
        return valid(p,c)
    for i,x in extensions(p,c,k,ind):
        c[i] = x
        ind.append(i)
        if aux(p,c,k,ind):
            return True
        c.pop(i)
        ind.remove(i)
    return False

def superstring(strings):
    for i in range(0, sum(map(lambda x: len(x), strings))):
        c = dict()
        ind = []
        if aux(strings, c, i, ind):
            print(ind)
            s = ""
            for palavra in ind:
                s += palavra[(len(palavra)-c[palavra]):]
            return s
    s = ""
    for string in strings:
        s+=string
    return s

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)