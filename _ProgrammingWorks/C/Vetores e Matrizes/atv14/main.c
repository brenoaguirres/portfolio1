// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 26/08/23
//
// -----------------------------------------------------------
// 14) Write an algorithm that reads two arrays x[10] and y[10].
//     Create then a z array which will be:
//     a - The difference between x and y.
//     b - The sum between x and y.
//     c - The product of x and y.
//     Write the array z at each calculation.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 10

int main()
{
    int x[MAX_SIZE], y[MAX_SIZE], z[MAX_SIZE];

    for(int i = 0; i < MAX_SIZE; i++) {
        printf("Please insert the %d value:\n", i+1);
        scanf("%d", &x[i]);
        while(getchar() != '\n');
        system("cls");
    }

    for(int i = 0; i < MAX_SIZE; i++) {
        printf("Please insert the %d value:\n", i+1);
        scanf("%d", &y[i]);
        while(getchar() != '\n');
        system("cls");
    }

    printf("Difference of the arrays:\n");
    for(int i = 0; i < MAX_SIZE; i++) {
        z[i] = x[i] - y[i];
        printf("%d  ", z[i]);
    }
    printf("\n\n");

    printf("Sum of the arrays:\n");
    for(int i = 0; i < MAX_SIZE; i++) {
        z[i] = x[i] + y[i];
        printf("%d  ", z[i]);
    }
    printf("\n\n");

    printf("Product of the arrays:\n");
    for(int i = 0; i < MAX_SIZE; i++) {
        z[i] = x[i] * y[i];
        printf("%d  ", z[i]);
    }
    printf("\n\n");

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
