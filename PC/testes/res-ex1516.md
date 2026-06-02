<br>

<h1 align="center">Resolução do exame de Programação Concorrente de 30 de Junho de 2016, feito por um aluno</h1>

<br>

palavra final
é uma afirmação errada pois a keyword final indica que a variavel será de single assignment, ou seja, uma vez atribuido um valor ou referencia, não volta a mudar, é imutável.

e o final garante que quando o objecto è lido, o valor é o correcto.
no caso de ser um construtor de um objecto, outra thread que tente ler esse objecto, so vai conseguir ler no fim da construçao e assim é garantido que lê os dados correctos.

se for para ler uma variavel que seja final, nao é necessário fazer syncronized pois a garantia de ser o valor correcto é  dado pela final.

----

```java
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;


class Exame {
    int c1,c2,c3;
    String cd1, cd2, cd3;

    Lock lock = new ReentrantLock();
    Condition notThere = lock.newCondition();

    Exame(String a, String b, String c){
        this.cd1 = a;
        this.cd2 = b;
        this.cd3 = c;

        this.c1 = 0; this.c2 = 0; this.c3 = 0;
    }


    void vota(String candidato){
        lock.lock();
        try {
            if (candidato.compareTo(cd1) == 0) { c1 += 1; }
            if (candidato.compareTo(cd2) == 0) { c2 += 1; }
            if (candidato.compareTo(cd3) == 0) { c3 += 1; }
            notThere.signalAll();
        } finally {
            lock.unlock();
        }
        //notThere.signalAll();
    }

    void espera (String a, String b, String c)  throws InterruptedException{
        lock.lock();
        try {
            if (a.compareTo(cd1) != 0) return;
            if (b.compareTo(cd2) != 0) return;
            if (c.compareTo(cd3) != 0) return;
    
            while ((c1 < c2 && c2 < c3) != true) {
                notThere.await();
            }
        } finally {
            lock.unlock();
        }
    }

    void showVotes() {
        System.out.println("Votos-----------------");
        System.out.println(cd1 + ": " + c1);
        System.out.println(cd2 + ": " + c2);
        System.out.println(cd3 + ": " + c3);
        System.out.println("----------------------");
    }
}


class Monitor {
    public static void main(String[] args) {
        Exame teste = new Exame("tiago", "sofia", "rosa");

        new Thread(() -> {
            try {
                System.out.println("Vou entrar...");
                teste.espera("tiago", "sofia", "rosa");
                System.out.println("1 - sai da espera finalmente!!!");

            } catch (Exception e) {}
        }).start();



        new Thread(() -> {
            try{
                System.out.println("Vou votar...");
                teste.showVotes();
                Thread.sleep(1000);

                teste.vota("tiago");
                teste.vota("rosa");
                teste.vota("sofia");
                teste.showVotes();

                Thread.sleep(1000);
                
                teste.vota("rosa");
                System.out.println("o 2 deve sair aqui");
                teste.vota("rosa");
                teste.showVotes();
                
                Thread.sleep(1000);
                
                teste.vota("sofia");
                System.out.println("o 1 deve sair aqui");

                teste.showVotes();

                Thread.sleep(1000);
        
        
                teste.showVotes();

            } catch (Exception e) { }
        }).start();





    }
}
```

----

```erl
-module(vote).
-export([start/0, vota/0, espera/3, votos/2]).


vota() ->
    receive
        sofia -> 
            votos ! {sofia},
            vota();
        tiago -> 
            votos ! {tiago},
            vota()
end.

votos(S,T)->
    espera ! {S,T},
    receive
        {sofia} ->
            io:format("Voto para a Sofia~n"),
            %espera ! {S+1,T},
            votos(S+1,T);
        {tiago} ->
            io:format("Voto para o Tiago~n"),
            %espera ! {S,T+1},
            votos(S,T+1);
        {show} ->
            io:format("S= ~p, T= ~p ~n",[S,T]),
            votos(S,T)
end.


espera(_,_,true) ->
    io:format("Tiago ultrapassou a Sofia~n");
espera(_,_,false) ->
    receive
        {S,T} ->
            %io:format("recebi os votos da votacao ~n",[]),
            Res = if
                T > S -> true;
                T < S -> false;
                T == S -> false
            end,
    espera(S,T,Res)
end.


start() ->
    register (espera, spawn(vote, espera, [0,0,false])),
    register (votos, spawn(vote, votos,[0,0])),
    io:format("criado o processo de votos~n"),

    timer:sleep(2000),
    votos ! {sofia},
    timer:sleep(2000),
    votos ! {tiago},
    timer:sleep(2000),
    votos ! {tiago},
    timer:sleep(2000),
    votos ! {show}.
```

```erl
-module(tut15).

-export([start/0, ping/2, pong/0]).

ping(0, Pong_PID) ->
    Pong_PID ! finished,
    io:format("ping finished~n", []);

ping(N, Pong_PID) ->
    Pong_PID ! {ping, self()},
    receive
        pong ->
            io:format("Ping received pong~n", [])
    end,
    ping(N - 1, Pong_PID).

pong() ->
    receive
        finished ->
            io:format("Pong finished~n", []);
        {ping, Ping_PID} ->
            io:format("Pong received ping~n", []),
            Ping_PID ! pong,
            pong()
    end.

start() ->
    Pong_PID = spawn(tut15, pong, []),
    spawn(tut15, ping, [3, Pong_PID]).
```

```erl
-module(msg).
-export([start/0, envia/2, recebe/0]).

envia(BoxPid,0) ->
    BoxPid ! stop;
envia(BoxPid,N)->
    BoxPid ! {msg,"nova mensagem!"},
    timer:sleep(5000),
    envia(BoxPid,N-1).

recebe() ->
    receive
        {msg,Texto} ->
            io:format("mensagem recebida: ~p ~n",[Texto]),
            recebe();
        stop ->
            io:format("hora de terminar~n",[]),
            ok
end.

start() ->
    BoxPid = spawn(msg, recebe, []),
    spawn(msg, envia, [BoxPid,3]).
```

<br><br>

[![retroceder]({{ '/assets/images/Rewind.png' | relative_url }})](https://david81820.github.io/Recursos-LCC/PC/testes)