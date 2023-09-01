// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 21/08/23
//
// -----------------------------------------------------------
// 6) Write an algorithm that reads an array of 10 positions and
//    show it sorted by ascending order.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main()
{

    int arr[10], aux, isSorted = 1;

    for(int i = 0; i < 10; i++) {
        printf("Please insert the %d number:\n", i+1);
        scanf("%d", &arr[i]);
        while (getchar() != '\n');
        system("cls");
    }

    for(int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (arr[j] > arr[j+1]) {
                aux = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = aux;

                isSorted = 0;
            }
        }

        if (isSorted == 1) {
            break;
        }
        isSorted = 1;
    }

    printf("Sorted array:\n");
    for(int i = 0; i < 10; i++) {
        printf("%d ", arr[i]);
    }

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
