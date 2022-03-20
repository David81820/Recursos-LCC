```Java
//------------------------------------------------------------------------------------------
// ___ 1 ‾‾‾
//------------------------------------------------------------------------------------------

public class PolyAsList{
    List<Double> polinomio; 

    public PolyAsList(List<Double> pol){
        this.polinomio = pol.stream().collect(Collectors.toList());
    }

    public  void   addMonomio(int  grau , double  coef){ 
        int graus = this.polinomio.size(); [1,2,3] = 3
        
        if (grau == graus+1){ grau = 4 
            this.polinomio.add(coef);
        }
        
        if (grau>graus+1){    
            this.polinomio.add(0.0);
            addMonomio(grau+1,coef);
        }
        
        if (grau<=graus){
            for (int n=0;n<graus;n++){
                if (n==grau){
                    double ad = this.polinomio.get(n); 
                    double teste = ad + coef; 
                    this.polinomio.set(n,teste); 
                }
            }
        }
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
                                                                     
}

                                                                     
                                                                     
//------------------------------------------------------------------------------------------
// ___ 2 ‾‾‾
//------------------------------------------------------------------------------------------

import  java.util.Set;
import  java.util.Map;
import  java.util.HashMap;
public  class  Grafo {//  vari ́aveis  de  inst^anciaprivate Map <String , Set <String >> adj;

    private Map <String , Set <String >> adj;
    
    public Grafo(){
        this.adj = new HashMap<>();     
    }

    public Grafo(Map<String, Set<String>> adj){
        this.adj = adj.entryset().stream().collect(Collectors.toMap(e->e.getKey(), e->e.getValue()));
    }

    public void addArco(String vOrig, String vDest){
        Set<String> adjac = this.adj.get(vOrig); 
        adjac.add(vDest);
        this.adj.put(vOrig,adjac);
        Set<String> adjacaux = this.adj.get(vDest); 
        adjac.add(vOrig);
        this.adj.put(vDest,adjacaux);
    }

    public boolean isSink(String v){
        return this.adj.get(v).size()==0;
    }

    public int size(){
        int vertices = this.adj.KeySet().count(); 
    }
  
}



//------------------------------------------------------------------------------------------
// ___ 3 ‾‾‾
//------------------------------------------------------------------------------------------

public  abstract  class  Imovel  implements  Serializable 
{
    private  String  codImovel;
    private  String  morada;
    private  String  nifProprietario;
    private  double  area;
    private  double  precoBase;
    private  abstract  double  precoDia ();
    ...}

public  class  Apartamento  extends  Imovel {
    private  String  andar;
    private  double  factorQualidade;
    
    public double precoDia(){
        return ((factorQualidade * super().getprecoBase()) + super().getprecoBase());
    }
    ...}

public  class  Moradia  extends  Imovel {
    private  double  areaPrivativa;
    private  double  areaExterior;...

}
    
public  class  Bungalow  extends  Imovel {
    private  double  factorQualidade;
    private  double  espessuraParedes;

    public double precoDia(){
        return ((factorQualidade + espessuraParedes)/2 * super.getprecoBase() + super.getprecoBase());
    }

    ...}
    
public  class  Cliente  implements  Serializable {
    private  String  nome;
    private  String  codCliente;
    private  List <Aluguer > meusAlugueres;...}
    
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
