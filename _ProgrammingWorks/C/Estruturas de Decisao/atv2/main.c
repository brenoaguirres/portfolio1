// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 2) Make an algorithm to read an integer and tell if the
//    number is odd or even.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    int number1;

    printf("Insert the first number: \n");
    scanf("%d", &number1);
    fflush(stdin);
    system("cls");

    if ((number1 % 2) == 0) {
        printf("THE INFORMED NUMBER IS EVEN!!\n");
    }
    else {
        printf("THE INFORMED NUMBER IS ODD!!\n");
    }

    getchar();

    return 0;
}
