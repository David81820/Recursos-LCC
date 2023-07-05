<h1 style="text-align: center;">LA2 | Treino 1 | Formata</h1>

```Python

"""
Implemente uma função que formata um programa em C.
O código será fornecido numa única linha e deverá introduzir
um '\n' após cada ';', '{', ou '}' (com excepção da última linha).
No caso do '{' as instruções seguintes deverão também estar identadas
2 espaços para a direita.
"""

def formata(codigo):
    ind = 0
    i = 0
    l = len(codigo)
    final = ""
    newline = True
    for c in codigo:
        i += 1
        if c == ';':
            final += c + ('\n'+ind*' ')*(i<l)
            newline = True
        elif c == '{':
            ind += 2
            final += c + ('\n'+ind*' ')*(i<l)
            newline = True
        elif c == '}':
            final = final[:-2]
            ind -= 2
            final += c + ('\n'+ind*' ')*(i<l)
            newline = True
        elif c == ' ' and newline:
            continue
        else:
            newline = False
            final += c
    
    return final


##############################
#    Solucao Alternativa     #
##############################

def formata(codigo):
    newline = True
    tab = 0
    final = ""
    for c in codigo:
        if newline and c == " ":
            continue
        elif c == '{':
            if newline:
                final += ' '*tab
            final += c +'\n'
            tab += 2
            newline = True
        elif c == '}':
            tab -= 2
            if newline:
                final += ' '*tab
            final += c +'\n'
            newline = True
        elif c == ';':
            if newline:
                final += ' '*tab
            final += c +'\n'
            newline = True
        else:
            if newline:
                final += ' '*tab
            final += c
            newline = False

    if newline:
        final = final[:-1]
    return final

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)