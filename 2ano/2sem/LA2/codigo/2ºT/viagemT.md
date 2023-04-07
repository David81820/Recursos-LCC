```Python

'''
Alguém pretende realizar uma viagem com início num determinado
aeroporto, e visitando em cada momento o aeroporto mais distante que
ainda não visitou. Implemente uma função que calcule o itinerário
que deve ser seguido. Para além do aeroporto de partida, irá receber uma 
lista com a descrição dos ligações existentes entre aeroportos, 
sendo que cada ligação consiste numa string com os dois códigos dos 
aeroportos, intercalados pela distância entre os mesmos. Se num determinado
ponto da viagem existirem dois aeroportos não visitados à mesma distância 
máxima deve ser visitado primeiro o que tiver o código mais pequeno 
em ordem lexicográfica.
'''

# Ora o 1º problema deste exercício deve-se ao facto de que os elementos do array 'voos' não estão devidamente separados para usar-mos diretamente a função 'build'.
# Esta função divide cada elemento num "triplo" com o formato (origem, distância, destino).
def div(voos):
    res = []
    for v in range(0,len(voos)):
        o = voos[v][:3]             # tiramos os primeiros 3 charateres dum elemento
        d = voos[v][-3:]            # tiramos os últimos 3 charateres dum elemento
        m = voos[v][3:-3]           # tiramos os charateres do meio
        res.append((o,int(m),d))    # int(m) converte de char para int
    return res


def build(voos):
    adj = {}
    for o,m,d in voos:
        if o not in adj:
            adj[o] = {}
        if d not in adj:
            adj[d] = {}
        adj[o][d] = m
        adj[d][o] = m
    return adj


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


# Agora está aqui a verdadeira dor de cabeça...
# O exercício pede para devolver os voos mais distantes entre dois aeroportos, contudo não podemos repetir aeroportos.
# A dificuldade está não na lógica, mas na sintaxe. 
def cal(d,o,v):         # d = grafo / o = aeroporto de partida / v = lista de voos
    res = [o]                           # começa-mos por anexar o voo inicial
    for n in range (1,len(d.keys())):       # só saimos daqui quando tivermos todos aeroportos em 'res', por isso usamos .keys()
        elem = d[res[n-1]]              # dá as distâncias ao aeroporto mais recentemente inserido em 'res'
        m = []
        if (max(elem, key=elem.get) in res)==False:     # se o voo mais distante não já tiver em 'res' adiciona-mos-lo
            res += [max(elem, key=elem.get)]            # por alguma razão se apenas escrevesse-mos max(elem) haveria problemas
        else:
            while len(elem)>0:
                m += [max(elem, key=elem.get)]          # array dos aeroportos ordenados do mais distante para o mais próximo
                del elem[max(elem, key=elem.get)]       # temos de apagar o valor máximo, para não voltar a ser anexado na próxima itereção
            for i in m:
                if i not in res:        # percorremos 'm' até encontrar-mos um voo que não repita em 'res'
                    res += [i]
    return res


def viagem(inicio,voos):
    if not len(voos):   # verifica se o grafo não está vazio
        return []
    new = div(voos)     # formata o array 'voos'
    adj = build(new)    # constroí o grafo pesado
    dist = fw(adj)              # usamos o método Floyd-Warshall
    res = cal(dist,inicio,voos)     # calcula os voos mais distantes
    return res


```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)