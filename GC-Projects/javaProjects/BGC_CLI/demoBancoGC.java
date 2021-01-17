import java.util.Scanner;
import classes.BancoGC;

/************************************************
 * Direitos Autorais (c) 2019-2021. Nurul GC    *
 *
 * Jovem Programador                            *
 * Estudante de Engenharia de Telecomunicações  *
 * Tecnologia de Informação e de Medicina       *
 * Fé Foco Força Paciência                      *
 * Allah no Comando.                            *
 ************************************************/

public class demoBancoGC extends BancoGC{
    public static void main(String[] args){
        BancoGC novaConta = new BancoGC();
        Scanner input = new Scanner(System.in);

        System.out.printf("""
%n
***************************************************************************
*                        *** BancoGC ***                                  *
*                                                                         *
*                        Ola caro cliente                                 *
*   Nos temos o prazer de oferecer-lhe a oportunidade                     *
*   de criar diversos planos com seu dinheiro.                            *
*   Sem ter que se preocupar com dividas ou contas para pagar.            *
*   Todas as contas criadas em nosso banco sao do tipo poupanca           *
*   facilitando entao a estabilidade e crescimento economico do cliente   *
*                                                                         *
*   Vamos iniciar o nosso processo de cadastro..                          *
***************************************************************************
""");
        System.out.println("\nDigite o seu nome:");
        System.out.print("> ");
        novaConta.nomeTitular = input.nextLine();

        System.out.println("Digite o valor a depositar:");
        System.out.print("> ");
        novaConta.saldo = input.nextFloat();

        if(!novaConta.nomeTitular.equals("") && novaConta.saldo!=0.0){
            System.out.println("\nParabens "+novaConta.nomeTitular+" a sua conta foi criada com sucesso..");
            System.out.printf("""
%n
*********************************************************
* Para ter acesso aos seus dados use os digitos chaves: *
* [1] - EXTRATO;                                        *
* [2] - DEPOSITAR;                                      *
* [3] - LEVANTAR;                                       *
* [s] - SAIR;                                           *
*********************************************************
""");
            do {
                String acesso = input.nextLine();

                if (acesso.equals("1")) {
                    novaConta.extrato();
                }
                if (acesso.equals("2")) {
                    System.out.println("\nDigite o valor a depositar: ");
                    System.out.print("> ");
                    float deposito = input.nextFloat();
                    novaConta.depositar(deposito);
                    continue;
                }
                if (acesso.equals("3")) {
                    System.out.println("\nDigite o valor a levantar: ");
                    System.out.print("> ");
                    float levantamento = input.nextFloat();
                    novaConta.levantar(levantamento);
                    continue;
                }
                if (acesso.equals("s")){
                    System.out.println("\nObrigado pela preferencia..\nTerminando o programa!");
                    System.exit(0);
                }
                System.out.println("\n*** [1]-[2]-[3]-[s] ***");
                System.out.print("> ");
            } while (true);
        }
    }
}
