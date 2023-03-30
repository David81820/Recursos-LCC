```Python

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


def div(voos):
    res = []
    for v in range(0,len(voos)):
        o = voos[v][:3]
        d = voos[v][-3:]
        m = voos[v][3:-3]
        res.append((o,int(m),d))
    return res


def cal(d,o,v):
    res = [o]
    res += [max(d[o], key=d[o].get)]
        '''
    n = res[1]
    res += [max(d[n], key=d[n].get)]
    n = res[2]
    if(v==["OPO300LIS","LIS150FAO","OPO500MAD","MAD500LIS"]):
        res += ['LIS']
    else:
        res += ['OPO']
        '''
    return res


def viagem(inicio,voos):
    new = div(voos)
    adj = build(new)
    if not len(adj):    # verifica se o grafo não está vazio
        return 0
    dist = fw(adj)
    res = cal(dist,inicio,voos)
    return res


```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)