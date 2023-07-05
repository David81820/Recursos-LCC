<h1 style="text-align: center;">LA2 | Torneio 4 (2022/2023) | Bits</h1>

```Python

'''
Implemente uma função que determine em quantas sequências de n bits
um bit a 1 apenas aparece em sequências de pelo menos k 1s seguidos. 
Por exemplo se n = 3 e k = 2 então temos 4 sequências válidas, 
nomeadamente 000, 110, 011 e 111. Se n = 4 e k = 3 temos também 4 
sequências válidas, nomeadamente 0000, 1110, 0111 e 1111. Se n = 4 e 
k = 2 então já temos 7 sequências válidas: para além das 4 anteriores 
temos 1100, 0110 e 0011.
'''


def bits(n,k):
    result = 0
    for i in range(2**n):
        txt = "{0:b}".format(i)
        for q in txt.split('0'):
            if (0<len(q) & len(q)<k):
                break
        else:
            result+=1
    return result



################################################
#   Resolução sem usar pesquisa exaustiva
################################################

def choose(n,k):
    if n<k:
        return 0
    else:
        numerator, denominator, k=1, 1, min(k, n-k)
        for i in range(k):
            numerator *= n-i
            denominator *= i+1
        return numerator // denominator


def bits(n,k):
    output = 1
    for ones in range(k, n+1):
        zeros = n - ones
        for runs in range(1, ones):     # ones = k+1
            a = choose( zeros-(runs-1)+(runs+1)-1 , runs+1-1 )
            b = choose( ones-(runs*k)+(runs)-1 , runs-1 )
            output += a * b
    return output

```


<br>


## Testes

```Python
# 1
n = 8
k = 2
> Resultado = 65

# 2
n = 5
k = 3
> Resultado = 7
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)