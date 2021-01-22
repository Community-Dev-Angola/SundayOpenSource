package classes;
import java.util.Random;

/************************************************
 * Direitos Autorais (c) 2019-2021. Nurul GC    *
 *
 * Jovem Programador                            *
 * Estudante de Engenharia de Telecomunicações  *
 * Tecnologia de Informação e de Medicina       *
 * Fé Foco Força Paciência                      *
 * Allah no Comando.                            *
 ************************************************/

public class BancoGC{
    public String nomeTitular;
    public float saldo;
    private final Random geradorNum = new Random();
    private final int numeroConta = setNumeroConta(geradorNum);

    private int setNumeroConta(Random gerador) {
        return gerador.nextInt(1000);
    }
    public void depositar(float valor){
        if (this.saldo>=1000000.0 || valor>=1000000.0){System.out.printf("[x] Lamento %s nao lhe e permitido acumular mais de 1.000.000..\n", this.nomeTitular);}
        else {this.saldo += valor;}
    }
    public void levantar(float valor){
        if(this.saldo<valor){System.out.printf("[x] Lamento %s o seu saldo e insuficiente para completar a operacao..\n", this.nomeTitular);}
        else {this.saldo -= valor;}
    }
    public void extrato(){
        System.out.printf("""
%n
***************************************
          EXTRATO  BANCARIO           
  Nome: %s             
  Numero da conta: %d  
  Saldo atual: %f      
***************************************
%n
""", this.nomeTitular, this.numeroConta, this.saldo);
    }
}
