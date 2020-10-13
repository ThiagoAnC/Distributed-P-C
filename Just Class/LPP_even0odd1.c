#include <stdio.h>

int show(int);

int main(void){
    unsigned int number = 0;
    int bol;
scanf("%u", &number);
    bol = show(number);
    if (bol == 0) {
        printf("%u",number);
        printf("0\n");
    }
    else if (bol == 1) {
        printf("%u",number);
        printf("1\n");
    }
return 0;
}

int show (int a){
    unsigned int aux, tam, soma;
    soma = tam = 0;
    aux = a;
    do {
        tam = tam + 1;
        soma = soma + aux%10;
        aux = aux / 10;
    }while (aux != 0);

    if (soma % 2 == 0){
        return 0;
    }
    else {
        return 1;
    }
}