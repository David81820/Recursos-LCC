# Tipos, variáveis e operadores

## Tipos

C tem vários tipos de dados simples. Estes são chamados tipo de dados primitivos. Outros tipos de dados mais complexos podem ser construídos a partir destes.

1. `char` um caracter ASCII;
2. `int` inteiro;
3. `float` um número real;
4. `double` um número real mais preciso (maior parte decimal);

Estes são os tipos mais comuns em C, mas ainda temos algums 'derivados' deles:
1. `long double` um número real ainda mais preciso (implementação obscura, recomendado não usar);
2. `short int` um inteiro mais pequeno;
3. `long int`  um inteiro maior;
4. `unsigned int` um inteiro sem ser negativo;

E onde é que estão os booleanos?

Em C booleanos propriamente ditos não existem.
<br>A prática mais comum é utilizar `0` como valor para `false` e `1` como `true`.

Podem também reparar que não foi discutido o tamanho de cada tipo. Na verdade o C apenas define um tamanho mínimo para cada tipo de dados.

<br>

## Variáveis

Variáveis são "caixas" que guardam valores.
<br>A declaração de uma variável, reserva e dá um nome a uma área na memória, que vai guardar um valor de um tipo específico.
<br>C é uma linguagem fortemente tipada. Isto é, cada variável tem um tipo declarado e bem definido.

A forma de declarar uma variável em C é:
```c
tipo nome;
```
Dando um exemplo mais concreto:
```c
int x = 7;
```
Foi alocada uma área na memória ligada à uma variável chamada `x`, que atualmente guarda um valor de `int` - especificamente o número 7.

**De notar que se não atribuir-mos qualquer valor a uma varíavel, `tipo id;`, o espaço de memória reservado nao é limpo**
<br>Ou seja, até atribuirmos um valor, `id` pode conter "lixo".

<br>

### Alguns detalhes

1. As variáveis em C são 'case sensitive';
2. As variáveis em C podem conter números e até começar com um `_` (contudo não é recomendável).
3. Podemos declarar variáveis do mesmo tipo seguidas:
```c
float x, y, z;
```
<br>

## Operadores

O operador para atribuir um valor a uma variável é o `=`.

Os operadores para comparar variáveis (ou variáveis e valores):
1. `==` Para igualdade;
2. `!=` Para desigualdade;
3. `>` Maior do que;
4. `>=` Maior ou igual do que;
5. `<` Menor do que;
6. `<=` Menor ou igual do que.

Operadores matemáticos
1. `+` Soma;
2. `-` Subtração;
3. `*` Multiplicação;
4. `/` Divisão;
5. `%` Resto da divisão.

Operadores lógicos
1. `!` Negação;
2. `||` Or;
3. `&&` And;

<br>

### Operadores que manipulam variáveis

Em vez de se fazer:
```c
int x = 5
// ...
x = x + 5;
```
Podemos simplesmente fazer:
```c
int x = 5
// ...
x += 5;
```
Isto funciona para todas as operações matemáticas.


Depois temos o `++` e `--`
```c
x++;
// é o equivalente a fazer:
x = x + 1;
```
Obviamente que `--` fará uma subtração por 1 valor.

Estes operadores têm a peculiaridade de poderem ser usado depois ou antes da variável, tendo efeitos diferents no seus valores:
```c
int x = 5;
int y = 3;

x = y++;
// x tem agora valor 3
// y tem agora valor 4
```
Contrariamente:
```c
int x = 5;
int y = 3;

x = ++y;
// x tem valor 4
// y tem valor 4
```

<br><br>

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/1ano)