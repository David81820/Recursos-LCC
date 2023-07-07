<h1 style="text-align: center;">LA2 | Torneio 3 (2021/2022) | Jogo</h1>

```Python

'''
Suponha que tem um baralho de cartas onde cada carta tem duas palavras, uma
escrita na parte de cima da carta, outra na parte de baixo. Assuma que tem
um stock infinito de cada carta. Implemente uma função que dado um baralho,
descrito como uma lista de pares de strings, determine a menor sequência de 
cartas tal que, quando colocadas lado a lado, a frase na parte de cima seja
igual à frase na parte de baixo. A sequência de cartas deve ser identificada
pelas respectivas posições no baralho. Caso haja mais do que uma sequência
óptima deve devolver a menor em ordem lexicográfica (ou seja, dando preferência
às cartas que aparecem primeiro).

Por exemplo se o baralho tiver as cartas

a    ab   bba
---  ---  ---
baa  aa   bb

a melhor solução seria

bba  ab   bba  a
---  ---  ---  ---
bb   aa   bb   baa

correspondente à frase bbaabbbaa. 

Este baralho ser´á representado pela lista [('a','baa'),('ab','aa'),('bba','bb')]
e a solução pela lista das posições das cartas no baralho, ou seja, [3,2,3,1].
'''


def jogo(cartas):

```


<br>


## Testes

```Python
# 1
cartas = [('a','baa'),('ab','aa'),('bba','bb')]
> Resultado = [3, 2, 3, 1]

# 2
cartas = [('c','bc'),('bb','b'),('ab','ba')]
> Resultado = [2, 1]
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)