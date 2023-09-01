// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 21/08/23
//
// -----------------------------------------------------------
// 1) Make an algorithm that reads an array N[20]. Then, find
//    the lower element from N and it's position inside the array
//    finally print it onscreen.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n[20];
    int lowerElement, lowerPosition, isFirstRun = 0;

    for(int i = 0; i < 20; i++) {
        printf("Please insert the %d number:\n", i+1);
        scanf("%d", &n[i]);
        fflush(stdin);
        system("cls");

        if (isFirstRun == 0) {
            lowerElement = n[i];
            lowerPosition = i;
            isFirstRun = 1;
        }
        else if (n[i] < lowerElement) {
            lowerElement = n[i];
            lowerPosition = i;
        }
    }

    printf("Lower inserted element is %d at position %d\n", lowerElement, lowerPosition + 1);

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
