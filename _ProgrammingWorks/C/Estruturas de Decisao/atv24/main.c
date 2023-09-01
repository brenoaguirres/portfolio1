// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 24) Make a program that receives three user ages and follow
//     these instructions:
//     If the mean of the ages is lower than 25, print:
//     Young class.
//     If the mean of the ages is between 25 and 40, print:
//     Adult class.
//     If the mean of the ages is higher than 40, print:
//     Elder class.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    int ageA;
    int ageB;
    int ageC;

    float mean;

    printf("Insert the first student age:\n");
    scanf("%d", &ageA);
    fflush(stdin);
    system("cls");

    printf("Insert the second student age:\n");
    scanf("%d", &ageB);
    fflush(stdin);
    system("cls");

    printf("Insert the third student age:\n");
    scanf("%d", &ageC);
    fflush(stdin);
    system("cls");

    mean = (ageA + ageB + ageC) / 3;

    if (mean < 25 && mean > 0) {
        printf("Young class.\n");
    }
    else if (mean >= 25 && mean <= 40) {
        printf("Adult class.\n");
    }
    else {
        printf("Elder class.\n");
    }

    printf("Press any key to continue...");
    getchar();

    return 0;
}
