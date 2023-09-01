// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 25) Make a program for an ATM. The program should ask the user
//     for the value of the withdrawal and then inform how many
//     bills of each value will be provided. Available bills are
//     1, 5, 10, 50 and 100. Max value of withdrawal of $600.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    int withdrawal;
    int bills1;
    int bills5;
    int bills10;
    int bills50;
    int bills100;

    printf("Welcome to the IFG ATM! Please insert the value of the withdrawal: (Max $600)\n");
    scanf("%d", &withdrawal);
    fflush(stdin);
    system("cls");

    if (withdrawal <= 600) {
        bills100 = withdrawal / 100;
        bills50 = (withdrawal - bills100 * 100) / 50;
        bills10 = ((withdrawal - bills100 * 100) - bills50 * 50) / 10;
        bills5 = (((withdrawal - bills100 * 100) - bills50 * 50) - bills10 * 10) / 5;
        bills1 = ((((withdrawal - bills100 * 100) - bills50 * 50) - bills10 * 10) - bills5 * 5);

        printf("Bank Statement\n");
        printf("---------------\n");
        printf("%d bills of 100\n", bills100);
        printf("%d bills of 50\n", bills50);
        printf("%d bills of 10\n", bills10);
        printf("%d bills of 5\n", bills5);
        printf("%d bills of 1\n", bills1);
        printf("----------------\n");
        printf("Total value: %d\n", withdrawal);
    }
    else {
        printf("Exceeded max withdrawal value.\n");
    }

    printf("Press any key to continue...");
    getchar();

    return 0;
}
