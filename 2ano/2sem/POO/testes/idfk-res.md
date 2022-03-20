```Java

import Exceptions.AlreadyPlayingException;
import Exceptions.PodcastNotFoundException;
import Exceptions.UserCurrentlySubscribedException;

import java.io.IOException;
import java.io.FileWriter;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.*;



//----------------------------------------------------------------------------------------------------------------
// -- MAIN --
//----------------------------------------------------------------------------------------------------------------

public class Main {
    public static void main(String[] args) throws PodcastNotFoundException,
            UserCurrentlySubscribedException,
            AlreadyPlayingException, IOException {

        LocalTime time1 = LocalTime.parse("02:24:55", DateTimeFormatter.ofPattern("HH:mm:ss"));
        LocalTime time2 = LocalTime.parse("00:55:29", DateTimeFormatter.ofPattern("HH:mm:ss"));

        ArrayList<String> content = new ArrayList<>();

        Episodio e1 = new Episodio("Episode 1", time1, 78, content, 356, LocalDateTime.now());
        Episodio e2 = new Episodio("Episode 2", time2, 91, content, 560, LocalDateTime.now());
        Episodio e3 = new Episodio("Episode 3", time1, 78, content, 150, LocalDateTime.now());
        Episodio e4 = new Episodio("Episode 4", time2, 80, content, 4561, LocalDateTime.now());

        ArrayList<Episodio> list1 = new ArrayList<>();
        list1.add(e1);list1.add(e2);list1.add(e3);
        ArrayList<Episodio> list2 = new ArrayList<>();
        list2.add(e4);

        Podcast p1 = new Podcast("Exame2021.Podcast 1",list1);
        System.out.println(p1.getEpisodio("Episode 2"));
        Podcast p2 = new Podcast("Exame2021.Podcast 2",list2);

        ArrayList<Podcast> listPodcast1 = new ArrayList<>();
        listPodcast1.add(p1);
        ArrayList<Podcast> listPodcast2 = new ArrayList<>();
        listPodcast2.add(p1);
        listPodcast2.add(p2);

        Utilizador u1 = new Utilizador("mariajoao99","Mary Jane",listPodcast1);
        Utilizador u2 = new Utilizador("joaomiguel2000","João Miguel",listPodcast2);
        UtilizadorPremium u3 = new UtilizadorPremium("mariobanana2","mario pereira",listPodcast2);
        u3.playEpisodio(p1.getId(),e1.getNome());
        u3.playEpisodio(p1.getId(),e2.getNome());
        u3.playEpisodio(p1.getId(),e3.getNome());
        System.out.println("user 3 waiting list: "+u3.getWaitingList());
        u3.gravaInfoEpisodiosParaTocarMaisTarde("user3");

        SpotifyPOO spoo = new SpotifyPOO();
        spoo.addPodcast(p1);
        spoo.addPodcast(p2);
        spoo.addUser(u1);
        spoo.addUser(u2);

        System.out.println("Exame2021.Episodio mais longo: "+spoo.getEpisodioMaisLongo(u2.getId()));
        try {
            spoo.remove(p2.getId());
        } catch (UserCurrentlySubscribedException e) {};
        System.out.println("Map dos episodios por classificação: "+spoo.episodiosPorClassf());
        System.out.println(p1);

    }
    
}



//----------------------------------------------------------------------------------------------------------------
// -- Interface Exemplo --
//----------------------------------------------------------------------------------------------------------------

public interface InterfaceExemplo {
    void play(String id);
    boolean run();
}



//----------------------------------------------------------------------------------------------------------------
// -- PODCAST --
//----------------------------------------------------------------------------------------------------------------

public class Podcast {
    String id;                 //identificador do podcast
    List<Episodio> episodios; //lista de episodios

    public Podcast(String id,List<Episodio> episodios) {
        this.id = id;
        this.episodios = episodios;
    }

    public Podcast(Podcast obj) {
        this.id = obj.getId();
        this.episodios = obj.getEpisodios();
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<Episodio> getEpisodios() {
        return episodios;
    }

    public void setEpisodios(List<Episodio> episodios) {
        this.episodios = episodios;
    }

    public Episodio getEpisodio(String idEpisodio) {
        return episodios.stream().filter(ep -> ep.getNome().equals(idEpisodio))
                .findFirst().orElse(null);
    }

    @Override
    public String toString() {
        return "Exame2021.Podcast{" +
                "id='" + id + '\'' +
                ", episodios=\n" + episodios +
                "}";
    }

    public Podcast clone() {
        return new Podcast(this);
    }

    public boolean equals(Object obj) {
        if (obj==this) return true;
        if (obj== null || obj.getClass()!=this.getClass()) return false;
        Podcast p = (Podcast) obj;
        return p.getId().equals(this.getId()) &&
                p.getEpisodios().equals(this.getEpisodios());
    }
    
}



//----------------------------------------------------------------------------------------------------------------
// -- UTILIZADOR --
//----------------------------------------------------------------------------------------------------------------

public class Utilizador implements InterfaceExemplo {
    private String id;
    private String nome;
    private List<Podcast> subscricoes; //podcasts a q o user está subscrito
    private Episodio isPlaying; //boleano que assinala se o user esta a reproduzir conteudo

    public Utilizador(String id, String nome, List<Podcast> subscricoes) {
        this.id = id;
        this.nome = nome;
        this.subscricoes = subscricoes;
        this.isPlaying = null;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public List<Podcast> getSubscricoes() {
        return subscricoes;
    }

    public void setSubscricoes(List<Podcast> subscricoes) {
        this.subscricoes = subscricoes;
    }

    public Episodio getIsPlaying() { return isPlaying; }

    public void setPlaying(Episodio playing) { isPlaying = playing; }

    @Override
    public String toString() {
        return "Exame2021.Utilizador{" +
                "id='" + id + '\'' +
                ", nome='" + nome + '\'' +
                ", subscricoes=" + subscricoes +
                '}';
    }

    public void playEpisodio(String idPodCast, String nomeEpisodio)
            throws AlreadyPlayingException {
        if (!(isPlaying == null)) throw new AlreadyPlayingException();
        else {
            for (Podcast p : subscricoes) {
                if (p.getId().equals(idPodCast)) setPlaying(p.getEpisodio(nomeEpisodio));
            }
        }
    }


    @Override
    public void play(String id) {
        System.out.println("The id "+id+" is currently playing.\n");
        run();
    }

    @Override
    public boolean run() {
        return true;
    }

}



//----------------------------------------------------------------------------------------------------------------
// -- SPOTIFY POO --
//----------------------------------------------------------------------------------------------------------------

public class SpotifyPOO {
    HashMap<String,Podcast> podcasts; //(id podcast,obj podcast)
    HashMap<String,Utilizador> utilizadores; //(id user,user)


    public SpotifyPOO() {
        this.podcasts = new HashMap<>();
        this.utilizadores = new HashMap<>();
    }

    public SpotifyPOO(HashMap<String,Podcast> podcasts,
                      HashMap<String,Utilizador> users) {
        this.podcasts = podcasts;
        this.utilizadores = users;
    }

    public HashMap<String, Podcast> getPodcasts() {
        return podcasts;
    }

    public void setPodcasts(HashMap<String, Podcast> podcasts) {
        this.podcasts = podcasts;
    }

    public HashMap<String, Utilizador> getUtilizadores() {
        return utilizadores;
    }

    public void setUtilizadores(HashMap<String,Utilizador> utilizadores) {
        this.utilizadores = utilizadores;
    }

    public List<Episodio> getEpisodios(String nomePodcast) {
        return this.podcasts.get(nomePodcast).getEpisodios();
    }

    /**
     * Adiciona um utilizador ao sistema
     * @param usr
     * @throws UserCurrentlySubscribedException
     */
    public void addUser(Utilizador usr) throws UserCurrentlySubscribedException {
        if (!this.utilizadores.keySet().contains(usr.getId())) this.utilizadores.put(usr.getId(),usr);
        else throw new UserCurrentlySubscribedException();
    }

    /**
     * Adiciona um podcast ao sistema
     * @param podcast
     * @throws PodcastNotFoundException
     */
    public void addPodcast(Podcast podcast) throws PodcastNotFoundException {
        if (!this.podcasts.keySet().contains(podcast.getId())) this.podcasts.put(podcast.getId(),podcast);
        else throw new PodcastNotFoundException();
    }

    /**
     * Remove do sistema o podcast com o ID indicado, não será possivel remocver se o podcast
     * nao existir registado no sistema ou se o mesmo podcast tiver utilizadores que atualmente o
     * estejam a subscrever
     * @param nomeP
     * @throws UserCurrentlySubscribedException
     * @throws PodcastNotFoundException
     */
    public void remove(String nomeP) throws UserCurrentlySubscribedException, PodcastNotFoundException {
        for (Utilizador user : this.utilizadores.values()) {
            if (user.getSubscricoes().stream().anyMatch(a->a.getId().equals(nomeP))) throw new UserCurrentlySubscribedException();
        }
        if (this.podcasts.keySet().contains(nomeP)) this.podcasts.remove(nomeP);
        else throw new PodcastNotFoundException();
    }

    /**
     * devolve o epis´odio mais longo de entre os
     * podcasts que um utilizador tem subscritos.
     * @param u
     * @return
     * @throws NoSuchElementException
     */
    public Episodio getEpisodioMaisLongo(String u) throws NoSuchElementException {
        LocalTime max = LocalTime.parse("00:00:00", DateTimeFormatter.ofPattern("HH:mm:ss"));
        Episodio maxEp = null;
        for (Podcast p : this.utilizadores.get(u).getSubscricoes()) {
            Episodio ep = p.getEpisodios().stream().max(Comparator.comparing(Episodio::getDuracao)).orElseThrow(NoSuchElementException::new);
            if (ep.getDuracao().isAfter(max) ) {
                max = ep.getDuracao();
                maxEp = ep;
            }
        }
        return maxEp;
    }

    /**
     * associa a cada valor de classificacao a lista dos epis´odios,
     * de todos os podcasts, com essa mesma classificacao
     * @return
     */
    public Map<Integer,List<Episodio>> episodiosPorClassf() {
        HashMap<Integer,List<Episodio>> res = new HashMap<>();
        for (Podcast p : this.podcasts.values()) {
            for (Episodio e : p.getEpisodios()) {
                if (res.containsKey(e.getClassificacao())) res.get(e.getClassificacao()).add(e);
                else {
                    ArrayList<Episodio> list = new ArrayList<>();
                    list.add(e);
                    res.put(e.getClassificacao(),list);
                }
            }
        }
        return res;
    }

}



//----------------------------------------------------------------------------------------------------------------
// -- EPISODIO--
//----------------------------------------------------------------------------------------------------------------

public class Episodio {
    private String nome;
    private LocalTime duracao;
    private int classificacao; //dada pelos seus ouvintes (valor de 0..100)
    private List<String> conteudo; //corresponde ao texto que é dito quando se reproduz o episodio
    private int numeroVezesTocada; //qts vezes é que o podcast foi ouvido
    private LocalDateTime ultimaVez; //regista quando foi reproduzido ultima vez

    public Episodio(String nome, LocalTime duracao, int classificacao, List<String> conteudo, int numeroVezesTocada, LocalDateTime ultimaVez) {
        this.nome = nome;
        this.duracao = duracao;
        this.classificacao = classificacao;
        this.conteudo = conteudo;
        this.numeroVezesTocada = numeroVezesTocada;
        this.ultimaVez = ultimaVez;
    }

    public String getNome() {
        return nome;
    }

    public LocalTime getDuracao() {
        return duracao;
    }

    public int getClassificacao() {
        return classificacao;
    }

    public List<String> getConteudo() {
        return conteudo;
    }

    public int getNumeroVezesTocada() {
        return numeroVezesTocada;
    }

    public LocalDateTime getUltimaVez() {
        return ultimaVez;
    }


    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setDuracao(LocalTime duracao) {
        this.duracao = duracao;
    }

    public void setClassificacao(int classificacao) {
        this.classificacao = classificacao;
    }

    public void setConteudo(List<String> conteudo) {
        this.conteudo = conteudo;
    }

    public void setNumeroVezesTocada(int numeroVezesTocada) {
        this.numeroVezesTocada = numeroVezesTocada;
    }

    public void setUltimaVez(LocalDateTime ultimaVez) {
        this.ultimaVez = ultimaVez;
    }

    @Override
    public String toString() {
        return "Exame2021.Episodio{" +
                "nome='" + nome + '\'' +
                ", duracao=" + duracao +
                ", classificacao=" + classificacao +
                ", conteudo=" + conteudo +
                ", numeroVezesTocada=" + numeroVezesTocada +
                ", ultimaVez=" + ultimaVez +
                "}\n";
    }
    
}



//----------------------------------------------------------------------------------------------------------------
// -- UTILIZADOR PREMIUM --
//----------------------------------------------------------------------------------------------------------------

public class UtilizadorPremium extends Utilizador implements InterfaceExemplo  {
    private List<Episodio> waitingList;

    public UtilizadorPremium(String id, String nome, List<Podcast> subscricoes) {
        super(id, nome, subscricoes);
        this.waitingList = new ArrayList<>();
    }

    public List<Episodio> getWaitingList() {
        return waitingList;
    }

    public void setWaitingList(List<Episodio> waitingList) {
        this.waitingList = waitingList;
    }

    public void playEpisodio(String idPodCast, String nomeEpisodio)
            throws AlreadyPlayingException {
        Podcast p = super.getSubscricoes().stream().filter(a->a.getId().equals(idPodCast)).findFirst().orElse(null);
        if (super.getIsPlaying()==null) {
            super.setPlaying(p.getEpisodio(nomeEpisodio));
        }
        else {
            waitingList.add(p.getEpisodio(nomeEpisodio));
        }
    }

    public void gravaInfoEpisodiosParaTocarMaisTarde(String fich) throws IOException {
        FileWriter fw = new FileWriter(fich+".txt");
        fw.append(super.getNome()+"\n");
        for (Episodio ep : waitingList) {
            fw.append(ep.getNome()+" - ");
            fw.append(ep.getDuracao().toString()+"\n");
        }
        fw.flush();
        fw.close();
    }

    public boolean testInstance() {
        if (this instanceof InterfaceExemplo) return true;
        else return false;
    }

}

```

<br><br>

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/POO/testes)
