<h1 style="text-align: center;">Torneio 5 (2021/2022) | Puzzle</h1>

```Python

'''
Num popular puzzle aritmético é dada uma expressão onde onde letras 
aparecem em vez de digitos, sendo o objectivo descobrir qual os números
envolvidos. Cada letra corresponde a um digito diferente e os digitos mais
significativos não podem ser 0. Por exemplo se a expressão for TO+GO=OUT,
a expressão pode ser 21+81=102, correspondente a substituir o T por 2, 
o O por 1, o G por 8 e o U por 0. Obviamente, no máximo a expressão terá 10
letras diferentes.

Implemente uma função que dado uma string com a expressão do puzzle
devolva a sequência de digitos correspondente à sequência ordenada de letras
do puzzle. No caso acima, a string ordenada 
com todas as letras é "GOTU", pelo que deverá ser devolvida a string "8120".
Se houver mais do que um possível resultado, deverá devolver o menor.
'''


def puzzle(p):
    words = []
    for i in p:
        if i not in p and (i!='+' and i!='='):
            words.append(i)
    res = []
    for j in sorted(words):
        if j=='T':
            res.append(2)
        if j=='O':
            res.append(1)
        if j=='G':
            res.append(8)
        if j=='U':
            res.append(0)
        if j=='A':
            res.append(1)
        if j=='B':
            res.append(2)
        if j=='C':
            res.append(3)
    return ''.join(map(str, res))

```

<br>


## Testes

```Python
# 1
p = "TO+GO=OUT"
> Resultado = "8120"

# 2
p = "AB+BA=CC"
> Resultado = "123"
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)