# Anatomia de um programa

<br>

## Hello World

```c
#include <stdio.h>

// Comentário
/*
  Outra forma
  de fazer
  um
  comentário
  */

int main() {
    printf("Hello, World!\n");
    return 0;
}
```
Aqui temos o clássico programa HelloWorld escrito em C.

<br>

## Comentários

Qual a diferença entre comentários `//` e comentários `/* */` ?.
<br>Ora :
  * `// Comment` são comentários de apenas uma linha;
  * contrariamente comentários `/* Comment2.0 */` podem extender-se por várias linhas, enquanto não forem fechados.

<br>

## Includes

Várias funções em C já se encontrão definidas, para as utilizarmos temos apenas que as importar.

Em C isto é feito utilizando a diretiva, de pré-processamento - `#include` - seguida do ficheiro que contém a função pretendida entre  `<  >`.
<br>Os ficheiros `.h` são header files - ficheiros importados que contêm todas as assinaturas das nossas funções (aprofundado mais à frente).

Visto que pretendíamos escrever "Hello, World" no ecrã, temos que ter uma função que imprima o nosso texto no terminal (standard output).
<br>Essa função já existe em C e chama-se `printf`, mas para a utilizarmos temos que incluir (importar) o ficheiro que a define (tecnicamente é onde se encontra a sua assinatura).
<br>A função `printf` encontra-se no ficheiro `stdio.h` - Stdio é uma abreviatura para Standard Input Output.

Agora para saber quais funções usar, como as usar e onde as encontrar, a chata resposta é ler documentação referente ao C.

<br>

## Introdução às Funções

Uma função em C, é um conjunto de codigo que é executado quando a função é chamada.

Em particular, a função `main` tem a qualidade única de ser sempre executada quando corremos programas C e também ser é sempre a primeira.
<br>Ou seja, sempre que a função `main` é chamada, tudo o que está entre chavetas é executado.


### Assinatura de uma Função

A assinatura de uma função é o que a caracteriza, o caso da nossa `main` a sua assinatura é:
```c
int main()
/* equivalente a :
int main(null)
*/
```
Daqui podemos inferir que a função main devolve um `int` e não recebe argumentos.

De facto, todas funções seguem este esquema de assinatura:
```c
tipo nome(tipo1 argumento1, tipo2 argumento2, etc...);
```


### Corpo de uma função

O corpo de uma função, a sua implementação, é todo código escrito entre chavetas. É aqui definido o seu comportamento.

```c
int exemplo(){
    // tudo aqui inserido constituí o corpo da função - essencialmente a sua operação
}
```


### Como chamar uma função?

Simplesmente usando o seu nome e passando os argumentos necessários.

<br>

## Return
Esta operação de "devolver", dá o valor final de uma função.
<br>Como a nossa `main` é do tipo int, então terá que devolver um número inteiro.
