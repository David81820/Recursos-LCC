### Exercícios I

<details>
  <summary>ExerciciosI</summary>

<pre><code lang="java">public class ExerciciosI {
    public int dayOfTheWeek(int day, int month, int year) {
        int totalDays = (int)((year - 1900) * 365.25);
        if(year % 4 == 0 && (year % 100 != 0 || year % 400 == 0) && month < 3) totalDays--;
        for(int i = month; i > 0; i--) {
            if(i == 2) totalDays += 28;
            else if(i == 4 || i == 6 || i == 9 || i == 11) totalDays += 30;
            else totalDays += 31;
        }
        return totalDays % 7;
    }
}
</code></pre>
</details>


<details>
  <summary>TestePrograma</summary>

<pre><code lang="java">import java.util.Scanner;

public class TestePrograma {
    public static void main(String[] args) {
        ExerciciosI exs = new ExerciciosI();

        Scanner inputReader = new Scanner(System.in);

        System.out.println("Introduz o nº da alínea:");
        int alinea =  inputReader.nextInt();
        inputReader.nextLine();

        switch(alinea) {
            case 1:
                System.out.println("Introduz uma data no formato DD-MM-AAAA:");
                String date = inputReader.nextLine();
                Scanner dateReader = new Scanner(date);
                dateReader.useDelimiter("\\W");
                int day = dateReader.nextInt();
                int month = dateReader.nextInt();
                int year = dateReader.nextInt();
                int weekDay = exs.dayOfTheWeek(day,month,year);
                switch(weekDay) {
                    case 0: System.out.println("Essa data é um domingo."); break;
                    case 1: System.out.println("Essa data é uma segunda-feira."); break;
                    case 2: System.out.println("Essa data é uma terça-feira."); break;
                    case 3: System.out.println("Essa data é uma quarta-feira."); break;
                    case 4: System.out.println("Essa data é uma quinta-feira."); break;
                    case 5: System.out.println("Essa data é uma sexta-feira."); break;
                    case 6: System.out.println("Essa data é um sábado."); break;
                }
                break;
        }
    }
}
</code></pre>
</details>

<br>

### Exercícios II

<details>
  <summary>ExerciciosI</summary>

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