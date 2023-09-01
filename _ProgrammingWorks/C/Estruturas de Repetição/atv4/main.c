// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 31/07/23
//
// -----------------------------------------------------------
// 4) Make an algorithm that present a table of equivalence of
//    temperatures in the Celsius scale to Fahrenheit scale.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    float fahrenheit = 0.0;

    for (int i = 0; i < 101; i++) {

        fahrenheit = ((9/5)*i) + 32;
        printf("Celsius - %d ; Fahrenheit - %.1f\n", i, fahrenheit);
    }

    printf("Press any key to continue...");
    getchar();

    return 0;
}
