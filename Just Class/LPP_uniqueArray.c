#include <stdio.h>
#include <stdlib.h>

int show(int* vet, int tam);

int main(){
int *vet;
int i,n,result;

scanf("%i",&n);

    vet = malloc(n * sizeof(int));
    for (i = 0; i < n; i++){
        scanf("%i",&vet[i]);
    }
    printf("%d\n",show(vet,n));
return 0;
}

int show(int* vet, int tam){
    int i,j, cont, flag;
    cont = 0;
    flag = 0;

    for (i = 0; i < tam; i++){
        for (j = 0; j < tam; j++){
            if (vet[i] == vet[j]){
                flag += 1;
            }
        }
        if (flag == 1||flag == 0){
            cont += 1;
        }
        flag = 0;
    }
return (cont);
}