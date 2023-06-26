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


################################
# Grafos - 90%
################################

def calculadora(ops,res):
    queue = [(0,0)] #res, operaçoes
    vis = [0]

    for r, op in queue:
        if r == res:
            return op

        for string in ops:
            if string[0].isdigit():
                novoNum = int(str(r) + string)
                if novoNum not in vis:
                    queue.append((novoNum, op+1))
                    vis.append(novoNum)
                continue
                
            operacao = string[0]
            num = int(string[1:])

            if operacao == '+':
                novoNum = r+num
            elif operacao == '-' and r > 0:
                novoNum = r-num
            elif operacao == '*' and r > 0:
                novoNum = r*num
            elif operacao == '/':
                novoNum = r//num

            if novoNum == res:
                return op+1

            if novoNum not in vis:
                queue.append((novoNum, op+1))
                vis.append(novoNum)

    return 0



################################
# Brute Force - 100%
################################

def search(ops, res, k, n, i):
    if k == i:
        return res == n
        
    for what in ops:
        cI = n
        if '+' in what:
            what = what.split('+')
            cI += int(what[1])
        elif '-' in what:
            what = what.split('-')
            cI -= int(what[1])
        elif '/' in what:
            what = what.split('/')
            cI //= int(what[1])
        elif '*' in what:
            what = what.split('*')
            cI *= int(what[1])
        else:
            cI = int(str(cI) + str(what))
        if search(ops, res, k, cI, i+1):
            return True

    return False


def calculadora(ops,res):
    print(ops, res)
    k = 0
    while True:
        if search(ops,res,k, 0, 0):
            return k
        k+=1
    return -1

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
