// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 23) Make a program that reads an integer lower than 1000 and
//     print how many hundreds, dozens and units it has.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    int number;

    int hundreds;
    int dozens;
    int units;

    char hundredsText[10];
    char dozensText[10];
    char unitsText[10];

    printf("Insert a number between 0 and 1000:\n");
    scanf("%d", &number);
    fflush(stdin);
    system("cls");

    if (number > 0 && number <= 1000) {
        if (number > 99) {
            hundreds = (number - (number % 100)) / 100;
            dozens = number - (hundreds * 100);
            dozens = (dozens - (dozens % 10)) / 10;
            units = number - hundreds * 100 - dozens * 10;
        }
        else if (number > 9) {
            hundreds = 0;
            dozens = number - (hundreds * 100);
            dozens = (dozens - (dozens % 10)) / 10;
            units = number - hundreds * 100 - dozens * 10;
        }
        else {
            hundreds = 0;
            dozens = 0;
            units = number;
        }

        switch (hundreds) {
            case 1:
                strcpy(hundredsText, "hundred");
                break;
            default:
                strcpy(hundredsText, "hundreds");
                break;
        }

        switch (dozens) {
            case 1:
                strcpy(dozensText, "dozen");
                break;
            default:
                strcpy(dozensText, "dozens");
                break;
        }

        switch (units) {
            case 1:
                strcpy(unitsText, "unit");
                break;
            default:
                strcpy(unitsText, "units");
                break;
        }

        if (number > 99) {
            printf("%d = %d %s, %d %s and %d %s.\n", number, hundreds, hundredsText, dozens, dozensText, units, unitsText);
        }
        else if (number > 9) {
            printf("%d = %d %s and %d %s.\n", number, dozens, dozensText, units, unitsText);
        }
        else if (number > 0) {
            printf("%d = %d %s.\n", number, units, unitsText);
        }
        else if (units == 0) {
            printf("Your number is 0.\n", number, hundreds, hundredsTe9xt, dozens, dozensText, units, unitsText);
        }
    }
    else {
        printf("Invalid number!\n");
    }

    printf("Press any key to continue...");
    getchar();

    return 0;
}
