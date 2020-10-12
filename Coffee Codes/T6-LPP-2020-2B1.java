import java.util.Random;

class Main
{
	public static void main (String[] args)
	{
        int var = 10;
        int[][] vet;

        vet = new int[3][3];

        calc(var,3,2);
        arr(vet, 3);

    }
    public static void calc(int var, int mult, int div) {
        int result = var+30;
        System.out.println("The sum is: " + result);
        System.out.println("The multiplication is: " + var*mult);
        System.out.println("The division is: " + var/div);       
    }
    public static void arr(int[][] vetor, int tam){
        Random r = new Random();
        for (int i = 0; i < tam; i++){
            for (int n = 0; n < tam; n++){
                vetor[i][n] = r.nextInt(10);
                System.out.print(vetor[i][n] + " ");
            }
        System.out.println();
        }
    }
}