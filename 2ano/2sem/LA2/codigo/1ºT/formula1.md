```Python

"""
Implemente uma função que, dada uma lista com registos de instantes de tempo e nome de piloto, 
descrevendo os tempos de passagem pela meta dos varios pilotos numa corrida de F1, 
devolva a lista com os nomes dos pilotos com a volta mais rápida ordenada por ordem alfabética. 
Assuma que todos os pilotos iniciaram a prova no instante 0.
"""

def formula1(log):
    fastest = {}
    log.sort(key = lambda x: x[0])
    for tempo, driver in log:
        if driver not in fastest:
            fastest[driver] = [tempo, tempo]
        else:
            if tempo - fastest[driver][1] < fastest[driver][0]:
                fastest[driver][0] = tempo - fastest[driver][1]
        fastest[driver][1] = tempo
    
    final = []
    for driver, tempo in sorted(fastest.items(), key = lambda x: (x[1][0], x[0]) ):
        if len(final) == 0:
            mintime = tempo[0]
            final.append(driver)
        elif tempo[0] == mintime:
            final.append(driver)

    return final

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)