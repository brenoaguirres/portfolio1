// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 27/08/23
//
// -----------------------------------------------------------
// 18) Make an algorithm that reads a numeric code and an array
//     of 50 positions. If the code is 0, exit the program. If it
//     is 1, display the array normally, if its 2, display the array
//     inverted.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 50

int main()
{
    int arr[MAX_SIZE], code, aux[MAX_SIZE];

    for(int i = 0; i < MAX_SIZE; i++) {
        printf("Please inform the %d number:\n", i+1);
        scanf("%d", &arr[i]);
        while(getchar() != '\n');
        system("cls");
    }

    printf("Please inform the numeric keycode:\n0 - Exit\n1 - Display\n2 - Inversion\n\n");
    scanf("%d", &code);
    while(getchar() != '\n');
    system("cls");

    switch(code) {
    case 0:
        printf("Exiting program...\n");
        break;
    case 1:
        for(int i = 0; i < MAX_SIZE; i++) {
            printf("%d  ", arr[i]);
        }
        break;
    default:
        for(int i = 0; i < MAX_SIZE; i++) {
            aux[i] = arr[i];
        }
        for(int i = 0; i < MAX_SIZE; i++) {
            arr[i] = aux[(MAX_SIZE - 1) - i];
            printf("%d  ", arr[i]);
        }
        break;
    }
    printf("\n\n");

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
