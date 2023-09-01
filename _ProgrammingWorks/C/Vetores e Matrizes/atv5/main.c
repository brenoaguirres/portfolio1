// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 21/08/23
//
// -----------------------------------------------------------
// 5) Make an algorithm that reads and shows an input array of
//    20 numbers. Count how many even values exist in the vector.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int arr[20], count = 0;

    for(int i = 0; i < 20; i++) {
        printf("Please insert the %d number:\n", i+1);
        scanf("%d", &arr[i]);
        fflush(stdin);
        system("cls");

        if(arr[i] % 2 == 0) {
            count++;
        }
    }

    printf("There are %d even numbers contained in the array\n", count);

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
