<h1 style="text-align: center;">LA2 | Treino 1 | ISBN</h1>

```Python

'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''

def isbn(livros):
    inv = []
    for t, c in livros.items():
        sum = 0
        for i in range(0,13):
            sum += int(c[i])*(3,1)[i%2==0] # (False = 3, True = 1)[condition == T]
        if sum % 10 != 0:
            inv.append(t)
    inv.sort()
    return inv

```


<br>


## Testes

```Python
# 1
livros = {
            "Todos os nomes":"9789720047572",
            "Ensaio sobre a cegueira":"9789896604011",
            "Memorial do convento":"9789720046711",
            "Os cus de Judas":"9789722036757"
        }
> Resultado = ["Memorial do convento","Todos os nomes"]

# 2
livros = {
            "Ola mundo":"0000000000001"
        }
> Resultado = ["Ola mundo"]
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)