<h1 style="text-align: center;">LA2 | Treino 1 | Cruzamentos</h1>

```Python

'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que lista os cruzamentos de uma cidade 
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto 
maior o número de ruas que interliga.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos). 
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.
A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade, 
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo 
nível de criticidade deverão ser listados por ordem alfabética.
'''

def cruzamentos(ruas):
    cruz = {}
    for rua in ruas:
        if rua[0] not in cruz.keys():
            cruz[rua[0]] = 1
        else:
            cruz[rua[0]] += 1
        if rua[-1] not in cruz.keys():
            cruz[rua[-1]] = 1
        elif rua[0] != rua[-1]:
            cruz[rua[-1]] += 1
        
    result = list(cruz.items())
    result.sort(key = lambda x: (x[1], x[0]) )
    return result

```


<br>


## Testes

```Python
# 1
ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]
> Resultado = [('t',1),('a',2),('e',2),('l',2),('r',2),('c',3),('o',3),('s',6)]

# 2
ruas = ["ab","bc","bd","cd"]
> Resultado = [('a',1),('c',2),('d',2),('b',3)]
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)