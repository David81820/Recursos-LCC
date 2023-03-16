### Exercício 1

<details>
  <summary>ex1</summary>

<pre><code lang="java">package exercicios;

public class ex1 {
    public int minimo(int[] array) {
        int min = Integer.MAX_VALUE;
        for(int elem: array) {
            if (elem < min) min = elem;
        }
        return min;
    }

    public int[] entreIndices(int[] array, int a, int b) {
        if (a > b || a < 0 || b > array.length) {
            return null;
        }
        int[] resultado = new int[b-a+1];
        System.arraycopy(array, a, resultado, 0, b - a + 1);
        return resultado;
    }

    public int[] comuns(int[] a, int[] b) {
        int[] res = new int[a.length];
        int count = 0;

        for (int elem: a) {
            boolean enc = this.existe(res, count, elem);
            for (int i = 0; i < b.length && !enc; i++) {
                if (enc = (elem == b[i])) {
                    res[count++] = elem;
                }
            }
        }
        int[] resultadoFinal = new int[count];
        System.arraycopy(res,0,resultadoFinal,0,count);

        return resultadoFinal;
    }

    private boolean existe(int[] array, int n, int elem) {
        boolean res = false;

        for(int i = 0; i < n && !res; i++) res = array[i] == elem;

        return res;
    }
}
</code></pre>
</details>


<details>
  <summary>TestaEx1</summary>

<pre><code lang="java">package exercicios;
import java.util.Arrays;
import java.util.Scanner;

public class TestaEx1 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ex1 teste = new ex1();

        /*
        // Alinea a
        System.out.print("Numero de elementos: ");
        int n = scan.nextInt();
        int[] array = new int[n];
        for (int i = 0; i < n; i++) array[i] = scan.nextInt();
        int min = teste.minimo(array);
        System.out.println("Minimo = " + min);
        // Fim Alinea a
        // Alinea b (com o array anterior)
        int a,b;
        a = scan.nextInt();
        b = scan.nextInt();
        int[] newArray = teste.entreIndices(array, a, b);
        System.out.println(Arrays.toString(newArray));
        // Fim Alinea b
        */

        // Alinea c
        System.out.print("Numero de elementos: ");
        int n = scan.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = scan.nextInt();

        System.out.print("Numero de elementos: ");
        n = scan.nextInt();
        int[] b = new int[n];
        for (int i = 0; i < n; i++) b[i] = scan.nextInt();

        System.out.println(Arrays.toString(teste.comuns(a, b)));
        // Fim Alinea c



    }
}
</code></pre>
</details>

<br>

### Exercício 2

<details>
  <summary>ex1</summary>

<pre><code lang="java">package exercicios;

public class ex2 {
    private int[][] notasTurma;

    public ex2() {
        this.notasTurma = new int[5][5];
    }

    public void atualizaPauta(int[][] notas) {
        for (int i = 0; i < 5; i++) {
            System.arraycopy(notas[i],0,this.notasTurma[i],0,5);
        }
    }

    public int somaNotasUC(int uc) {
        int soma = 0;
        for (int i = 0; i < 5; i++) soma += this.notasTurma[i][uc];
        return soma;
    }

    public int[][] getPauta() {
        int[][] res = new int[5][5];
        for (int i = 0; i < 5; i++) {
            System.arraycopy(this.notasTurma[i],0,res[i],0,5);
        }
        return res;
    }

    public double mediaAluno(int aluno) {
        int soma = 0;

        for (int i = 0; i < 5; i++)
            soma += this.notasTurma[aluno][i];

        return soma/5.0;
    }

    public double mediaUC(int uc) {
        int soma = 0;

        for (int i = 0; i < 5; i++)
            soma += this.notasTurma[i][uc];

        return soma/5.0;
    }

    public int notaMaisAlta() {
        int maisAlta = Integer.MIN_VALUE;

        for (int[] aluno: this.notasTurma)
            for (int nota: aluno)
                if (nota > maisAlta) maisAlta = nota;

        return maisAlta;
    }

    public int notaMaisBaixa() {
        int maisBaixa = Integer.MAX_VALUE;

        for (int[] aluno: this.notasTurma)
            for (int nota: aluno)
                if (nota < maisBaixa) maisBaixa = nota;

        return maisBaixa;
    }

