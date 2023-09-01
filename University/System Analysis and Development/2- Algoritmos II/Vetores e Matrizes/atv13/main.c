// Instituto Federal de Goiás - IFG
// Atividade de Algoritmos II
// Breno Aguirres ; Henrique Herrmann; David Daves
// __________________________________

//13) Escrever um algoritmo que lê 2 vetores de tamanho 10. Crie, a seguir, um vetor
//S de 20 posições que contenha os elementos dos outros 2 vetores em ordem
//crescente. Obs.: copie primeiro os valores para o vetor S para depois ordena-los.

#include <stdio.h>
#include <stdlib.h>

int main()
{

    int vet1[10], vet2[10];
    int S[20];
    int i, j, aux; // para indices e auxiliar
    int isOrdered = 0;

    for(i=0; i<10; i++) {
        printf("Digite o %d numero do vetor 1:\n", i+1);
        scanf("%d", &vet1[i]);
        fflush(stdin);
        system("cls");
    }

    for(i=0; i<10; i++) {
        printf("Digite o %d numero do vetor 2:\n", i+1);
        scanf("%d", &vet2[i]);
        fflush(stdin);
        system("cls");
    }

    for(i=0; i<20; i++) {
        if (i<10) {
            S[i] = vet1[i];
        }
        else {
            S[i] = vet2[i-10];
        }
    }

    for(j = 0; j < 20; j++) {
        for(i = 0; i < 19; i++) {
            if (S[i] > S[i+1]) {
                aux = S[i];
                S[i] = S[i+1];
                S[i+1] = aux;
                isOrdered = 1;
            }
        }

        if(isOrdered == 0) {
            break;
        }
        isOrdered = 0;
    }

    printf("Vetor S em ordem crescente: \n");
    for(i = 0; i < 20; i++) {
        printf("%d ", S[i]);
    }


    printf("\nPress any key to continue...");
    getchar();

    return 0;
}
