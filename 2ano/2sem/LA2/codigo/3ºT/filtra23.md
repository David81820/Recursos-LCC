<h1 style="text-align: center;">LA2 | Torneio 3 (2022/2023) | Filtra</h1>

```Python

'''
Implemente a seguinte função que dada uma lista de strings filtra as strings
que podem ser obtidas intercalando os caracteres das strings a e b também dadas
como parâmetro. Uma string s intercala as strings a e b sse apenas contem 
caracteres de a e b e todos os caracters de a e b aparecem pela mesma 
ordem em s. Sugere-se que comece pode definir recursivamente uma função 
auxiliar que testa se uma string s intercala as strings a e b, e que depois
optimize essa função com as técnicas de memoization e programação dinâmica.
'''


def intercalado(s, a, b, dic={}):
    if len(s) == 0:
        return True
    if (s, a, b) in dic:
        return dic[(s, a, b)]

    res = False
    if len(a) > 0 and a[0] == s[0]:
        res = intercalado(s[1:], a[1:], b, dic)
    if not res and len(b) > 0 and b[0] == s[0]:
        res = intercalado(s[1:], a, b[1:], dic)

    dic[(s, a, b)] = res
    return res


def filtra(strings, a, b):
    filtrado = []
    for str in strings:
        if intercalado(str, a, b):
            filtrado.append(str)
    return filtrado



#==================================
#           TESTES

# 1
strings = ["ACDB","ABCD","ADCB"]
resultado = ["ACDB","ABCD"]

# 2
strings = ["ACDABC","ABCACD","AACCBC","AABCDC"]
resultado = ["ACDABC","ABCACD","AABCDC"]

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)