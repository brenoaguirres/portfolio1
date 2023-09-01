// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 27/08/23
//
// -----------------------------------------------------------
// 17) Make an algorithm that reads two arrays of 200 positions
//     of characters. Following, swap the first element of
//     A with the 200th element of B, the 2nd of A with the 199th
//     of B. Show the arrays before and after.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 200

int main()
{
    char A[MAX_SIZE], B[MAX_SIZE], aux[MAX_SIZE];

    for(int i = 0; i < MAX_SIZE; i++) {
        printf("Please inform the %d value of A:\n", i+1);
        scanf("%c", &A[i]);
        while(getchar() != '\n');
        system("cls");
    }

    for(int i = 0; i < MAX_SIZE; i++) {
        printf("Please inform the %d value of B:\n", i+1);
        scanf("%c", &B[i]);
        while(getchar() != '\n');
        system("cls");
    }

    printf("First array:\n");
    for(int i = 0; i < MAX_SIZE; i++) {
        printf("%c  ", A[i]);
    }
    printf("\n\n");

    printf("Second array:\n");
    for(int i = 0; i < MAX_SIZE; i++) {
        printf("%c  ", B[i]);
    }
    printf("\n\n");

    //Swapping the arrays
    for(int i = 0; i < MAX_SIZE; i++) {
        aux[i] = A[i];
        A[i] = B[(MAX_SIZE - 1) - i];
        B[(MAX_SIZE - 1) - i] = aux[i];
    }

    printf("First swapped array:\n");
    for(int i = 0; i < MAX_SIZE; i++) {
        printf("%c  ", A[i]);
    }
    printf("\n\n");

    printf("Second swapped array:\n");
    for(int i = 0; i < MAX_SIZE; i++) {
        printf("%c  ", B[i]);
    }
    printf("\n\n");

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
