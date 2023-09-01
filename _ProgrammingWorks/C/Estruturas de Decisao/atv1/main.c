// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II---
// 29/07/23
//
// -----------------------------------------------------------
// 1) Make an algorithm to read two integers and tell if these
// numbers are equal or different.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    int number1;
    int number2;

    printf("Insert the first number: \n");
    scanf("%d", &number1);
    system("cls");
    fflush(stdin);
    printf("Insert the second number: \n");
    scanf("%d", &number2);
    fflush(stdin);
    system("cls");

    if (number1 == number2) {
        printf("The numbers are equal.");
    }
    else {
        printf("The numbers are different.");
    }

    getchar();
}