    public int[] notasAcimaDeX(int x) {
        int[] notas = new int[25];
        int i = 0;

        for (int[] aluno: this.notasTurma)
            for (int nota: aluno)
                if (nota > x) notas[i++] = nota;

        int[] resultado = new int[i];
        System.arraycopy(notas,0,resultado,0,i);

        return resultado;
    }

    public String notas() {
        String notas = "Notas dos Alunos: \n";

        for (int i = 0; i < 5; i++) {
            notas = notas.concat("Aluno " + i + ":\n");
            for (int j = 0; j < 5; j++) {
                notas = notas.concat("UC " + j + ": " + this.notasTurma[i][j] + "\n");
            }
        }

        return notas;
    }

    public int mediaMaisAlta() {
        double media, mediaMaisAlta = this.mediaUC(0);
        int maisAlta = 0;

        for (int i = 1; i < 5; i++) {
            media = this.mediaUC(i);
            if (media > mediaMaisAlta) {
                maisAlta = i;
                mediaMaisAlta = media;
            }
        }

        return maisAlta;
    }
}
</code></pre>
</details>


<details>
  <summary>TestaEx2</summary>

<pre><code lang="java">package exercicios;
import java.util.Arrays;
import java.util.Scanner;

public class TestaEx2 {
    public static void main(String[] args) {
        ex2 turma = new ex2();
        int[][] pauta = new int[5][5];
        Scanner in = new Scanner(System.in);

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++){
                System.out.print("Aluno: " + i + ", UC: " + j + " => ");
                pauta[i][j] = in.nextInt();
            }
        }
        turma.atualizaPauta(pauta);
        System.out.println(Arrays.deepToString(turma.getPauta()));

        //alineaB(turma, in);
        //alineaC(turma, in);
        //alineaD(turma, in);
        //alineaE(turma);
        //alineaF(turma);
        //alineaG(turma, in);
        //alineaH(turma);
        alineaI(turma);

    }

    private static void alineaB(ex2 turma, Scanner in) {
        int uc;
        do {
            System.out.print("Unidade Curricular (0-4): ");
            uc = in.nextInt();
        } while (!(uc >= 0 && uc <= 4));

        int soma = turma.somaNotasUC(uc);
        System.out.println("Soma das notas da UC " + uc + ": " + soma);

    }

    private static void alineaC(ex2 turma, Scanner in) {
        int aluno;
        do {
            System.out.print("Aluno (0-4): ");
            aluno = in.nextInt();
        } while(!(aluno >= 0 && aluno < 5));

        System.out.println(turma.mediaAluno(aluno));
    }

    private static void alineaD(ex2 turma, Scanner in) {
        int uc;
        do {
            System.out.print("Aluno (0-4): ");
            uc = in.nextInt();
        } while(!(uc >= 0 && uc < 5));

        System.out.println(turma.mediaUC(uc));
    }

    private static void alineaE(ex2 turma) {
        System.out.println("Nota mais alta: " + turma.notaMaisAlta());
    }

    private static void alineaF(ex2 turma) {
        System.out.println("Nota mais baixa: " + turma.notaMaisBaixa());
    }

    private static void alineaG(ex2 turma, Scanner in) {
        int x;
        System.out.print("Valor: ");
        x = in.nextInt();

        System.out.println(Arrays.toString(turma.notasAcimaDeX(x)));
    }

    private static void alineaH(ex2 turma) {
        System.out.println(turma.notas());
    }

    private static void alineaI(ex2 turma) {
        System.out.println(turma.mediaMaisAlta());
    }
}
</code></pre>
</details>

<br>

### Exercício 3

<details>
  <summary>ex3</summary>

<pre><code lang="java">package exercicios;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;


public class ex3 {
    private LocalDate[] datas;
    private int tamanho;
    private int ocupacao = 0;

    public ex3(int tamanho) {
        this.datas = new LocalDate[tamanho];
        this.tamanho = tamanho;
    }

    public void insereData(LocalDate data) {
        this.datas[ocupacao++] = data;
    }

    public LocalDate dataMaisProxima(LocalDate data) {
        long dist = Integer.MAX_VALUE, d;
        LocalDate maisProxima = null;

        for (int i = 0; i < ocupacao; i++) {
            d = Math.abs(ChronoUnit.DAYS.between(this.datas[i],data));
            System.out.println(d);
            if (d < dist) {
                dist = d;
                maisProxima = this.datas[i];
            }
        }

        return maisProxima;
    }

