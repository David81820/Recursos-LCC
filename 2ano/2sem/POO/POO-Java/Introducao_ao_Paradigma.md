# Introdução ao Paradigma

Um objeto é apenas a junção de dados e comportamento numa unidade lógica.

Ou seja, se tivermos um carro poderíamos representá-lo da seguinte forma:

```c
struct Car {
    String brand;
    String model;
    int kmsTotal;
    int kmsParcial;
}
```

Depois podemos querer definir que o carro pode "andar" e aumentar o número de
kms que tem, ou reiniciar a quilometragem parcial. Para isto podemos definir
funções como:

```c
void andar(Car* car, int km) {
    car->kmsTotal += km;
    car->kmsParcial += km;
}

void resetParcial(Car* car) {
    car->kmsParcial = 0;
}


// Example Main
int main() {
    Car car = /* inicialização */
    andar(&car, 10);
    resetParcial(car);
}
```

Este padrão de funções que recebem a estrutura para fazer alterações sobre o
mesmo é muito comum. Este tipos de funções são o que chamamos de comportamento
e no paradigma orientado a objetos são definidas juntas com a estrutura em si.
Em Java usamos classes para criar esta relação e estas funções chamam-se **métodos**.

Logo em Java definiríamos esta `Class` da seguinte forma.

```java
public class Car {
    private String brand;
    private String model;
    private int kmsTotal;
    private int kmsParcial;

    public void andar(int km) {
        this.kmsTotal += km;
        this.kmsParcial += km;
    }

    public void resetParcial(int km) {
        this.kmsParcial = 0;
    }
}

// Example Main
public class Main {
    public static void main(String args[]){
        Car car = new Car();
        car.andar(10);
        car.resetParcial();
    }
}
```

Aqui podemos ver que a keyword `this` substitui a referencia da estrutura que
temos sempre de ter em programação imperativa.

<br>

## Nota

Em Java todos os objectos são pointers, (excepto os tipos primitivos, `int`,
`long`, `float`, `double`, `byte`, etc), logo onde no código em `C` tem de se
explicitamente passar um pointer para as funções, em Java isto é implícito,
fazendo o `'.'` em Java equivalente ao `'->'` em `C`.

<br><br>

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/POO/POO-Java)
