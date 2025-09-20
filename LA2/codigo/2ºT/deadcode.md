<h1 style="text-align: center;">LA2 | Torneio 2 (2020/2021) | Deadcode</h1>

```Python

"""
Neste problema pretende-se que desenvolva uma função para detectar código
morto num programa. Código morto são instruções que nunca poderão ser
executadas num programa e que, como tal, poderiam ser eliminadas.
A linguagem de programação a analisar é muito simples. Um programa é uma
sequência de comandos, e apenas existem dois tipos de comandos: "print" que
dado um número imprime esse número e "jump" que dada uma sequência de 
localizações do programa separadas por vírgulas salta para uma dessas 
localizações à sorte. Uma localização é simplesmente o indíce de um comando
na sequência. A execução de um programa termina quando se executa a última
instrução (se for um "print") ou se salta para uma localização inexistente.
A função deve devolver um tuplo com o número de instruções que podem ser
executadas e o número de instruções que nunca poder~ão ser executadas.
"""


def deadcode(prog):
    
    iJump = []
    cEx = [0]
    
    x = 0
    
    for i in prog:
        inst = i.split(" ")
        if inst[0] == "print":
            x += 1
        else:
            iJump.append(inst[1])
            cEx.append(x)
            x += 1
    
    for index in iJump:
        iSplit = index.split(",")
        cEx.append(int(iSplit[0]))
        cEx.append(int(iSplit[1]))
    
    cEx.sort()
    cEx = list(set(cEx))
    cEx.pop()
    cMo = len(prog)-len(cEx)
    
    return (len(cEx),cMo)

```


<br>


## Testes

```Python
# 1
prog = ["print 0","jump 0,2","print 1","jump 2,4"]
> Resultado = (4,0)

# 2
prog = ["print 0","jump 0,3","print 2","print 1","jump 3,5"]
> Resultado = (4,1)
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)