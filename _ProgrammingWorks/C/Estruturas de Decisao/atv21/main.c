// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 21) Make a program that asks for a date in dd/mm/yyyy format
//     and determine if it's a valid date.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    int dd;
    int mm;
    int yyyy;

    printf("Please input a day on dd format: \n");
    scanf("%d", &dd);
    fflush(stdin);
    system("cls");

    printf("Please input a month on mm format: \n");
    scanf("%d", &mm);
    fflush(stdin);
    system("cls");

    printf("Please input a year on yyyy format: \n");
    scanf("%d", &yyyy);
    fflush(stdin);
    system("cls");

    if (dd <= 31 && dd > 0) {
        if (mm <= 12 && mm > 0) {
            if (yyyy > 0) {
                switch (mm) {
                    case 2:
                        if (dd <= 29) {
                            printf ("This is a valid date: %d/%d/%d\n", dd, mm, yyyy);
                        }
                        else {
                            printf ("This isn't a valid date!\n");
                        }
                        break;
                    case 4:
                    case 6:
                    case 9:
                    case 11:
                        if (dd >= 30) {
                            printf ("This is a valid date: %d/%d/%d\n", dd, mm, yyyy);
                        }
                        else {
                            printf ("This isn't a valid date!\n");
                        }
                        break;
                    default:
                        printf ("This is a valid date: %d/%d/%d\n", dd, mm, yyyy);
                        break;
                }
            }
            else {
                printf ("This isn't a valid date!\n");
            }
        }
        else {
            printf ("This isn't a valid date!\n");
        }
    }
    else {
        printf ("This isn't a valid date!\n");
    }

    printf("Press any key to continue...");
    getchar();

    return 0;
}
