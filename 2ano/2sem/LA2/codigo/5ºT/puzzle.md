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


############################
# Resolução mais completa
############################

def complete(ipt, dic):
    for number in dic.values():
        if number == -1:
            return False
    return True

def extensions(ipt, dic):
    nextLetter = [x for x in sorted(dic.keys()) if dic[x] == -1][0]
    return [(nextLetter, str(x)) for x in range(10) if str(x) not in dic.values()]

def valid(ipt, dic):
    numbers = []
    res = -1
    string = ""
    for pos, c in enumerate(ipt):
        if c == "+":
            numbers.append(int(string))
            string = ""
        elif c == "=":
            numbers.append(int(string))
            res = int("".join(map(lambda x: dic[x],ipt[pos+1:])))
            break
        else:
            string += dic[c]
            
    return sum(numbers) == res

def aux(ipt, dic):
    if complete(ipt, dic):
        return valid(ipt, dic)
    for i,x in extensions(ipt, dic):
        dic[i] = x
        if aux(ipt, dic):
            return True
        dic[i] = -1
    
    return False

def puzzle(p):
    dic = {}
    for c in p:
        if c not in ["+", "="]:
            dic[c] = -1
    res = aux(p, dic)
    print(dic.items())
    return "".join(map(lambda x: dic[x], sorted(dic.keys())))


###################################
# Resolução Alternativa
###################################

# testa se o candidato c está completo
def complete(p,c,ind,puz):
    print(ind)
    return ind == len(p)
# enumera as extensões válidas para o candidato parcial c
def extensions(p,c,ind,puz):
    r = []
    ex = p[ind]
    print(ex)
    if c[ex] == -2:
        r = [x for x in range(1,10) if x not in c.values()]
    elif c[ex] == -1:
        r = [x for x in range(0,10) if x not in c.values()]
    print(r)
    return r
# testa se um candidato c é uma solução válida para p
def valid(p,c,puz):
    string = ""
    for letra in puz:
        if letra in c:
            string+=str(c[letra])
        elif letra == '=':
            string+=letra
            string+=letra
        else:
            string+=letra
    return eval(string)
            
def aux(p,c,puz,ind):
    if complete(p,c,ind,puz):
        return valid(p,c,puz)
    for x in extensions(p,c,ind,puz):
        tmp = c[p[ind]]
        c[p[ind]] = x
        if aux(p,c,puz,ind+1):
            return True
        c[p[ind]] = tmp
    return False

def puzzle(p):
    d = dict()
    for i in range(0,len(p)):
        if (p[i] >= 'A' and p[i] <= 'Z') and p[i] not in d:
            d[p[i]] = -1
        if p[i] in d and (i == 0 or p[i-1] not in d):
            d[p[i]] = -2
    s = ""
    print(d)
    if aux(sorted(d.keys()),d,p,0):
        for x in (sorted(d.keys())):
            s += str(d[x])
    return s

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