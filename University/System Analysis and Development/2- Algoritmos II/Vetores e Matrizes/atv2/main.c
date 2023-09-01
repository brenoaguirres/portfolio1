// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 21/08/23
//
// -----------------------------------------------------------
// 2) Make an algorithm that reads two arrays of 10 positions and
//    multiply the elements of same index, inserting the result
//    in a third array. Show the resulting array.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int firstArray[10], secondArray[10], resultArray[10];

    for (int i = 0; i < 20; i++) {
        if (i < 10) {
            printf("Insert the %d number of the %d array:\n", i+1, 1);
            scanf("%d", &firstArray[i]);
        }
        else {
            printf("Insert the %d number of the %d array:\n", (i+1 -10), 2);
            scanf("%d", &secondArray[i-10]);
        }
    }

    for (int i = 0; i < 10; i++) {
        resultArray[i] = firstArray[i] * secondArray[i];
        printf("%d multiplication = %d.\n", i+1, resultArray[i]);
    }

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
