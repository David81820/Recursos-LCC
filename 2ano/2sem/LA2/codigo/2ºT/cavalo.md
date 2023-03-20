```Python

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

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)