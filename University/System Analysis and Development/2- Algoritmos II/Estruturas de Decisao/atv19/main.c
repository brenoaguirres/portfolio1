// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 19) Make a program that will ask which shift you study. Ask
//     the user to input M, A, N, for the shifts. Print the
//     message "Good Morning!", "Good Afternoon!", "Good Evening!",
//     or "Invalid Shift!", accordingly to each case.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    char shift;

    printf("Which shift do you study?");
    scanf("%c", &shift);
    fflush(stdin);
    system("cls");

    if (shift == 'M') {
        printf("Good Morning!\n");
    }
    else if (shift == 'A') {
        printf("Good Afternoon!\n");
    }
    else if (shift == 'N') {
        printf("Good Evening!\n");
    }
    else {
        printf("Invalid Shift!\n");
    }

    printf("Press any key to continue...");
    getchar();

    return 0;
}
