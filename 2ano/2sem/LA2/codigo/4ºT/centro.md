Torneio 20/21



"""

Dadas duas strings de igual tamanho s1 e s2 a distância entre elas d(s1,s2) 
pode ser determinada pelo número de substituições de caracteres necessárias 
para transformar uma na outra (ou seja, o número de caracteres diferentes 
na mesma posição). Por exemplo d("cama","maca") == 2. 

Implemente uma função que, dado um conjunto de strings s1, ..., sn de igual 
tamanho (apenas com letras minúsculas), determine uma nova string s desse 
tamanho que seja o "centro" desse conjunto, isto é, tal que d(s,si) <= k 
para todo 1 <= i <= n e tal que k seja o menor possível. Se existir mais do 
que uma string nessas condições devolva a menor em ordem lexicográfica.

"""

import string
import copy

def distancia(c, strs):
    d = 0
    for s in strs:
        y = 0
        for i in range(0, len(s)):
            if (c[i] != s[i]):
                y += 1
        if y > d:
            d = y
    return d

def first4(h):
    return ['a']*h

def next4(h,c):
    i = len(c) - 1
    while i >= 0 and c[i] == 'z':
        c[i] = 'a'
        i = i-1
    if i < 0:
        return None
    c[i] = chr(ord(c[i])+1)
    return c

def search4(h, strings):
    final = []
    c = first4(h)
    final.append((c, distancia(c, strings)))
    while (c != None):
        d = copy.deepcopy(c)
        final.append((d, distancia(d, strings)))
        c = next4(h,d)

    dists = [y for (x, y) in final]
    minimo = min(dists)

    return [x for (x,y) in final if y == minimo]

def centro(strings):
    return min((search4(len(strings[0]), strings)))






strings = ["ola","ole","elo"]
            self.assertEqual(centro(strings),"olo")

strings = ["cama","saca","soca"]
            self.assertEqual(centro(strings),"aaca")