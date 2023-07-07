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


###################################
#   Minha Resolução
###################################

def diferentes(frases):
    # Caso vazio
    if frases == []:
        return []
    
    
    numcardifFinal = [] # Lista que vai ter os numeros de carateres de cada string
    for string in frases: # Percorrer a lista frases
        numcardifAux = [] # Lista auxiliar que vai conter os carateres sem repetições de cada string
        for i in string: # Percorrer a string
            if not i in numcardifAux: # Se o carater lido não estiver em "numcardifAux", é adicionado à respetiva lista
                numcardifAux.append(i)
        numcardifFinal.append(len(numcardifAux)) # Adiciono o comprimento da lista "numcardifAux" que corresponde ao numero de carateres distintos da string
    Final = list(zip(frases, numcardifFinal)) # Criar uma lista de tuplos (string, numero de char)
    Final = sorted(Final, key=lambda x: (-x[1], x[0])) # Ordenar pela ordem decrescente do numero de carateres, depois crescente do comprimento da string e por fim por ordem alfabetica
    Final = [x[0] for x in Final] # Ir buscar só as strings
    return Final

```


<br>


## Testes

```Python
# 1
frases = ["olamundo","cienciasdacomputacao","pyhtonefixe"]
> Resultado = ['cienciasdacomputacao', 'pyhtonefixe', 'olamundo']

# 2
frases = ["abcdef","ghijkl","fedcba","acebdf"]
> Resultado = ['abcdef', 'acebdf', 'fedcba', 'ghijkl']
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)