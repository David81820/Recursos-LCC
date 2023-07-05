<h1 style="text-align: center;">LA2 | Treino 3 | Espaça</h1>

```Python

"""
Implemente uma função que, dada uma frase cujos espaços foram retirados, 
tenta recuperar a dita frase. Para além da frase (sem espaços nem pontuação), 
a função recebe uma lista de palavras válidas a considerar na reconstrução 
da dita frase. Deverá devolver a maior frase que pode construir inserindo
espaços na string de entrada e usando apenas as palavras que foram indicadas 
como válidas. Por maior entende-se a que recupera o maior prefixo da string
de entrada. Só serão usados testes em que a maior frase é única.
"""

#######################################
#  Resolução 1 - 80%
#######################################

def espaca(frase,palavras):
    res = ""
    dic = {}
    for i in range(len(frase)+1):
        for j in range(0,i):
            if frase[j:i] in palavras:
                if j in dic:
                    dic[i] = dic[j] + " " + frase[j:i]
                else:
                    dic[i] = frase[j:i]
                break
    if dic:
        res = dic[len(frase)]
    return res


#######################################
#  Resolução 2 - 100%
#######################################

def espaca(frase,palavras):
    dic = {0:[]}
    mx = 0
    for i in range(1, len(frase)+1):
        for palavra in palavras:
            n = len(palavra)
            if i-n in dic and frase[i-n:].startswith(palavra):
                dic[i] = dic[i-n].copy()
                dic[i].append(palavra)
                mx = i
    return ' '.join(dic[mx])

```


<br>


## Testes

```Python
# 1
frase = "estecursoeomaior"
palavras = ["e","o","so","maior","este","curso","urso","es","maio"]
> Resultado = "este curso e o maior"

# 2
frase = "ogatomiaeavacamuge"
palavras = ["o","oga","ga","gato","gatom","mia","eava","ava","e","a","va","vaca","mu","muge"]
> Resultado = "o gato mia e a vaca muge"
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)