// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 4) Make an algorithm to read two integers variables, and
//    guarantee that A and B stays in ascending order, i.e.
//    the variable A must store the lower value and the variable
//    B must store the highest.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    int numberA;
    int numberB;
    int aux;

    printf("Insert the first number: \n");
    scanf("%d", &numberA);
    fflush(stdin);
    system("cls");

    printf("Insert the second number: \n");
    scanf("%d", &numberB);
    fflush(stdin);
    system("cls");

    if (numberA > numberB) {
        aux = numberA;
        numberA = numberB;
        numberB = aux;
    }

    printf("The higher number is B: %d and the lower is A: %d.\n", numberB, numberA);

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}

