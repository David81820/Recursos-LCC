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
        this.adj = adj.entryset().stream().collect(Collectors.toMap(e->e.getKey(), e->new HashSet<String>(e.getValue())));
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


////////////////////////////////////////////////////////////////////////////////////////////////
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

//          OU

    public boolean haCaminho(String vOrig, String vDest){
        if(!this.adj.constains(vOrig) || !this.adj.constainsKey(vDest))
            return false;
        return haCaminhoAux(vOrig, vDest, new HashSet<String>());
    }

    public boolean haCaminhoAux(String vOrig, String vDest, Set<String>){
        if(vOrig.equals(vDest)
            return true;
        visitados.add(vOrig);
        for(String v : adj.get(vOrig)){
            if(!visitados.contains(v) && (haCaminho(v, vDest))
                return true;
        }
    }
//////////////////////////////////////////////////////////////////////////////////////////


    public Set<Map.Entry<String, String>> fanOut (String v){
        if(!this.adj.containsKey(v))
            return new HashSet<>();
        return this.adj.get(v).entrySet().stream().collect(Collectors.toSet());
    }
  
}



//------------------------------------------------------------------------------------------
// ___ 3 ‾‾‾
//------------------------------------------------------------------------------------------

import java.util.*;
import java.time.*;

public abstract class Imovel implements Serializable {
	private String codImovel ;
	private String morada ;
	private String nifProprietario ;
	private double area ;
	private double precoBase ;
	
	private abstract double precoDia ();
	
	...
}


public class Apartamento extends Imovel {
	private String andar ;
	private double factorQualidade ;
	
	...
	
	public double precoDia(){
		return (1 + this.factorQualidade) * super.getPrecoBase();
	}
}


public class Moradia extends Imovel {
	private double areaPrivativa ;
	private double areaExterior ;
	
	...
	
	public double precoDia(){
		return super.getPrecoBase() * ((this.areaPrivativa * 0.3) + (this.areaExterior * 0.7));
	}
}


public class Bungalow extends Imovel {
	private double factorQualidade ;
	private double espessuraParedes ;
	
	...
	
	public double precoDia(){
		return super.getPrecoBase * ((this.factorQualidade + this.espessuraParedes)*0.5);
	}
}


public class Cliente implements Serializable {
	private String nome ;
	private String codCliente ;
	private List<Aluguer> meusAlugueres ;
	
	...
}


public class Aluguer implements Serializable {
	private String codCliente ;
	private String codImovel ;
	private LocalDate dataInicio ;
	private LocalDate dataFim ;
	
	...
}


public class POOAirBnB implements Serializable {
	private Map<String, Imovel> imoveis ;
	private Map<String, Cliente> clientes ;
	
	...
	
	public void insereImovel(Imovel i) extends ImovelJaExistente{
		if(this.imoveis.constainsKey(i.getCodImovel()))
			throw new ImovelJaExistente();
		else
			this.imoveis.put(i.getCodImovel(), i.clone());
	}
	
	public double valorTotalAluguerCliente(String codCliente){
		if(!this.clientes.containsKey(codCliente))
			return 0;
		double sum = 0.0;
		List<Aluguer> als = this.clientes.get(codCliente).getMeusAlugueres();
		for(Aluguer a : als){
			int dias = Period.between(a.getDataInicio(), a.getDataFim());
			dias = Math.abs(dias);
			sum += dias * this.imoveis.get(a.getCodImovel()).precoDia();
		}
		return sum;
	}
	
	public String clienteMaisGastador(){
		if(this.clientes.isEmpty())
			return null;
		return this.clientes.values().stream().sorted( (a,b) -> this.valorTotalAluguerCliente(a.getNome()) - this.valorTotalAluguerCliente(b.getNome()) ).findFirst().get().getNome();
	}
	
	public Map<String, Set<String>> clientesPorImovel(){
	
	/// Método 1
		Map<String, Set<String>> res = new HashMap<>();        
        for (Cliente t : this.clientes.values()){
            
        }
        return res; 
	
	
	/// Método 2
		return clientes.values()
				   .stream()
				   .map(Cliente::getMeusAlugueres)
				   .flatMap(List::stream)
				   .collect(
				   		groupingBy(Aluguer::getCodImovel, mapping(Aluguer::getCodCliente, toSet())));
	}
}

public class ImovelJaExistente extends Exception{
	public ImovelJaExistente(){ super(); }
	public ImovelJaExistente(String msg){ super(msg); }
}

```

<br><br>

[![retroceder]({{ '/assets/images/Rewind.png' | relative_url }})](https://david81820.github.io/Recursos-LCC/POO/testes)
