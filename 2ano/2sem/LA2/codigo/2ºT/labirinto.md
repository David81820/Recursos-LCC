<h1 style="text-align: center;">LA2 | Treino 2 | Labirinto</h1>

```Python

'''
Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.
'''

def build(mapa):
    adj = {}
    length = len(mapa)
    width = len(mapa[0])
    for y in range(length):
        for x in range(width):
            if mapa[y][x] == '#':
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
                    if mapa[y+j][x+i] == '#':
                        continue
                    if (x+i, y+j) not in adj:
                        adj[(x+i, y+j)] = set()
                    
                    adj[(x, y)].add((x+i, y+j))
                    adj[(x+i, y+j)].add((x, y))
    return adj


def bfs(adj,o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return pai


def caminho(mapa):
    origem = (0,0)
    destino = (len(mapa)-1 , len(mapa[0])-1)
    
    adj = build(mapa)
    caminho = bfs(adj,destino)
    
    res = ""
    
    while origem in caminho:
        dx = caminho[origem][0] - origem[0]
        dy = caminho[origem][1] - origem[1]
        
        if dx==0 and dy==-1:
            res += 'N'
        elif dx==0 and dy==1:
            res += 'S'
        elif dx==1 and dy==0:
            res += 'E'
        elif dx==-1 and dy==0:
            res += 'O'
        
        origem = caminho[origem]
    
    return res

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)