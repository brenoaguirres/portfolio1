// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 26/08/23
//
// -----------------------------------------------------------
// 15) Write an algorithm that reads an array k[15] of positive
//     numbers. Create then an array p, which will contain all
//     prime numbers of k. Write p.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 15

int main()
{
    int k[MAX_SIZE], p[MAX_SIZE], count = 0;

    for(int i = 0; i < MAX_SIZE; i++) {
        printf("Please insert the %d number:\n", i+1);
        scanf("%d", &k[i]);
        while(getchar() != '\n');
        system("cls");
    }

    for(int i = 0; i < MAX_SIZE; i++) {
        int num = k[i];
        //checking if number is prime
        if (num <= 1) {
            continue;
        }

        int ctrlVar = 1;
        for (int j = 2; j * j <= num; j++) {
            if (num % j == 0) {
                ctrlVar = 0;
            }
        }
        if (ctrlVar == 0) {
            continue;
        }

        // if loop wasn't skipped 'til here, then it's prime.
        p[count] = num;
        count++;
    }

    printf("Prime numbers:\n");
    for(int i = 0; i < count; i++) {
        printf("%d  ", p[i]);
    }
    printf("\n\n");

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
