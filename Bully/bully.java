import java.io.*;
import java.util.Random;
 
class Bully{
    static int numProc;
    static int prioridade[] = new int[100];
    static int status[] = new int[100];
    static int chefe;

    static Random shuffle = new Random();  //Geramos um objeto para os aleatórios
    public static void main(final String args[]) throws IOException {
        
        numProc = shuffle.nextInt(30) + 1;  //Definimos o número de processos aqui
        System.out.println("Teremos " + numProc + " processos."); //Mostramos na tela essa quantidade

        for (int i = 0; i < numProc; i++) {  //Aqui estabelecemos a prioridade e o status
            status[i] = shuffle.nextInt(2);  //status 1 é ativo e status 0 é desativado
            prioridade[i] = shuffle.nextInt(numProc);  //prioridade dos nós
        }

        int bully = shuffle.nextInt(numProc);  //Um nó qualquer pode solicitar o início da eleição
        System.out.println("O nó " + bully + " vai começar a eleição!");

        election(bully);
        System.out.println("O coordenador novo é " + chefe); //quem é o novo coordenador

    }
     
    static void election(int novoLider)
    {
        novoLider = novoLider - 1;
        chefe = novoLider + 1;          //quem iniciou, na primeira execução, depois será o nó eleito

        for (int i = 0; i < numProc; i++)
        {
            if(prioridade[novoLider]<prioridade[i])
            {
                System.out.println("Mensagens foram enviadas de " + (novoLider + 1) + " para " + (i+1) + "!");
                if(status[i] == 1)
                    election(i+1);
            }
        }
    }
}