    public String toString() {
        String datas = "Datas:\n";
        LocalDate data;
        for (int i = 0; i < this.ocupacao; i++) {
            data = this.datas[i];
            datas = datas.concat(String.valueOf(data));
            datas = datas.concat("\n");
        }
        return datas;
    }
}
</code></pre>
</details>


<details>
  <summary>TestaEx3</summary>

<pre><code lang="java">package exercicios;

import java.time.LocalDate;
import java.util.Scanner;

public class TestaEx3 {
    public static void main(String[] args) {
        ex3 datas = new ex3(10);
        Scanner in = new Scanner(System.in);

        adicionarData(in, datas);
        adicionarData(in, datas);
        adicionarData(in, datas);

        LocalDate data;
        System.out.print("Dia: ");
        int dia = in.nextInt();//1-31
        System.out.print("Mes: ");
        int mes = in.nextInt(); //1-12
        System.out.print("Ano: ");
        int ano = in.nextInt();
        data = LocalDate.of(ano, mes, dia);

        System.out.println("Data mais proxima: " + datas.dataMaisProxima(data));

        System.out.println(datas.toString());

    }

    private static void adicionarData(Scanner in, ex3 datas) {
        System.out.print("Dia: ");
        int dia = in.nextInt();//1-31
        System.out.print("Mes: ");
        int mes = in.nextInt(); //1-12
        System.out.print("Ano: ");
        int ano = in.nextInt();

        LocalDate data = LocalDate.of(ano, mes, dia);

        datas.insereData(data);
    }
}
</code></pre>
</details>

<br>

### Exercício 4

<details>
  <summary>ex4</summary>

<pre><code lang="java">package exercicios;

import java.util.Arrays;
import java.util.Scanner;

public class ex4 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Tamanho: ");
        int n = in.nextInt();
        int[] array = new int[n];

        for (int i = 0; i < n; i++) array[i] = in.nextInt();

        ordena(array);
        System.out.println(Arrays.toString(array));

        System.out.print("Binary Search: ");
        int x = in.nextInt();
        System.out.println(binarySearch(array, x, array.length-1));
    }

    // Alinea a
    // Insertion sort
    private static void ordena(int[] array) {
        int menor;

        for (int i = 0; i < array.length; i++) {
            menor = i;
            for (int j = i; j < array.length; j++)
                if (array[j] < array[menor]) menor = j;
            swap(array, i, menor);
        }
    }

    // Alinea b
    private static int binarySearch(int[] array, int x, int max) {
        int i = -1;
        int min = 0;
        int mid = max/2;
        while (min < max) {
            if (array[mid] == x) {
                i = mid;
                break;
            } else {
                if (array[mid] < x) {
                    min = mid+1;
                } else {
                    max = mid-1;
                }
                mid = (min + max)/2;
            }
        }
        if (min == max && array[min] == x) i = min;
        return i;
    }

    private static void swap(int[] array, int x, int y) {
        int temp = array[x];
        array[x] = array[y];
        array[y] = temp;
    }
}
</code></pre>
</details>

<br>

### Exercício 5

<details>
  <summary>ex5</summary>

<pre><code lang="java">package exercicios;

public class ex5 {
    private String[] array;
    private int tamanho;
    private int ocupacao;

    public ex5(int tam) {
        this.array = new String[tam];
        this.tamanho = tam;
    }

    public boolean adicionaString(String a) {
        if (this.ocupacao == this.tamanho) return false;
        this.array[ocupacao++] = new String(a);
        return true;
    }

    public String[] stringsExistentes() {
        String[] array = new String[this.ocupacao];
        int i=0;
        for (int k = 0; k < this.ocupacao; k++) {
            boolean rep = false;
            for (int j = 0; j < i; j++)
                if (array[j].equals(this.array[k])) {
                    rep = true;
                    break;
                }
            if (!rep) array[i++] = new String(this.array[k]);
        }

        String[] res = new String[i];
        System.arraycopy(array,0,res,0,i);
        return res;
    }

