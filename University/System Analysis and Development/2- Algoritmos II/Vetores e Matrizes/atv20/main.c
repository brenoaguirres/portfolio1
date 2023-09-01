// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 27/08/23
//
// -----------------------------------------------------------
// 20) Make an algorithm that reads a array of 50 positions, then
//     divide all elements by the largest value of the array. Show
//     the array after the calculations.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

#define MAX_VALUE 5

int main()
{
    float vecValues[MAX_VALUE], largestVal = 0;

    for(int i=0; i < MAX_VALUE; i++) {
        printf("Press insert the %d number:\n", i+1);
        scanf("%f", &vecValues[i]);
        while (getchar() != '\n');
        system("cls");

        if (i == 0) {
            largestVal = vecValues[i];
        }
        else {
            if (largestVal < vecValues[i]) {
                largestVal = vecValues[i];
            }
        }
    }

    printf("Values divided by largest value sent:\n");
    for(int i = 0; i < MAX_VALUE; i++) {
        vecValues[i] /= largestVal;
        printf("%.2f  ", vecValues[i]);
    }
    printf("\n\n");


    printf("Press any key to continue...");
    getchar();

    return 0;
}
