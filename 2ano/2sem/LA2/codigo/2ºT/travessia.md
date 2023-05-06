```Python

'''
Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar 
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo 
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.
'''

#############################################
#  Resolução 1 = 60%
#############################################

def build(mapa):
    adj = {}
    for x in range(len(mapa[0])):
        if abs(int(mapa[1][x]) - int(mapa[0][x])) <= 2:
            if (x,0) not in adj:
                adj[(x,0)] = {}
            if (x,1) not in adj:
                adj[(x,1)] = {}
            adj[(x,0)][(x,1)] = abs(int(mapa[1][x]) - int(mapa[0][x]))
            adj[(x,1)][(x,0)] = abs(int(mapa[1][x]) - int(mapa[0][x]))
            for y in range(1, len(mapa)):
                for x in range(1, len(mapa[0])):
                    if x != len(mapa[0])-1:
                        if abs(int(mapa[y][x+1]) - int(mapa[y][x])) <= 2:
                            if (x,y) not in adj:
                                adj[(x,y)] = {}
                            if (x+1,y) not in adj:
                                adj[(x+1,y)] = {}
                            adj[(x+1,y)][(x,y)] = abs(int(mapa[y][x+1]) - int(mapa[y][x]))
                            adj[(x,y)][(x+1,y)] = abs(int(mapa[y][x+1]) - int(mapa[y][x]))
                    if y != len(mapa)-1:
                        if abs(int(mapa[y+1][x]) - int(mapa[y][x])) <= 2:
                            if (x,y) not in adj:
                                adj[(x,y)] = {}
                            if (x,y+1) not in adj:
                                adj[(x,y+1)] = {}
                            adj[(x,y+1)][(x,y)] = abs(int(mapa[y+1][x]) - int(mapa[y][x]))
                            adj[(x,y)][(x,y+1)] = abs(int(mapa[y+1][x]) - int(mapa[y][x]))
    return adj


def dijkstra(adj, o):
    pai = {}
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla, key = lambda x: dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pai[d] = v
                dist[d] = dist[v] + adj[v][d]
    return pai


def travessia(mapa):
    adj = build(mapa)
    cheap = (-1, -1, 99)
    for i in range(len(mapa[0])):
        if (i,0) in adj.keys():
            pai = dijkstra(adj, (i,0))
            for k in range(len(mapa[0])):
                temp = 0
                d = (k,len(mapa)-1)
                caminho = [d]
                while d in pai:
                    temp += 1 + adj[d][pai[d]]
                    d = pai[d]
                    caminho.insert(0,d)
                print(caminho)
                print("custo",temp)
                if temp < cheap[2] and caminho[0][1] == 0:
                    cheap = (i, k, temp)
    return (cheap[0], cheap[2])



#############################################
#  Resolução 2 = 100%
#############################################

def verifica(mapa, i, j):
    return (0<=i<len(mapa[0]) and 0<=j<len(mapa))


def dijkstra(adj,o):
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x: dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                dist[d] = dist[v] + adj[v][d]
                
    return dist


def travessia(mapa):
    grafo = {}
    
    for j in range(len(mapa)):
        for i in range(len(mapa[0])):
            if (i,j) not in grafo:
                grafo[(i,j)] = {}
            
            #esquerda
            if(verifica(mapa, i-1, j) == True and abs(int(mapa[j][i]) - int(mapa[j][i-1])) <= 2):
                grafo[(i,j)][(i-1,j)] = 1 + abs(int(mapa[j][i]) - int(mapa[j][i-1]))
            #direita
            if(verifica(mapa, i+1, j) == True and abs(int(mapa[j][i]) - int(mapa[j][i+1])) <= 2):
                grafo[(i,j)][(i+1,j)] = 1 + abs(int(mapa[j][i]) - int(mapa[j][i+1]))
            #cima
            if(verifica(mapa, i, j-1) == True and abs(int(mapa[j][i]) - int(mapa[j-1][i])) <= 2):
                grafo[(i,j)][(i,j-1)] = 1 + abs(int(mapa[j][i]) - int(mapa[j-1][i]))
            #baixo
            if(verifica(mapa, i, j+1) == True and abs(int(mapa[j][i]) - int(mapa[j+1][i])) <= 2):
                grafo[(i,j)][(i,j+1)] = 1 + abs(int(mapa[j][i]) - int(mapa[j+1][i]))
            
    print(grafo)
    
    r = (0,0)
    dists = []
   
    for k in range(len(mapa[0])):
        custos = dijkstra(grafo, (k,0))
        for i in range(len(mapa[0])):
            if (i, len(mapa)-1) in custos:
                dists.append( (k, custos[(i,len(mapa)-1)])  )
        
    
    dists.sort(key = lambda x: (x[1],x[0]))
    print(dists)

    return dists[0]

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)