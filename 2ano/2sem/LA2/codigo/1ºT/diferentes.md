```Python

"""
Defina uma função que, dada uma lista de strings, retorne
essa lista ordenada por ordem decrescente do número de 
caracteres diferentes nela contidos.
Caso duas strings tenham o mesmo número de caracteres
diferentes a mais pequena em ordem lexicográfica deve
aparecer primeiro na lista retornada.
"""


def diferentes(frases):
    semrep = []
    for frase in frases:
        semrep.append( (frase, len(set(frase))) )
    semrep = [ x[0] for x in sorted(semrep, key = lambda x: (-x[1], x[0]) ) ]
    return semrep

```