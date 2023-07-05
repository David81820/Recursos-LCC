<h1 style="text-align: center;">LA2 | Treino 3 | Ladrão</h1>

```Python

"""
Um ladrão assalta uma casa e, dado que tem uma capacidade de carga limitada, 
tem que decidir que objectos vai levar por forma a maximizar o potencial lucro. 

Implemente uma função que ajude o ladrão a decidir o que levar.
A função recebe a capacidade de carga do ladrão (em Kg) seguida de uma lista 
dos objectos existentes na casa, sendo cada um um triplo com o nome, o valor de 
venda no mercado negro, e o seu peso. Deve devolver o máximo lucro que o ladrão
poderá  obter para a capacidade de carga especificada.
"""


#######################################
#  Resolução 1 - 80%
#######################################

def sack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    
    if (wt[n-1] > W):
        return sack(W, wt[:n-1], val[:n-1], n-1)
    else:
        return max(val[n-1] + sack(W-wt[n-1], wt[:n-1], val[:n-1], n-1), sack(W, wt[:n-1], val[:n-1], n-1))


def ladrao(lim,obj):
    n = len(obj)
    v = []
    w = []
    for o in obj:
        v.append(o[1])
        w.append(o[2])
    res = sack(lim, w, v, n)
    return res



#######################################
#  Resolução 2 - 100%
#######################################

def ladrao(capacidade,objectos):
    dic = {}
    dic[0] = 0
    possiveis = {}
    possiveis[0] = objectos.copy()
    for i in range (1,capacidade+1):
        r = 0
        sobram = objectos.copy()
        for obj in objectos:
            if obj[2] <=i and obj in possiveis[i-obj[2]]:
                a = dic[i-obj[2]] + obj[1]
                if a > r:
                    r = a
                    sobram = possiveis[i-obj[2]].copy()
                    sobram.remove(obj)
        dic[i] = r
        possiveis[i] = sobram
            
    
    return max(dic.items(), key=lambda x: x[1])[1]

```


<br>


## Testes

```Python
# 1
soma = 10
objectos = [("microondas",30,6),("jarra",14,3),("giradiscos",16,4),("radio",9,2)]
> Resultado = [[8,1,7,3,3,6,3,5],[1,1,1,2,3,1,2]]

# 2
soma = 10
objectos = [('A',10,1),('B',20,1),('C',30,1),('D',40,1),('E',50,1),('F',60,1),('G',70,1),('H',80,1),('I',90,1),('J',100,1)]
> Resultado = 550
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)