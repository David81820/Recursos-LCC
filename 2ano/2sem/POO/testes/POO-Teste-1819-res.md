```Java
//------------------------------------------------------------------------------------------
// ___ 1 ‾‾‾
//------------------------------------------------------------------------------------------

import java.util.List;
import java.util.ArrayList;


public class PolyAsList{
    List<Double> polinomio; 


    public PolyAsList(){
        this.polinomio = new ArrayList<>();
    }

    public PolyAsList(List<Double> pol){
        this.polinomio = pol.stream().collect(Collectors.toList());
    }



    public void addMonomio(int grau, double coef){
        int graus = this.polinomio.size();
        if(graus<=grau)
            for(int i=graus, i<grau, i++)
                this.polinomio.add(0.0);
            this.polinomio.add(coef);
        else
            this.polinomio.set(grau,coef);
    }


    public  double  calcula(double x){
        double res = 0.0;
        for(int n=0; n<this.polinomio.size();n++){
            res += this.polinomio.get(n) * (Math.pow(x,n));  
        }
        return res; 
    }


    public  int  grau (){
        return this.polinomio.size()-1;
    }


    public  PolyAsList  derivada (){
        List<Double> ret = new ArrayList<>(); 
        for (int n=0;n<this.polinomio.size();n++){
            if(n==0){
                this.polinomio.remove(n);
            }
            ret.add((this.polinomio.get(n)*n));
        }
        return new PolyAsList(ret);
    }



    public String toString(){
        StringBuilder sb = new StringBuilder();
        for(int i = polinomio.size()-1; i>=0; i--){
            sb.append(polinomio.get(i)).append("x^").append(i);
            if (i>0)
                sb.append(" + ");
        }
        return sb.toString();
    }
                                                                     
}

                                                                     
                                                                     
//------------------------------------------------------------------------------------------
// ___ 2 ‾‾‾
//------------------------------------------------------------------------------------------

import  java.util.Set;
import  java.util.Map;
import  java.util.HashMap;


public  class  Grafo {//  vari ́aveis  de  inst^anciaprivate Map <String , Set <String >> adj;

    private Map<String  Set<String >> adj;
    
    
    public Grafo(){
        this.adj = new HashMap<>();     
    }

    public Grafo(Map<String, Set<String>> adj){
        this.adj = adj.entryset().stream().collect(Collectors.toMap(e->e.getKey(), e->new HashMap<>(e.getValue())));
    }



    public void addArco(String vOrig, String vDest){
        this.adj.putIfAbsent(vOrig, new HashSet<>());
        this.adj.putIfAbsent(vDest, new HashSet<>());
        this.adj.get(vOrig).add(vDest);
    }


    public boolean isSink(String v){
        if(!this.adj.containsKey(v))
            return false;
        else
            return this.adj.get(v).isEmpty();
    }


    public int size(){
        int sum = 0;
        this.adj.values().forEach(v -> sum += 1 + v.size());
        return sum;
    }


    boolean haCaminho(String vOrig, String vDest){
        if(!this.adj.constainsKey(vOrig) || !this.adj.constainsKey(vDest))
            return false;
        Set<String> visitados = new HashSet<String>();
        visitados.add(vOrig);
        List<String> queue = new ArrayList<String>();
        queue.add(vOrig);
        for(String v = vOrig; !queue.isEmpty(); v = queue.get(0)){
            if(v.equals(vDest))
                return true;
            this.adj.get(v).forEach( newV -> {
                if (!visitdados.contains(newV)){
                    visitados.add(newV);
                    queue.add(newV);
                }
            } );
        }
    }


    Set<Map.Entry<String, String>> fanOut (String v){
        if(!this.adj.containsKey(v))
            return new HashSet<>();
        return this.adj.get(v).entrySet().stream().collect(Collectors.toSet());
    }
  
}



//------------------------------------------------------------------------------------------
// ___ 3 ‾‾‾
//------------------------------------------------------------------------------------------

public  abstract  class  Imovel  implements  Serializable {
    private  String  codImovel;
    private  String  morada;
    private  String  nifProprietario;
    private  double  area;
    private  double  precoBase;

    private  abstract  double  precoDia ();
}


public  class  Apartamento  extends  Imovel {
    private  String  andar;
    private  double  factorQualidade;
    
    public double precoDia(){
        return ((factorQualidade * super().getprecoBase()) + super().getprecoBase());
    }
}


public  class  Moradia  extends  Imovel {
    private  double  areaPrivativa;
    private  double  areaExterior;
}

    
public  class  Bungalow  extends  Imovel {
    private  double  factorQualidade;
    private  double  espessuraParedes;

    public double precoDia(){
        return ((factorQualidade + espessuraParedes)/2 * super.getprecoBase() + super.getprecoBase());
    }
}

    
public  class  Cliente  implements  Serializable {
    private  String  nome;
    private  String  codCliente;
    private  List <Aluguer > meusAlugueres;
}
    
public  class  Aluguer  implements  Serializable {
    private  String  codCliente;
    private  String  codImovel;
    private  LocalDate  dataInicio;
    private  LocalDate  dataFim;
}
    
public  class  POOAirBnB  implements  Serializable {
    private Map <String , Imovel > imoveis;
    private Map <String , Cliente > clientes;...
    
    public void insereImovel(Imovel i) extends ImovelJaExistente{
        if(this.imoveis.KeySet().contains(i.getId())){
            throw new ImovelJaExistente("Imovel ja existente"); 
        }
        else{
            this.imoveis.put(i.getId(),i.clone());
        }
    }

    public double valorTotalAluguerCliente(String codCliente){
        double preco = 0.0; 
        if(this.clientes.KeySet().contains(codCliente)){
            List<Aluguer> alugueres = this.clientes.get(codCliente).getMeusAlugueres();

            for (Aluguer a : alugueres){
                for(Imovel i : this.imoveis.values()){
                    if (i.getcodimovel().equals(a.getcodimovel())){
                        int nrodias = a.getdatafim() - a.getdatainicio();
                        preco += i.precoDia() * nrodias;
                    }
                }
            }
        }
        else{
            throw new ImovelJaExistente("");
        }
        return preco; 
    }

    public List<Cliente> ordena(){
        Comparator<Cliente> comp = (e1,e2) -> e2.valorTotalAluguerCliente() - e1.valorTotalAluguerCliente(); 
        return this.clientes.values().sorted(comp).collect(Collectors(toList()));
    }

    public String clienteMaisGastador(){
        return ordena().get(0);
    }

    public Map<String, Set<String>> clientesPorImovel(){
        Map<String, Set<String>> ret = new HashMap<>(); 
        
        for (Cliente t : this.clientes.values()){
            
        }

        return ret; 
    }
  
}

public ImovelJaExistente extends Exception{
    public ImovelJaExistente(String msg){
        super(msg);
    }
}

```

<br><br>

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/POO/testes)
