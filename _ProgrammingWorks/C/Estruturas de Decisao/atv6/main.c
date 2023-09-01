// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 6) Make an algorithm to test if an inserted password equals
//    to "eh4nois". If it is correct, print "Access Granted.",
//    otherwise, print the message "You do not have access to
//    this system.".
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    char password[50];

    printf("Insert the password: \n");
    scanf("%s", &password);
    fflush(stdin);
    system("cls");

    if (strcmp(password, "eh4nois") == 0) {
        printf("Access granted.\n");
    }
    else {
        printf("You do not have access to this system.\n");
    }

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}

