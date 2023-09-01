// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 10) Make an algorithm that will say if an inserted number
//     is between the interval [20, 90].
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    int number;

    printf("Please insert a number: \n");
    scanf("%d", &number);
    fflush(stdin);
    system("cls");

    if (number > 19 && number < 91) {
        printf("Your number is in the interval of 20 to 90.\n");
    }
    else {
        printf("Your number is not in the interval of 20 to 90.\n");
    }

    printf("Press any key to continue...");
    getchar();

    return 0;
}