    public String maiorString() {
        int maiorLe = -1;
        String maior = null;

        for (int i = 0; i < this.ocupacao; i++) {
            String elem = this.array[i];
            if (elem.length() > maiorLe) {
                maiorLe = elem.length();
                maior = elem;
            }
        }

        return new String(maior);
    }

    public String[] repetidos() {
        String[] array = new String[this.ocupacao];
        int p = 0;
        for (int i = 0; i < this.ocupacao; i++) {
            if (this.repete(this.array[i]) && !this.repeteAte(this.array[i], array, p)) {
                array[p++] = this.array[i];
            }
        }
        String[] res = new String[p];
        System.arraycopy(array,0,res,0,p);
        return res;

    }

    public int ocorrencias(String a) {
        int oc = 0;
        for (int i = 0; i < this.ocupacao; i++) {
            if (this.array[i].equals(a)) oc++;
        }
        return oc;
    }

    private boolean repete(String a) {
        return this.ocorrencias(a) > 1;
    }

    private boolean repeteAte(String a, String[] array, int n) {
        int oc = 0;
        for (int i = 0; i < n && oc <= 1; i++) {
            if (a.equals(array[i])) oc++;
        }
        return oc > 0;
    }
}
</code></pre>
</details>


<details>
  <summary>TestaEx5</summary>

<pre><code lang="java">package exercicios;
import java.util.Arrays;
import java.util.Scanner;

public class TestaEx5 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        ex5 classe = new ex5(10);


        classe.adicionaString("Ola");
        classe.adicionaString("Tiago");
        classe.adicionaString("Grand Theft Auto V");
        classe.adicionaString("Ola");
        classe.adicionaString("Carriço");
        classe.adicionaString("Grand Theft Auto V");
        classe.adicionaString("Grand Theft Auto V");
        classe.adicionaString("Bola");

        alineaA(in, classe);
        alineaB(in, classe);
        alineaC(in, classe);
        alineaD(in, classe);

    }

    private static void alineaA(Scanner in, ex5 classe) {
        System.out.println(Arrays.toString(classe.stringsExistentes()));
    }

    private static void alineaB(Scanner in, ex5 classe) {
        System.out.println(classe.maiorString());
    }

    private static void alineaC(Scanner in, ex5 classe) {
        System.out.println(Arrays.toString(classe.repetidos()));
    }

    private static void alineaD(Scanner in, ex5 classe) {
        System.out.println(classe.ocorrencias("Grand Theft Auto V"));
    }
}
</code></pre>
</details>

<br>

### Exercício 6

<details>
  <summary>ex6</summary>

<pre><code lang="java">package exercicios;

import java.util.Scanner;

public class ex6 {
    private int[][] matrix;
    private int N;
    private int M;

    public ex6(int[][] input) {
        this.N = input.length;
        this.M = input[0].length;
        matrix = new int[this.N][this.M];
        for (int i = 0; i < this.N; i++)
            System.arraycopy(input[i],0,this.matrix[i],0,M);
    }

    public ex6 soma(ex6 second) {
        if (this.N == second.N && this.M == second.M) {
            ex6 soma = new ex6(this.matrix);
            for (int i = 0; i < this.N; i++) {
                for (int j = 0; j < this.M; j++) {
                    soma.matrix[i][j] += second.matrix[i][j];
                }
            }
            return soma;
        } else return null;
    }

    public boolean equals(ex6 second) {
        if (this.N == second.N && this.M == second.M) {
            boolean rep = true;

            for (int i = 0; i < this.N && rep; i++)
                for (int j = 0; j < this.M && rep; j++)
                    rep = this.matrix[i][j] == second.matrix[i][j];

            return rep;
        } else return false;
    }

    public ex6 matrizOposta() {
        int[][] oposta = new int[this.N][this.M];

        for (int i = 0; i < this.N; i++)
            for (int j = 0; j < this.M; j++)
                oposta[i][j] = -this.matrix[i][j];

        return new ex6(oposta);
    }

    public int[][] getMatrix() {
        return this.matrix;
    }
}
</code></pre>
</details>


<details>
  <summary>TestaEx5</summary>

<pre><code lang="java">package exercicios;

import java.util.Arrays;

