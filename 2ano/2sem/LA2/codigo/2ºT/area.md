```Python

'''
Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 
'''

def area(p,mapa):
    xi, yi = p

    if mapa[yi][xi] == '*':
        return 0
    else:
        area = 1
        vis = {(xi,yi)}
        queue = [(xi,yi)]
        while queue:
            x,y = queue.pop(0)
            for i in [-1,0,1]:
                for k in [-1,0,1]:
                    if not abs(i)+abs(k)-2:
                        continue
                    if (x+i,y+k) in vis:
                        continue
                    if y + k >= 0 and y + k < len(mapa) and x + i >= 0 and x + i < len(mapa):
                        if mapa[y+k][x+i] == '*':
                            continue
                        vis.add((x+i,y+k))
                        area += 1
                        queue.append((x+i,y+k))

        return area


#############################################
#  Resolução usando algoritmos de travessia  #
#############################################

def build(mapa):
    adj = {}
    length = len(mapa)
    width = len(mapa[0])
    for y in range(length):
        for x in range(width):
            if mapa[y][x] == '*':
                continue
            elif (x, y) not in adj:
                adj[(x, y)] = set()
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if abs(i) + abs(j) == 2:
                        continue
                    if not 0 <= x+i < width:
                        continue
                    if not 0 <= y+j < length:
                        continue
                    if mapa[y+j][x+i] == '*':
                        continue
                    if (x+i, y+j) not in adj:
                        adj[(x+i, y+j)] = set()
                    
                    adj[(x, y)].add((x+i, y+j))
                    adj[(x+i, y+j)].add((x, y))
    return adj

def bfs(adj,o):
    custo = 0
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                custo += 1
                queue.append(d)
    return custo

def area(p,mapa):
    adj = build(mapa)
    custo = bfs(adj, p)
    return (custo, custo+1) [mapa[p[1]][p[0]] == '.' ]

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)