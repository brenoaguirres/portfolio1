// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 27/08/23
//
// -----------------------------------------------------------
// 19) Make an algorithm that reads an array A of 10 positions.
//     Then, compact the array, removing null and negative values
//     by putting them in a 2nd vector B.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 10

int main()
{
    int A[MAX_SIZE], B[MAX_SIZE], count = 0;

    for(int i = 0; i < MAX_SIZE; i++) {
        printf("Please inform the %d number:\n", i+1);
        scanf("%d", &A[i]);
        while(getchar() != '\n');
        system("cls");

        if(A[i] >= 1) {
            B[count] = A[i];
            count++;
        }
    }

    printf("Compacted vector:\n");
    for(int i = 0; i < count; i++) {
        printf("%d  ", B[i]);
    }
    printf("\n\n");

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
