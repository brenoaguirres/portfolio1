// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 31/07/23
//
// -----------------------------------------------------------
// 3) Make an algorithm that prints the powers of 2, from 2^0
//    to 2^10.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {

    for (int i = 0; i < 11; i++) {
        printf("2^%d = %d\n", i, pow(2, i));
    }

    printf("Press any key to continue...");
    getchar();

    return 0;
}
