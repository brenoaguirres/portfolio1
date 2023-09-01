// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 3) Make an algorithm to read two integers A and B and tell
//    if A is divisible by B.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    int numberA;
    int numberB;

    printf("Insert the first number: \n");
    scanf("%d", &numberA);
    fflush(stdin);
    system("cls");

    printf("Insert the second number: \n");
    scanf("%d", &numberB);
    fflush(stdin);
    system("cls");

    if ((numberA % numberB) == 0) {
        printf("The second number divides the first one.\n");
    }
    else {
        printf("The second number doesn't divides the first one.\n");
    }

    getchar();

    return 0;
}
