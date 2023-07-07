Torneio 20/21



"""

Implemente uma função que calcula um quadrado de letras minúsculas de
dimensão n por n, tal que as letras em cada linha e em cada coluna
sejam todas diferentes. O quadrado deve ser representado por uma string
com n linhas (separadas por '\n') cada uma com n caracteres.
Para um dado n devolva a menor dessas strings em ordem lexicográfica.

"""

import string


def swap(s):
    t = len(s)
    r = ''
    x=0
    y=1
    while y<t:
        r.append(s[y])
        r.append(s[x])
        x+=2
        y+=2


def quadrado(n):
    
    ABC = 'abcdefghijklmnopqrstuvwxyz'
    
    str = [ABC[0:n]]

    i = 1
    if n<4:
        while i<n:
            str.append(ABC[i:n] + ABC[0:i])
            i+=1
        
        res = ''
        for j in str:
            res += j+'\n'
    
        return res[:-1]
    
    else:
        while i<n:
            if (i%2)==0:
                str.append(ABC[i:n] + ABC[0:i])
                i+=1
            else:
                str.append(swap(str[i-1]))
                i+=1
        
        res = ''
        for j in str:
            res += j+'\n'
    
        return res[:-1]






self.assertEqual(quadrado(3),'abc\nbca\ncab')
            
self.assertEqual(quadrado(4),'abcd\nbadc\ncdab\ndcba')