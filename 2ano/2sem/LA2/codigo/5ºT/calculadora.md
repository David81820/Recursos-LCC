<h1 style="text-align: center;">Torneio Extra 2020/2021</h1>

```Python

"""
Dada uma calculadora que apenas tem disponível um conjunto fixo de operações e 
cujo valor inicial é zero, implemente uma função que determina qual o número 
mínimo de operações necessárias para atingir um determinado resultado. 
Assuma que tal é sempre possível. 
As operações disponíveis são representadas por uma sequência de strings, 
onde cada string pode ser um dos caracteres '+', '-', '*' ou '/' 
seguido de um número inteiro positivo (o segundo operando) 
ou um único digito, que representa a operação de acrescentar um digito ao 
número actualmente na calculadora. 
Por exemplo, a string "/3" representa a operação de divisão inteira por 3 e 
a string "4" a operação de acrescentar o digito 4 ao número actualmente 
na calculadora (por exemplo, se o número actual é 3 ficará com o número 34).
"""

def calculadora(ops, res):

```


<br>


## Testes

```Python
# 1
ops = ["+1","+2","*3"]
res = 9
> Resultado = 3

# 2
ops = ["+6","-2","*4"]
res = 64
> Resultado = 4
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)
