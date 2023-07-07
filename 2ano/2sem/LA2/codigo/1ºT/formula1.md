<h1 style="text-align: center;">LA2 | Torneio 1 (2021/2022) | Fórmula 1</h1>

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


###################################
#   Minha Resolução
###################################

def formula1(log):
    # Caso vazio
    if log == []:
        return []
    
    pilots = [x[1] for x in log] # Lista de pilotos
    pilots = list(set(pilots)) # Tira as repetições dos pilotos
    pilots = sorted(pilots, key=lambda x: x) # Ordena alfabeticamente
    pilotsAndtimes = [[x, [0]] for x in pilots] # Cria uma lista com [nomepiloto, [tempos]]
    for pt in log: # Percorre a lista dada
        for pandt in pilotsAndtimes: # Percorre a lista dos pilotos e tempo
            if pt[1] == pandt[0]: # Se os pilotos corresponderem, adiciono o tempo lido à lista de cada piloto em pilotsAndtimes
                pandt[1].append(pt[0])
                pandt[1].sort()
                break

    tempominimo = float("inf") # Tempo mais rápido de toda a prova
    for y in pilotsAndtimes: # Percorrer a lista pilotsAndtimes
        tempo = float("inf") # Tempo mais rápido do piloto
        for i in range(len(y[1]) - 1): # Percorrer a lista dos tempos
            diferenca = y[1][i+1] - y[1][i] # Fazer a diferença entre o tempo lido e o a seguir
            if (diferenca) < tempo: # Se a diferença for menor que o tempo mais rápido do piloto até ao momento, é substituido pela mesma
                tempo = diferenca
        if tempo < tempominimo: # Se o tempo do piloto for menor do que o tempo mais rápido registado até ao momento, é substituido pelo mesmo
            tempominimo = tempo
        y[1] = tempo # Substituir a lista dos tempos pelo tempo mais rápido do piloto
    pilotsAndtimes = [x for x in pilotsAndtimes if x[1] == tempominimo] # Retirar só os pilotos com o tempo menor igual ao mais rápido da corrida
    pilotsAndtimes = [x[0] for x in pilotsAndtimes] # Retirar apenas o nome dos pilotos
    return pilotsAndtimes

```


<br>


## Testes

```Python
# 1
log = [(20,"Alonso"),(20,"Rosberg"),(25,"Hamilton"),(35,"Rosberg"),(50,"Alonso"),(55,"Hamilton"),(70,"Hamilton"),(80,"Rosberg"),(70,"Alonso"),(100,"Alonso"),(120,"Hamilton")]
> Resultado = ['Hamilton', 'Rosberg']

# 2
log = [(20,"Alonso"),(25,"Hamilton"),(50,"Alonso"),(55,"Hamilton"),(70,"Hamilton"),(70,"Alonso")]
> Resultado = ['Hamilton']
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)