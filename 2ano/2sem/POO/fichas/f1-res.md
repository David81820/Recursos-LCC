## Exercícios I

<details>
  <summary>ExerciciosI</summary>


```java

public class ExerciciosI {
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

```
</details>

<br>

<details>
  <summary>TestePrograma</summary>

```java
 import java.util.Scanner;

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
```
</details>

<br><br>

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/POO)