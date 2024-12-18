<h1 style="text-align: center;">LA2 | Treino 1 | Futebol</h1>

```Python

'''
Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.
'''

def tabela(jogos):
    ponts = {}
    for e1,g1,e2,g2 in jogos:
        if e1 not in ponts.keys():
            ponts[e1] = [0,0,0]
        if e2 not in ponts.keys():
            ponts[e2] = [0,0,0]
        if g1 == g2:
            ponts[e1][0] += 1
            ponts[e2][0] += 1
        elif g1>g2:
            ponts[e1][0] += 3
        else:
            ponts[e2][0] += 3
        ponts[e1][1] += g1
        ponts[e1][2] += g2
        ponts[e2][1] += g2
        ponts[e2][2] += g1
        
    result = [(x,y[0]) for x,y in sorted(ponts.items(), key = lambda x: (-x[1][0], -(x[1][1]-x[1][2]), x[0]))]
    return result

```


<br>


## Testes

```Python
# 1
jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",4,"Benfica",1),("Sporting",2,"Porto",2)]
> Resultado = [('Porto', 4), ('Benfica', 4), ('Sporting', 2)]

# 2
jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",2,"Benfica",1),("Sporting",2,"Porto",2)]
> Resultado = [('Benfica', 4), ('Porto', 4), ('Sporting', 2)]
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)