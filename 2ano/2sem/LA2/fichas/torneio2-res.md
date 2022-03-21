```Python

#--------------------------------------------------------------------------------------------------
#   ÁREA
#--------------------------------------------------------------------------------------------------

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
#  Approach usando algoritmos de travessia  #
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



#--------------------------------------------------------------------------------------------------
#   CAVALO
#--------------------------------------------------------------------------------------------------

'''
O objectivo deste problema é determinar quantos movimentos são necessários para 
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.
'''

def saltos(o,d):
    numsaltos = 0
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        x,y = queue.pop(0)
        if (x,y) == d:
            break
        for i in [-2,-1,1,2]:
            for k in [-2,-1,1,2]:
                if abs(i) != abs(k):
                    if (x+i,y+k) not in vis:
                        vis.add((x+i,y+k))
                        pai[(x+i,y+k)] = (x,y) 
                        queue.append((x+i,y+k))

    while d in pai:
        d = pai[d]
        numsaltos += 1
    return numsaltos



#--------------------------------------------------------------------------------------------------
#   CIDADE
#--------------------------------------------------------------------------------------------------

'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade, 
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os 
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a 
letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.
'''

def build(ruas):
    adj = {}

    for rua in ruas:
        c1 = rua[0]
        c2 = rua[-1]
        if c1 not in adj:
            adj[c1] = {}
        if c2 not in adj:
            adj[c2] = {}
        if c2 in adj[c1] and adj[c1][c2] < len(rua):
            continue
        adj[c1][c2] = len(rua)
        adj[c2][c1] = len(rua)

    return adj
  
####################################
#        Solved with dijkstra      #
####################################

def dijkstra(adj,o):
    pai = {}
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pai[d] = v
                dist[d] = dist[v] + adj[v][d]
    return pai

def tamanho(ruas):
    adj = build(ruas)
    dist = 0
    for cruz in adj.keys():
        pai = dijkstra(adj, cruz)
        for cruzd in adj.keys():
            if cruz != cruzd:
                temp = 0
                d = cruzd
                while d in pai:
                    temp += adj[d][pai[d]]
                    d = pai[d]
                dist = max(dist, temp)

    return dist
  
#########################################
#        Solved with Floy-Warshall      #
#########################################
  
def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist 


def tamanho(ruas):
    adj = build(ruas)
    dist = fw(adj)
    final = 0
    for i in adj:
        for k in adj:
            final = max(final, dist[i][k])
    return final
    
    
    
#--------------------------------------------------------------------------------------------------
#   CONTINENTE
#--------------------------------------------------------------------------------------------------

'''
O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.
'''

def build(vizinhos):
    adj = {}
    for fronteira in vizinhos:
        for pais in fronteira:
            if pais not in adj:
                adj[pais] = set()
            for pais2 in fronteira:
                if pais != pais2:
                    if pais2 not in adj:
                        adj[pais2] = set()
                    adj[pais].add(pais2)
    return adj

################################
#    Also possible with DFS    #
################################

def dfs(adj,o):
    return dfs_aux(adj,o,set())

def dfs_aux(adj,o,vis):
    vis.add(o)
    for d in adj[o]:
        if d not in vis:
            dfs_aux(adj,d,vis)
    return vis
################################

def bfs(adj,o):
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                queue.append(d)
    return vis

def maior(vizinhos):
    adj = build(vizinhos)
    vis = []
    tamanho = 0
    for fronteira in vizinhos:
        for pais in fronteira:
            if pais not in vis:
                continente = bfs(adj,pais)
                vis.append(list(continente))
                tamanho = max(tamanho, len(continente))
    return tamanho



#--------------------------------------------------------------------------------------------------
#   ERDOS
#--------------------------------------------------------------------------------------------------

'''
O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca de 1500 artigos, grande parte deles em 
pareceria com outros autores. O número de Erdos de Paul Erdos é 0. 
Para qualquer outro autor, o seu número de Erdos é igual ao menor 
número de Erdos de todos os seus co-autores mais 1. Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menores que um determinado 
valor. A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.
'''

def build(artigos):
    adj = {}
    for autores in artigos.values():
        for autor in autores:
            for autor2 in autores:
                if autor != autor2:
                    if autor not in adj:
                        adj[autor] = set()
                    if autor2 not in adj:
                        adj[autor2] = set()
                    adj[autor].add(autor2)
                    adj[autor2].add(autor)
    return adj

def bfs(adj, o):
    vis = {}
    vis[o] = 0
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis[d] = vis[v]+1
                queue.append(d)
    return vis

def erdos(artigos,n):
    adj = build(artigos)
    dictAutores = bfs(adj, "Paul Erdos")
    final = [ x for x, y in sorted(dictAutores.items(), key = lambda x: (x[1], x[0])) if y <= n ]
    
    return final



#--------------------------------------------------------------------------------------------------
#   LABIRINTO
#--------------------------------------------------------------------------------------------------

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
    o = (0,0)
    d = (len(mapa[0])-1 , len(mapa)-1)
    adj = build(mapa)
    pai = bfs(adj, d)
    final = ""

    while o in pai:
        dx = pai[o][0] - o[0]
        dy = pai[o][1] - o[1]
        if dx == 1 and dy == 0:
            final += 'E'
        elif dx == -1 and dy == 0:
            final += 'O'
        elif dx == 0 and dy == 1:
            final += 'S'
        elif dx == 0 and dy == -1:
            final += 'N'
        o = pai[o]

    return final



#--------------------------------------------------------------------------------------------------
#   TRAVESSIA
#--------------------------------------------------------------------------------------------------

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



#--------------------------------------------------------------------------------------------------
#   VIAGEM
#--------------------------------------------------------------------------------------------------

'''
Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.
'''

def build(rotas):
    adj = {}
    for rota in rotas:
        for i in range(0, len(rota)-2, 2):
            cid1 = rota[i]
            custo = rota[i+1]
            cid2 = rota[i+2]
            if cid1 not in adj:
                adj[cid1] = {}
            if cid2 not in adj:
                adj[cid2] = {}
            adj[cid1][cid2] = custo
            adj[cid2][cid1] = custo

    return adj

###############################
#     Dijkstra Version        #
###############################

def dijkstra(adj,o):
 pai = {}
 dist = {}
 dist[o] = 0
 orla = {o}
 while orla:
    v = min(orla,key=lambda x:dist[x])
    orla.remove(v)
    for d in adj[v]:
        if d not in dist:
            orla.add(d)
            dist[d] = float("inf")
        if dist[v] + adj[v][d] < dist[d]:
            pai[d] = v
            dist[d] = dist[v] + adj[v][d]
 return pai

def viagem(rotas,o,d):
    custo = 0

    adj = build(rotas)
    if d not in adj:
        return custo
    pai = dijkstra(adj, d)

    while o in pai:
        custo += adj[o][pai[o]]
        o = pai[o]

    return custo

####################################
#     Floyd-Warshal Version        #
####################################

def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist

def viagem(rotas,o,d):
    adj = build(rotas)
    if not len(adj):
        return 0
    dists = fw(adj)
    return dists[o][d]

```
