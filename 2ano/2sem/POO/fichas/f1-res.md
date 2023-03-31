### Exercícios I

<details>
  <summary>ExerciciosI</summary>

<pre><code lang="java">package ex1;
import static java.lang.Math.abs;
import static java.lang.Math.sqrt;

import java.util.Scanner;
import java.time.LocalDateTime;

public class exI {
    public static void main(String[] args) {
        // Ex 1
        System.out.println(diaDaSemana(30, 3, 2019));

        // Ex 4
        int[] r = mediaTemps(new int[]{15, 12, 20, 23, 18}, 5);
        System.out.print("A media das temperaturas foi de " + r[0] + " graus.\nA maior variaçao registou-se entre os dias " +
                r[1] + " e " + (r[1]+1) + ", tendo a temperatura ");
        if (r[2] > 0) System.out.print("subido ");
        else System.out.print("descido ");
        System.out.println(abs(r[2]) + " graus.");

        // Ex 5
        triangulo();

        // Ex 6
        primos();

        // Ex 7
        idade();
    }

    // Ex 1
    private static String diaDaSemana(int dia, int mes, int ano) {
        int diaSemana = ((ano - 1900)*365) + (ano - 1900)/4;
        if (ano % 4 == 0 && mes < 3) {
            diaSemana--;
        }

        for (int i = 1; i < mes; i++) {
            diaSemana += 30;
            if (i == 1 || i == 3 || i == 5 || i == 7 || i == 8 || i == 10 || i == 12)
                diaSemana++;
            else if (i == 2)
                diaSemana-=2;
        }
        diaSemana += dia;
        return Semana(diaSemana % 7);
    }

    // Ex 2
    private static void somaDatas() {
        // wtf
    }

    // Ex 3
    private static int[] classificacoes(int[] lista, int N) {
        int[] intervalos = {0,0,0,0};
        for (int i = 0; i < N; i++) {
            if (lista[i] >= 0 && lista[i] < 5) intervalos[0]++;
            else if (lista[i] >= 5 && lista[i] < 10) intervalos[1]++;
            else if (lista[i] >= 10 && lista[i] < 15) intervalos[2]++;
            else intervalos[3]++;
        }
        return intervalos;
    }

    // Ex 4
    private static int[] mediaTemps(int[] temperaturas, int N) {
        int[] resultado = {temperaturas[0],0,-1}; // Media, dia, variaçao
        for (int i = 1; i < N; i++) {
            resultado[0] += temperaturas[i];
            int diferenca = temperaturas[i] - temperaturas[i-1];
            if (diferenca > resultado[2]) {
                resultado[1] = i;
                resultado[2] = diferenca;
            }
        }
        resultado[0] /= N;
        return resultado;
    }

    //Ex 5
    private static void triangulo() {
        double base = 1, altura;
        double area, perimetro;
        Scanner input = new Scanner(System.in);
        while (base != 0) {
            System.out.print("Base: ");
            base = input.nextDouble();
            if (base == 0) break;
            System.out.print("Altura: ");
            altura = input.nextDouble();

            area = (base*altura)/2;
            System.out.printf("Area: %.5f\n", area);
        }
    }

    // Ex 6
    private static void primos() {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        for(int i = 2; i < n; i++) {
            if (ePrimo(i)) System.out.printf("%d ", i);
        }
        System.out.println();
        // Ninguem quer "jogar novamente" so... nao vou por isso aqui
    }

    // Ex 7
    private static void idade() {
        Scanner input = new Scanner(System.in);
        
        System.out.println("\n\nIntroduz uma data de nascimento.\nComeçando pelo ano: ");
        String ano = input.next();
        int y = Integer.parseInt( ano );
        System.out.println("\nAgora o mês, em formato numérico: ");
        String mes = input.next();
        int m = Integer.parseInt( mes );
        System.out.println("\nFinalmente o dia do mês: ");
        String dia = input.next();
        int d = Integer.parseInt( dia );
        
        LocalDateTime ani = LocalDateTime.of( y , m , d , 0, 0 ,0 );
        
        LocalDateTime now = LocalDateTime.now();
        
        long numberOfHours = Duration.between(ani, now).toHours();
        
        System.out.println("\nNúmero de horas passadas entre a data de nascimento e hoje : " +numberOfHours);
    }

