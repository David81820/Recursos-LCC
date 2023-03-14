```Python

'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

def frequencia(texto):
    freq = {}
    for pal in texto.split():
        if pal not in freq.keys():
            freq[pal] = 1
        else:
            freq[pal] += 1
    
    result = [a for a,b in sorted(freq.items(), key = lambda x: (-x[1], x[0]))]
    return result

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)