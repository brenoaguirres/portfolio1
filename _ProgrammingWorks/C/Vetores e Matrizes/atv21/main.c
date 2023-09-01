// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 27/08/23
//
// -----------------------------------------------------------
// 21)Make an algorithm that reads an array of 10 positions. Then,
//    show the 3 minor values of the array.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

#define MAX_VALUE 10
#define MINOR_VALUES 3

int main()
{
    int pos[MAX_VALUE], min[MINOR_VALUES], count = 0, hasInitialized = 0, aux;

    for(int i = 0; i < MAX_VALUE; i++) {
        printf("Please insert the %d number:\n", i+1);
        scanf("%d", &pos[i]);
        while(getchar() != '\n');
        system("cls");

        if(hasInitialized == 0) {
            min[i] = pos[i];
            for(int j = 0; j < MINOR_VALUES; j++) {
                if(min[j] > min[i]) {
                    aux = min[i];
                    min[i] = min[j];
                    min[j] = aux;
                    break;
                }
            }

            count++;
            if(count == MINOR_VALUES) {
                hasInitialized = 1;
            }
        }

        for(int j = 0; j < MINOR_VALUES; j++) {
            if(pos[i] < min[j]) {
                min[j] = pos[i];
                break;
            }
        }
        printf("--------------------------------------\nDEBUGLOG\n");
        printf("hasInitialized = %d\n", hasInitialized);
        for(int f = 0; f < MAX_VALUE; f++) {
            printf("pos[%d] = %d\n", f, pos[f]);
        }
        for(int f = 0; f < MINOR_VALUES; f++) {
            printf("min[%d] = %d\n", f, min[f]);
        }
        printf("--------------------------------------\n\n");

    }

    printf("Minor values informed:\n");
    for(int i = 0; i < MINOR_VALUES; i++) {
        printf("%d  ", min[i]);
    }
    printf("\n\n");

    printf("Press any key to continue...");
    getchar();

    return 0;
}
