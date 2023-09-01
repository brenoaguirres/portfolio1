// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 21/08/23
//
// -----------------------------------------------------------
// 10) Write an algorithm that reads an array of 30 positions
//     and create a second array that changes the null values by
//     1. Show both arrays.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 30

int main()
{
    int arr[MAX_SIZE], arr_notnull[MAX_SIZE];

    for(int i = 0; i < MAX_SIZE; i++) {
        printf("Please insert the %d number:\n", i+1);
        scanf("%d", &arr[i]);
        while(getchar() != '\n');
        system("cls");

        if (arr[i] == NULL || arr[i] == 0) {
            arr_notnull[i] = 1;
        }
        else {
            arr_notnull[i] = arr[i];
        }
    }

    printf("Corrected Array:\n");
    for(int i = 0; i < MAX_SIZE; i++) {
        printf("%d  ", arr_notnull[i]);
    }
    printf("\n");

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