    // Auxiliares
    private static String Semana(int dia) {
        switch(dia) {
            case 0: return "Domingo"; break;
            case 1: return "Segunda-feira"; break;
            case 2: return "Terça-feira"; break;
            case 3: return "Quarta-feira"; break;
            case 4: return "Quinta-feira"; break;
            case 5: return "Sexta-feira"; break;
            case 6: return "Sabado"; break;
        }
        return "Nope";
    }

    private static Boolean ePrimo(int n) {
        boolean primo = true;
        for (int i = 2; i < n; i++)
            if ((n % i) == 0) {
                primo = false;
                break;
            }
        return primo;
    }

}
</code></pre>
</details>

<br>

### Exercícios II

<details>
  <summary>ExerciciosII</summary>

<pre><code lang="java">import java.time.LocalDateTime;

public class ExerciciosII {
    public double celsiusParaFahrenheit(double graus) {
        return 1.8 * graus + 32;
    }

    public int maximoNumeros(int a, int b) {
        return a > b ? a : b;
    }

    public String criaDescricaoConta(String nome, double saldo) {
        return "A conta pertencente a " + nome + " tem um saldo de " + saldo;
    }

    public double eurosParaLibras(double valor, double taxaConversao) {
        return valor * taxaConversao;
    }

    public long factorial(int num) {
        return num > 0 ? num * factorial((num - 1)) : 1;
    }

    public long tempoGasto() {
        int startTime = LocalDateTime.now().getNano();
        long factorialOf5000 = factorial(5000);
        int tExec = LocalDateTime.now().getNano() - startTime;
        return tExec;
    }
}
</code></pre>
</details>


<details>
  <summary>TestePrograma</summary>

<pre><code lang="java">import java.util.Scanner;

public class TestePrograma {
    public static void main(String[] args) {
        Scanner inputReader = new Scanner(System.in);
        ExerciciosII exs = new ExerciciosII();

        System.out.println("Introduz o nº da alínea:");
        int alinea = inputReader.nextInt();
        inputReader.nextLine();

        switch(alinea) {
            case 1:
                System.out.println("Introduz uma temperatura em graus Celsius:");
                double grausC = inputReader.nextDouble();
                double grausF = exs.celsiusParaFahrenheit(grausC);
                System.out.printf("%fºC = %fºF\n", grausC, grausF);
                break;
            case 2:
                System.out.println("Introduz dois valores, separados por um espaço:");
                String nums = inputReader.nextLine();
                Scanner numSplitter = new Scanner(nums);
                int a = numSplitter.nextInt();
                int b = numSplitter.nextInt();
                System.out.printf("O maior de %d e %d é %d.\n",a,b,exs.maximoNumeros(a,b));
                break;
            case 3:
                System.out.println("Introduz um nome e um valor (saldo):");
                String nome = inputReader.nextLine();
                int saldo = inputReader.nextInt();
                System.out.println(exs.criaDescricaoConta(nome,saldo));
                break;
            case 4:
                System.out.println("Introduz um valor em euros:");
                double valueEuros = inputReader.nextDouble();
                // System.out.println("Introduz o valor da taxa de conversão de euros para libras:");
                // double conversionRate = inputReader.nextDouble();
                double conversionRate = 0.8428;
                double valuePounds = exs.eurosParaLibras(valueEuros,conversionRate);
                System.out.printf("%f EUR = %f GBP", valueEuros, valuePounds);
                break;
            case 5:
                System.out.println("Introduz dois valores inteiros, separados por um espaço:");
                nums = inputReader.nextLine();
                numSplitter = new Scanner(nums);
                a = numSplitter.nextInt();
                b = numSplitter.nextInt();
                System.out.printf("Os dois valores por ordem decrescente ficam: %d %d\n", a > b ? a : b, a > b ? b : a);
                System.out.printf("A média destes dois valores é %f\n.", (a + b) / 2.0);
                break;
            case 6:
                if(args.length == 0) {
                    System.out.println("Erro - não foi passado nenhum argumento ao programa");
                    break;
                }
                int num = Integer.parseInt(args[0]);
                long factNum = exs.factorial(num);
                System.out.printf("O fatorial de %d é %d. (o valor %d foi passado como argumento ao programa.)\n", num, factNum, num);
                break;
            case 7:
                long tExec_ns = exs.tempoGasto();
                System.out.printf("O ciclo demorou %f ms a executar.\n",tExec_ns / 100000.0);
                break;
            default:
                break;
        }
    }
}
</code></pre>
</details>

<br><br>

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/POO/fichas)