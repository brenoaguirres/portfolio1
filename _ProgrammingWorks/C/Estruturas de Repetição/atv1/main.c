// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 31/07/23
//
// -----------------------------------------------------------
// 1) Make an algorithm to read a value between 1 and 10 and
//    print the number on the screen times the its own value.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    int number;

    do {
        printf("Please enter a number from 1 to 10:\n");
        scanf("%d", &number);
        fflush(stdin);
        system("cls");
        if (number < 1 || number > 10) {
           printf("This number isn't on the interval from 1 to 10.\n");
        }
    } while (number < 1 || number > 10);

    for(int i = 0; i < number; i++) {
          printf("Printing number %d for the %d time.\n", number, i + 1);
    }


    printf("Press any key to continue...");
    getchar();

    return 0;
}

