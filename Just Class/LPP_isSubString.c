#include <stdio.h>

int show(char* string, char* sub);

int main (){
    char string[30], sub[30];
    int result;

fgets(string, 30, stdin);
fgets(sub, 30, stdin);

result = show(string,sub);

if (result == -1){
    printf("Não é substring!\n");
}
else if (result == 1){
    printf("É substring!\n");
}


return 0;
}

int show(char* string, char* sub){
    int i = 0, j = 0;
    int ind;

    while (string[i] != '\0') {
        while (string[i] != sub[0] && string[i] != '\0') i++;
        if (string[i] == '\0') return (-1);
    
        ind = i;
    
        while (string[i] == sub[j] && string[i] != '\0' && sub[j] != '\0') {
            i++;
            j++;
        }

    if (sub[j] == '\0') return 1;
    else if (string[i] == '\0') return -1;

    i = ind + 1;
    j = 0;
    }
}