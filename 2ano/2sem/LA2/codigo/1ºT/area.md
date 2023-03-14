```Python

"""
Defina uma função que calcula a área de uma figura desenhada com pecas
lineares. A função recebe uma lista de pecas, onde para cada peça se indica
a sua localização no plano, a orientação (True significa horizontal e False
vertical), e a dimensão.
"""

def area(pecas):    # pensa nas peças como quadrados 2D, em cada um os lados medem 1 valor (e só percorre o quadrante dos valores positivos)
    loc = []                # array temporário onde iremos por os tuplos das coordenadas x/y onde os quadrados se encontram
    for x,y,o,a in pecas:       # x,y - localização inicial no eixo x/y  |  o - orientação (True = Horizontal, False = Vertical)  |  a - área, quantos quadrados são
        if o==True:
            for i in range(0,a):
                loc.append( (x+i,y) )
        elif o==False:
            for j in range(0,a):
                loc.append( (x,y+j) )
    
    loc = list(dict.fromkeys(loc))          # este comando remove quaisquer elementos repetidos do array - temos isto pois algumas peças vão-se interceptar no "gráfico", assim repetindo coordenadas x/y
    res = len(loc)                          # agora contamos o número total de quadrados, essa é a "área" pedida
    
    return res

```