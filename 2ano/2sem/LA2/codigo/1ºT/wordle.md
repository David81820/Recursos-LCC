<h1 style="text-align: center;">LA2 | Torneio 1 (2022/2023) | Área</h1>

```Python

"""
Implemente uma função que dada uma palavra secreta e uma palavra tentativa
devolva uma lista com os caracteres da palavra tentativa que aparecem na
palavra secreta.
Mais concretamente, para cada caracter que apareça na palavra tentativa
deve também ser indicada a respectiva posição e um booleano que indica se
aparece na mesma posição na palavra secreta ou numa posição diferente.
"""


def wordle(secreta, tentativa):
    res = []
    usados = set()

    for i in range(len(tentativa)):
        char = tentativa[i]

        if char in secreta:
            secretIndex = secreta.find(char)

            if secretIndex == i:
                res.append((char, i, True))
            elif secretIndex not in usados:
                res.append((char, i, False))

            usados.add(secretIndex)

    return res

```


<br>


## Testes

```Python
# 1
secreta = "programa"
tentativa = "logica"
> Resultado = [('o',1,False),('g',2,False),('a',5,True)]

# 2
secreta = "logica"
tentativa = "programa"
> Resultado = [('o',2,False),('g',3,False),('a',5,True)]
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)