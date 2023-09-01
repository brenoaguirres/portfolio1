// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 21/08/23
//
// -----------------------------------------------------------
// 8) Write an algorithm that reads an array of 20 positions
//    and show it. Then, swap the first element with the last
//    one, the second with the last but one, and so on. Show
//    the new array on screen after the exchange.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int arr_Size = 20;
    int arr[arr_Size], aux;

    for(int i = 0; i < arr_Size; i++) {
        printf("Please insert the %d number:\n", i+1);
        scanf("%d", &arr[i]);
        while (getchar() != '\n');
        system("cls");
    }

    for(int i = 0; i < (arr_Size / 2); i++) {
        aux = arr[i];
        arr[i] = arr[(arr_Size-1)-i];
        arr[(arr_Size-1)-i] = aux;
    }

    printf("New array:\n");
    for(int i = 0; i < arr_Size; i++) {
        printf("%d  ", arr[i]);
    }
    printf("\n");

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
