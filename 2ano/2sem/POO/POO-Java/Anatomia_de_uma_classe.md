# Anatomia de uma classe

Notas:
 * Código entre [ ] é opcional. Ou seja, fica ao teu critério se é necessário.
 * As palavras 'MyClass', 'XClass', 'SuperClass' e 'InterfaceClass' são apenas exemplificativas.

<br>

### Declaração

Nesta declaração indicamos o nome da nossa class, se estende uma classe e se, e quais, interfaces implementa.
```java
public class MyClass [extends SuperClass] [implements InterfaceClass, ...] {
```

<br>

### Variáveis de instância
Estas devem ser sempre `private` para garantir o encapsulamento do estado
interno do objeto.
```java
    private int num;
    private String nome;
    private XClass outraCena;
    private ArrayList<String> nomes;
    private ArrayList<XClass> outrasCenas;
```

<br>

### Construtores
Os contrutores permitem instanciar novos objetos da classe. Devem inicializar todos as variáveis de instância.
<br>

#### Construtor vazio
Este construtor inicializa as variáveis de instância com valores pré-definidos.
```java
    public MyClass(){
        this.num = 0;
        this.nome = "";
        this.outraCena = new XClass();
        this.nomes = new ArrayList<>();
        this.outrasCenas = new ArrayList<>();
    }
```
<br>

#### Construtor parametrizado
Este construtor recebe como parâmetro os valores que as variáveis de instância
 devem tomar.

*(Nota: Uma classe pode ter mais variáveis de instância do que os parâmetros
 passados neste tipo de construtor, caso, por exemplo, uma destas tenha um
 valor derivado de outras variáveis.)*

As diferentes atribuições feitas neste construtor são explicadas através dos
 getters/setters mais à frente.
```java
    public MyClass(int num, String nome, XClass outraCena,
                    ArrayList<String> nomes, ArrayList<XClass> outrasCenas){
        this.num = num;
        this.nome = nome;
        this.outraCena = outraCena.clone();
        this.nomes = new ArrayList<>(nomes);
        this.outrasCenas = new ArrayList<>();
        for(XClass cena: outrasCenas){
            this.outrasCenas.add(cena.clone());
        }
    }
```
<br>

#### Construtor de cópia
Este construtor permite criar uma cópia exata de outra instância deste objeto.

*(Nota: Este construtor assume que todos os getters clonam corretamente as
 variáveis de instância que retornam.)*
```java
    public MyClass(MyClass myClass){
        this.num = myClass.getNum();
        this.nome = myClass.getNome();
        this.outraCena = myClass.getOutraCena();
        this.nomes = myClass.getNomes();
        this.outrasCenas = myClass.getOutrasCenas();
    }
```

<br>

### Getters
Os getters permitem aceder às variáveis de instância de uma instância da nossa
 classe. Devem ser `public` apenas os que queremos que seja possível aceder.
<br>

#### Get de uma variável de tipo primitivo
As variáveis são 'passed by value', ou seja, o seu valor é copiado. Logo, este get é simples.

(Irá ficar mais claro mais a frente.)
```java
    public int getNum(){
        return this.num;
    }
```
<br>

#### Get de um objeto imutável
Uma string é imutável, logo retornar um apontador para este objeto que pertence ao estado interno
no nosso objeto não tem problema.
```java
    public String getNome(){
        return this.nome;
    }
```
<br>

#### Get de um objeto mutável
Um objeto mutável deve ser clonado para manter o encapsulamento. Se este objeto fosse alterado
fora da instância que o retornou, implicaria alterar o estado interno da mesma instância.

(Porque a variável é 'passed by value' e esta, na verdade, é um apontador.)
```java
    public XClass getOutraCena(){
        return this.outraCena.clone();
    }
```
<br>

#### Get de uma lista de objetos imutáveis
Tem que se criar uma lista nova. Apesar de cada objeto individual da lista ser imutável, a lista
em si, não é imutável. Logo, se retornarmos a lista diretamente, novos valores podem ser adicionados
à mesma, alterando o estado interno da instância a partir do exterior.

Para isto, podemos fazer uso do construtor da `ArrayList` que recebe uma `Collection` e copia os valores.

