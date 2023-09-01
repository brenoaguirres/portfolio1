// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 8) Make an algorithm to read three positive numbers and
//    write them in ascending order.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {
    int numberA;
    int numberB;
    int numberC;
    int aux;

    printf("Inform the first number: \n");
    scanf("%d", &numberA);
    fflush(stdin);
    system("cls");

    printf("Inform the second number: \n");
    scanf("%d", &numberB);
    fflush(stdin);
    system("cls");

    printf("Inform the third number: \n");
    scanf("%d", &numberC);
    fflush(stdin);
    system("cls");

    if(numberA > numberB){
        aux = numberA;
        numberA = numberB;
        numberB = aux;
    }

    if(numberB > numberC){
        aux = numberB;
        numberB = numberC;
        numberC = aux;
    }

    if(numberA > numberB){
        aux = numberA;
        numberA = numberB;
        numberB = aux;
    }

    printf("The informed values in ascending order: %d  %d  %d  \n", numberA, numberB, numberC);

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}

