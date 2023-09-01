// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 21/08/23
//
// -----------------------------------------------------------
// 7) Create an algorithm that reads 30 values and split them in
//    two arrays if they're even or odd. The max size of the
//    array is five positions, if they're full - write them. Each
//    array can be filled as many times as needed.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main()
{

    int arr[30], evn_arr[5], odd_arr[5], evn_cnt = 0, odd_cnt = 0;

    for(int i = 0; i < 30; i++) {
        printf("Please insert the %d number:\n", i+1);
        scanf("%d", &arr[i]);
        while(getchar() != '\n');
        system("cls");
    }

    for(int i = 0; i < 30; i++) {
        // check if arrays are full and print 'em
        if(evn_cnt == 5) {
            for (int j = 0; j < 5; j++) {
                printf("%d\t", evn_arr[j]);
            }
            evn_cnt = 0;
            printf("\n");
        }
        else if(odd_cnt == 5) {
            for (int j = 0; j < 5; j++) {
                printf("%d\t", odd_arr[j]);
            }
            odd_cnt = 0;
            printf("\n");
        }

        // assign numbers to arrays
        if (arr[i] % 2 == 0) {
            evn_arr[evn_cnt] = arr[i];
            evn_cnt += 1;
        }
        else {
            odd_arr[odd_cnt] = arr[i];
            odd_cnt += 1;
        }
    }

    if (evn_cnt != 0) {
        for (int i = 0; i < evn_cnt; i++) {
            printf("%d\t", evn_arr[i]);
        }
        evn_cnt = 0;
        printf("\n");

    }

    if (odd_cnt != 0) {
        for (int i = 0; i < odd_cnt; i++) {
            printf("%d\t", odd_arr[i]);
        }
        odd_cnt = 0;
        printf("\n");
    }

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
