<h1 style="text-align: center;">LA2 | Treino 1 | Apelidos</h1>

```Python

'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''

def apelidos(nomes):
    nomes.sort(key = lambda x: (len(x.split()), x) )
    return nomes

```


<br>


## Testes

```Python
# 1
apelidos = ['Jose Carlos Bacelar Almeida', 'Maria Joao Frade', 'Jose Bernardo Barros', 'Jorge Manuel Matos Sousa Pinto', 'Manuel Alcino Pereira Cunha', 'Xico Esperto']
> Resultado = ['Xico Esperto', 'Jose Bernardo Barros', 'Maria Joao Frade', 'Jose Carlos Bacelar Almeida', 'Manuel Alcino Pereira Cunha', 'Jorge Manuel Matos Sousa Pinto']

# 2
apelidos = ['Pedro Silva','Pedro Pereira']
> Resultado = ['Pedro Pereira','Pedro Silva']
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)