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