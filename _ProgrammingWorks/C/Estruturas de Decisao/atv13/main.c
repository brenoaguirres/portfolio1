// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 13) Make a program that will ask for a 4 - digit year, and
//     then determine if the year is a leap year.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    int year;

    printf("Please insert an year: \n");
    scanf("%d", &year);
    fflush(stdin);
    system("cls");

    if ((year % 4) == 0) {
        if ((year % 100) == 0) {
            if ((year % 400) == 0) {
                printf("The year %d is divisible by 400, it is a LEAP YEAR!\n", year);
            }
            else {
                printf("The year %d is not divisible by 400, so it is NOT a LEAP YEAR!\n", year);
            }
        }
        else {
            printf("The year %d is divisible by 4 but not by 100, it is a LEAP YEAR!\n", year);
        }
    }
    else {
        printf("The year %d is not divisible by 4, so it is NOT a LEAP YEAR!\n", year);
    }


    printf("Press any key to continue...");
    getchar();

    return 0;
}
