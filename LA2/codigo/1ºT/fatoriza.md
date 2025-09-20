<h1 style="text-align: center;">LA2 | Treino 1 | Fatoriza</h1>

```Python

'''
Defina uma função que recebe um número positivo
e produz a soma dos seus factores primos distintos.
'''

def factoriza(n):
    soma = 0
    for i in range(2,n+1//2):
        if n == 1:
            break
        if n % i == 0:
            soma += i
            while(n%i == 0):
                n /= i
    return soma

```


<br>


## Testes

```Python
# 1
n = 6
> Resultado = 5

# 2
n = 28
> Resultado = 9
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)