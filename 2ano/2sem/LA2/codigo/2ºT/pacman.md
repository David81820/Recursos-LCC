<h1 style="text-align: center;">LA2 | Torneio 2 (2020/2021) | Deadcode</h1>

```Python

"""
Neste problema pretende-se que implemente uma função que ajude o Pac-Man a 
fugir dos fantasmas. Ir´á receber um mapa onde um '*' representa uma parede e 
um ' ' uma posição livre, onde 'P' marca a posição onde se encontra o Pac-Man e
'G' uma posição onde se encontra um fantasma. A função deve devolver a posição
para onde o Pac-Man se deve deslocar (uma das posições adjancentes, sendo que
apenas se pode movimentar na horizontal ou vertical, ou a posição onde se
encontra, se a melhor opção for ficar quieto), por forma a que fique o mais
distante possível de um fantasma. Caso haja mais do que uma posição ideal a 
prioridade deverá ser: ficar quieto, desloar-se para cima, deslocar-se para
baixo, deslocar-se para a direita, e deslocar-se para esquerda.
A posição consiste na coordenada horizontal (medida da esquerda para a direita)
e na coordenada vertical (medida de cima para baixo).
"""


import copy
import collections


def bfsLAux(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if x == len(grid)-1 and y == len(grid)-1:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid) and grid[y2][x2] != '*' and grid[y2][x2] != 'G' and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
            elif x2 == -1 and 0 <= y2 < len(grid) and grid[y2][len(grid[0])-1] != '*' and grid[y2][len(grid[0])-1] != 'G' and (len(grid[0])-1, y2) not in seen:
                queue.append(path + [(len(grid[0])-1, y2)])
                seen.add((len(grid[0])-1, y2))
            elif x2 == len(grid[0]) and 0 <= y2 < len(grid) and grid[y2][0] != '*' and grid[y2][0] != 'G' and (0, y2) not in seen:
                queue.append(path + [(0, y2)])
                seen.add((0, y2))
            elif 0 <= x2 < len(grid[0]) and y2 == -1 and grid[len(grid)-1][x2] != '*' and grid[len(grid)-1][x2] != 'G' and (x2, len(grid)-1) not in seen:
                queue.append(path + [(x2, len(grid)-1)])
                seen.add((x2, len(grid)-1))
            elif 0 <= x2 < len(grid[0]) and y2 == len(grid) and grid[0][x2] != '*' and grid[0][x2] != 'G' and (x2, 0) not in seen:
                queue.append(path + [(x2, 0)])
                seen.add((x2, 0))

    return seen


def bfsL(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == 'G':
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < len(grid) and 0 <= y2 < len(grid) and grid[y2][x2] != '*' and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
            elif x2 == -1 and 0 <= y2 < len(grid) and grid[y2][len(grid[0])-1] != '*' and (len(grid[0])-1, y2) not in seen:
                queue.append(path + [(len(grid[0])-1, y2)])
                seen.add((len(grid[0])-1, y2))
            elif x2 == len(grid[0]) and 0 <= y2 < len(grid) and grid[y2][0] != '*' and (0, y2) not in seen:
                queue.append(path + [(0, y2)])
                seen.add((0, y2))
            elif 0 <= x2 < len(grid[0]) and y2 == -1 and grid[len(grid)-1][x2] != '*' and (x2, len(grid)-1) not in seen:
                queue.append(path + [(x2, len(grid)-1)])
                seen.add((x2, len(grid)-1))
            elif 0 <= x2 < len(grid[0]) and y2 == len(grid) and grid[0][x2] != '*' and (x2, 0) not in seen:
                queue.append(path + [(x2, 0)])
                seen.add((x2, 0))
            
    return path


def pacman(mapa):

    pac = []
    for i in range(0, len(mapa[0])): # Percorrer x's
        for j in range(0, len(mapa)): # Percorrer y's
            if (mapa[j][i]) == 'P': # Se encontrar a posição do Pacman
                pac.append((i,j))
                break

    pi = pac[0] # Posição onde vai estar o Pacman

    teste = bfsLAux(mapa, pi) # Posições possíveis onde o Pacman pode ir
    teste.remove(pi) # Conjunto sem a posição inicial

    travs = []
    for n in teste:
        if bfsL(mapa, n) == None:
            travs.append(0)
        else:
            travs.append(len(bfsL(mapa, n)))

    indices = [i for i, x in enumerate(travs) if x == max(travs)]

    pf = 0

    if len(indices) == 1:
        pf = indices[0]
        auxiliar = list(teste)
        return auxiliar[pf]
    else:
        return pi

```


<br>


## Testes

```Python
# 1
mapa = ["*****",
        "*  G*",
        "* ***",
        "*P G*",
        "*****"]
> Resultado = (1,2)

# 2
mapa = ["******",
        "P G   ",
        "******"]
> Resultado = (5,1)
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)