**_ATENÇÃO: SÓ PODEMOS USAR ESTE construtor PARA LISTAS DE objetos IMUTÁVEIS_**
```java
    public ArrayList<String> getNomes(){
        return new ArrayList<>(this.nomes);
    }
```
Ou
```java
    public ArrayList<String> getNomes(){
        return this.nomes.clone();
    }
```
<br>

#### Get de uma lista de objetos mutáveis
Como no get anterior, tem que ser criada uma nova lista. Mas, os elementos ao serem adicionados à mesma,
têm que ser clonados.
```java
    public ArrayList<XClass> getOutrasCenas(){
        ArrayList<XClass> newOCenas = new ArrayList<>();
        for(XClass cena: this.outrasCenas){
            newOCenas.add(cena.clone());
        }
        return newOCenas;
    }
```

<br>

### Setters
Os setters seguem o mesmo princípio dos getters. Objetos imutáveis e tipos primitivos
não têm que ser clonados, tudo o resto sim.
```java
    public void setNum(int num){
        this.num = num;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public void setOutraCena(XClass outraCena){
        this.outraCena = outraCena.clone();
    }

    public void setNomes(ArrayList<String> nomes){
        this.nomes = new ArrayList<>(nomes);
    }

/*  OU assim
    public void setNomes(ArrayList<String> nomes){
        this.nomes = nomes.clone();
    }
*/

    public void setOutrasCenas(ArrayList<XClass> cenas){
        ArrayList<XClass> newCenas = new ArrayList<>();
        for(XClass cena: cenas){
            newCenas.add(cena.clone());
        }
        this.outrasCenas = newCenas;
    }
```
*Nota: Setters de uma lista nem sempre fazem sentido. Dependendo do contexto, pode fazer mais
sentido implementar métodos que adicionem ou removam elementos às listas.*

<br>

### Métodos "obrigatórios" de definir.
Estes métodos devem ser definidos para todas as classes que sejam criadas. Salvo exceções em que
sejam inúteis.
<br>

#### equals
O equals é o mais importante, e raramente é inútil.
```java
    public boolean equals(Object o){
/*[1]*/ if(this == o) return true;

/*[2]*/ if(o == null || this.getClass() != o.getClass())
            return false;

/*[3]*/ MyClass that = (MyClass) o;
/*[4]*/ return this.num == that.getNum()
            && this.nome.equals(that.getNome())
            && this.outraCena.equals(that.getOutraCena())
            && this.nomes.equals(that.getNomes())
            && this.outrasCenas.equals(that.getOutrasCenas());
    }
```
Análise do código:
 1. Compara-se os apontadores. Se forem iguais, sabemos que o objeto é o mesmo.
 2. Verifica-se se o objeto é null ou se as classes entre eles são diferentes. Qualquer uma destas
    indica que não são iguais.
 3. Faz-se o cast para se poder chamar métodos.
 4. Verifica-se se todos os elementos da classe são iguais.
    * Para tipos primitivos podemos comparar normalmente com `==`.
    * Para classes chamamos o `equals` das mesmas.
<br><br>

#### toString
O toString é importante para efeitos de debug. Pode também ser adaptado para aplicações de terminal.
```java
    public String toString(){
        StringBuffer sb = new StringBuffer("MyClass: ");
        sb.append("Num: ").append(this.num).append(", ");
        sb.append("Nome: ").append(this.nome).append(", ");
        sb.append("Outra Cena: ").append(this.outraCena).append(", ");
        sb.append("Nomes: ").append(this.nomes).append(", ");
        sb.append("Outras Cenas: ").append(this.outrasCenas).append(", ");
        return sb.toString();
    }
```
<br>

#### Clone
O clone deve ser implementado porque o Nestor diz que sim. Objetos imutáveis não devem
 implementar este método.
```java
    public MyClass clone(){
        return new MyClass(this);
    }
```

<br><br>

Lista dos principais objetos imutáveis disponíveis:
 * Integer
 * Float
 * Double
 * Char
 * Boolean
 * String
 * LocalDate
 * LocalTime
 * LocalDateTime
(existem mais)

<br><br>

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/POO/POO-Java)
