// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 21/08/23
//
// -----------------------------------------------------------
// 3) Make an algorithm that reads an array K[30]. Then, exchange
//    all the odd elements with the following element if its an
//    even number.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int k[30], aux;

    for (int i = 0; i < 30; i++) {
        printf("Please insert the %d number of the k array:\n", i+1);
        scanf("%d", &k[i]);
    }

    for (int i = 0; i < 30; i++) {
        if (i < 29) {
            if (k[i]%2 != 0 && k[i+1]%2 == 0) {
                aux = k[i];
                k[i] = k[i+1];
                k[i+1] = aux;
                i++;
                continue;
            }
        }
    }

    for (int i = 0; i < 30; i++) {
        printf("%d ", k[i]);
    }
    printf("\n");

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
