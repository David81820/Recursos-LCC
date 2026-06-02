<br>

<h1 align="center">Resolução do exame de Época Especial de Programação Concorrente de 30 de Julho de 2016, feito por um aluno</h1>

<br>

exclusao mutua e ordem de execução
exclusao mutua é quando um processo está a executar codigo sobre um objecto e o tem em lock, neste caso mais ninguem pode fazer nada pois esta "fechado" com aquele processo.
um exemplo exagerado é:
um banco e um processo faz lock do banco para efetuar uma transferencia, como fez lock do banco todo, mais nenhuma operação avança em nenhuma conta pois o banco está todo "fechado" enquanto a tranferencia decorre.

ordem de execuçao, é quando ha varios processos a tentar aceder ao mesmo bocado de codigo,
se nao houver pre condiçao de quem entra primeiro, o acesso é dado ao primeiro que fizer lock,
neste caso pode haver starvation pois nao ha garantia nenhuma que um dado processo eventualmente entrará enquanto houver varios processos a concorrer para aquele codigo.

----

```java
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

import javax.management.openmbean.OpenMBeanConstructorInfo;


class Ponte {

    int ocupacao=0;
    Lock lock = new ReentrantLock();
    Condition canReturn = lock.newCondition();
    Condition canGo = lock.newCondition();

    
    void inicioTravessiaIda() throws InterruptedException {
        lock.lock();
        try{
            if (ocupacao == 10) {
                System.out.println("Ponte cheia");
                wait(); 
            }
            ocupacao +=1;
            Thread.sleep(5000);
            fimTravessia();
        } finally {
            lock.unlock();
        }


    }

    void inicioTravessiaVolta() throws InterruptedException{
        lock.lock();
        try{
            if (ocupacao == 10) {
                System.out.println("Ponte cheia");
                wait(); 
            }
            ocupacao +=1;
            Thread.sleep(5000);
            fimTravessia();
        } finally {
            lock.unlock();
        }
    

    }

    void fimTravessia() throws InterruptedException{
        lock.lock();
        try {
            ocupacao-=1;
            System.out.println("Pode entrar um");           
            canReturn.signal();
            canGo.signal();

        } finally {
            lock.unlock();
        }
    }
   
}
```

<br><br>

[![retroceder]({{ '/assets/images/Rewind.png' | relative_url }})](https://david81820.github.io/Recursos-LCC/PC/testes)