public class TestaEx6 {
    public static void main(String[] args) {
        int[][] matriz = new int[5][5];
        for (int i = 0; i < 5; i++)
            for (int j = 0; j < 5; j++)
                matriz[i][j] = 1;

        ex6 matrix = new ex6(matriz);

        ex6 soma = matrix.soma(matrix);
        ex6 oposta = matrix.matrizOposta();

        System.out.println(matrix.equals(soma));
        System.out.println(Arrays.deepToString(matrix.getMatrix()));
        System.out.println(Arrays.deepToString(soma.getMatrix()));
        System.out.println(Arrays.deepToString(oposta.getMatrix()));
    }
}
</code></pre>
</details>

<br>

### Exercício 7

<details>
  <summary>ex7</summary>

<pre><code lang="java">package exercicios;

import java.lang.Math;
import java.util.Scanner;

public class ex7 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int[][] respostas = new int[2][];
        respostas[0] = new int[5];
        respostas[1] = new int[2];

        do {
            System.out.print("Chaves: ");
            for (int i = 0; i < 5; i++) respostas[0][i] = in.nextInt();
        } while(!valido(respostas[0]));

        do {
            System.out.print("Estrelas: ");
            for (int i = 0; i < 2; i++) respostas[1][i] = in.nextInt();
        } while(!validoEstrelas(respostas[1]));

        if (respostaCorreta(respostas, gerador())) {
            for (int i = 0; i < 100; i+=2) {
                for (int espacos = 0; espacos < i; espacos++) System.out.print(" ");
                for (int j = 0; j < 5; j++) System.out.print(respostas[0][j] + " ");
                System.out.print(respostas[1][0] + " ");
                System.out.print(respostas[1][1] + "\n");
            }
        } else System.out.println("Incorreto :(");

    }

    private static boolean respostaCorreta(int[][] respostas, int[][] chaves) {
        boolean correto = true;

        for (int i = 0; i < 5 && correto; i++) {
            if (i < 2) {
                correto = false;
                for (int k = 0; k < 2 && !correto; k++)
                    if (respostas[1][i] == chaves[1][k])
                        correto = true;
            }
            if (correto) {
                correto = false;
                for (int k = 0; k < 5 && !correto; k++)
                    if (respostas[0][i] == chaves[0][k])
                        correto = true;
            }
        }

        return correto;
    }

    private static boolean validoEstrelas(int[] respostas) {
        boolean rep = true;

        for (int i = 0; i < 2 && rep; i++) {
            if (respostas[i] < 0 || respostas[i] > 9) rep = false;
            else {
                for (int j = 0; j < i && rep; j++)
                    if (respostas[i] == respostas[j]) rep = false;
            }
        }

        return rep;
    }

    private static boolean valido(int[] respostas) {
        boolean rep = true;

        for (int i = 0; i < 5 && rep; i++) {
            if (respostas[i] < 0 || respostas[i] > 50) rep = false;
            else {
                for (int j = 0; j < i && rep; j++)
                    if (respostas[i] == respostas[j]) rep = false;
            }
        }

        return rep;
    }
    
    private static int[][] gerador() {
        int[][] chaves = new int[2][];
        chaves[0] = new int[5]; // Numeros
        chaves[1] = new int[2]; // Estrelas

        int[] chavesPossiveis = new int[50];
        for (int i = 0; i < 50; i++) chavesPossiveis[i] = i+1;
        int[] estrelasPossiveis = new int[9];
        for (int i = 0; i < 9; i++) estrelasPossiveis[i] = i+1;

        for (int i = 0; i < 5; i++) {
            int k = (int) (Math.random() * (50-i));
            chaves[0][i] = chavesPossiveis[k];
            swap(chavesPossiveis, k, 50-i-1);
        }
        for (int i = 0; i < 2; i++) {
            int k = (int) (Math.random() * (9-i));
            chaves[1][i] = estrelasPossiveis[k];
            swap(estrelasPossiveis, k, 9-i-1);
        }
        return chaves;
    }

    /* Testes
    private static int[][] gerador() {
        int [][] chaves = new int[2][];
        chaves[0] = new int[]{1, 2, 3, 4, 5};
        chaves[1] = new int[]{1, 2};
        return chaves;
    }
    */

    private static void swap(int[] array, int x, int y) {
        int temp = array[x];
        array[x] = array[y];
        array[y] = temp;
    }
}
</code></pre>
</details>

<br><br>

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/POO/fichas)