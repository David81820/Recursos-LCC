Torneio 2020/2021



"""

Implemente uma função que, dado um texto, duplique algumas palavras
por forma a obter o maior texto possível. A única restrição é que
não é possível duplicar duas palavras seguidas.
Caso haja mais do que um resultado possíveis com o mesmo comprimento máximo deve
retornar o menor deles em ordem lexicográfica.

"""

def aux3(texto, pal, pSort, n):
    
    w1 = pSort[:n-1]
    w2 = pSort[:n-2]
    
    res1 = ""
    for i in range(0,n-1):
        res1 += pal[i]+" "
        if (pal[i] in w1) and (pal[i+1] not in w1):
            res1 += pal[i]+" "
    if pal[i+1] in w1:
        res1 += pal[i+1]+" "+pal[i+1]
    f1 = len(res1)
    
    res2 = ""
    for j in range(0,n-1):
        res2 += pal[j]+" "
        if (pal[j] in w2) and (pal[j+1] not in w2):
            res2 += pal[j]+" "
    if pal[j+1] in w2:
        res2 += pal[j+1]+" "+pal[j+1]
    f2 = len(res2)
    
    if f1>f2:
        return res1
    else:
        return res2


def aux(texto, pal, pSort, n):
    
    w2 = pSort[:n-2]
    w3 = pSort[:n-3]
    
    res2 = ""
    for i in range(0,n-1):
        res2 += pal[i]+" "
        if (pal[i] in w2) and (pal[i+1] not in w2):
            res2 += pal[i]+" "
    if pal[i+1] in w2:
        res2 += pal[i+1]+" "+pal[i+1]
    f2 = len(res2)
    
    res3 = ""
    for j in range(0,n-1):
        res3 += pal[j]+" "
        if (pal[j] in w3) and (pal[j+1] not in w3):
            res3 += pal[j]+" "
    if pal[j+1] in w3:
        res3 += pal[j+1]+" "+pal[j+1]
    f3 = len(res3)
    
    if f2>f3:
        return res2
    else:
        return res3


def duplica(texto):
    
    words = texto.split()
    wSortLen = sorted(words, key=len)[::-1]
    t = len(words)
    
    if t==1:
        return texto+" "+texto
    elif t==2:
        for i in range(0,t):
            if words[i]==wSortLen[0]:
                words[i]+" "+words[i]+" "+words[i+1]
            else:
                words[i]+" "+words[i+1]+" "+words[i+1]
    elif t==3:
        return aux3(texto, words, wSortLen, t)
    elif t>3:
        return aux(texto, words, wSortLen, t)















texto = "hoje e dia de torneio"
            self.assertEqual(duplica(texto),"hoje hoje e dia dia de torneio torneio")

texto = "gosto muito de programar"
            self.assertEqual(duplica(texto),"gosto gosto muito de programar programar")