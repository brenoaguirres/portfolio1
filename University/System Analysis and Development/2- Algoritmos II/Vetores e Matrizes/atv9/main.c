// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 21/08/23
//
// -----------------------------------------------------------
// 9) Write an algorithm that reads 5 values for a 5 position
//    array. Show only the positive numbers.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 5

int main()
{

    int arr[MAX_SIZE];

    for(int i = 0; i < MAX_SIZE; i++) {
        printf("Please insert the %d number.\n", i+1);
        scanf("%d", &arr[i]);
        while (getchar() != '\n');
        system("cls");
    }

    printf("Positive numbers inside the array:\n");
    for(int i = 0; i < MAX_SIZE; i++) {
        if (arr[i] > 0) {
            printf("%d  ", arr[i]);
        }
    }
    printf("\n");

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
