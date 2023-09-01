// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 27/08/23
//
// -----------------------------------------------------------
// 16) Write an algorithm that reads an array x[20], and then
//     write each different value that appears in x saying
//     how many times each value appears in x.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 20

int main()
{
    int x[MAX_SIZE], uniqueValues[MAX_SIZE], repetitions[MAX_SIZE], count = 0;

    // input values to x, put x values just one time within unique values
    // count variable stores size of uniqueValues and repetitions arrays
    for(int i = 0; i < MAX_SIZE; i++) {
        printf("Please inform the %d value:\n", i+1);
        scanf("%d", &x[i]);
        while(getchar() != '\n');
        system("cls");


        if (i == 0) {
            uniqueValues[i] = x[i];
            count++;
        }
        else {
            int contains = 1; // 1 - not contained ----- 0 - contained
            for(int j = 0; j < i; j++) {
                if(x[i] == uniqueValues[j]) {
                    contains = 0;
                }
            }
            if (contains == 1) {
                uniqueValues[count] = x[i];
                count++;
            }
        }
    }

    //fill repetitions with ones up to count
    for(int i = 0; i < count; i++) {
        repetitions[i] = 0;
    }

    //compare each uniqueValues to each x value and if its within, add one to the corresponding repetitions
    for(int i = 0; i < count; i++) {
        for(int j = 0; j < MAX_SIZE; j++) {
            if(uniqueValues[i] == x[j]) {
                repetitions[i] += 1;
            }
        }
    }

    //print quantities
    printf("-----------------------------------------------------------------------------\n");
    for(int i = 0; i < count; i++) {
        printf("Number: %d\nQuantity: %d\n\n", uniqueValues[i], repetitions[i]);
    }
    printf("-----------------------------------------------------------------------------\n");

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
