// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 5) Make an algorithm to read the coefficients from a 2nd
//    grade equation and calculate its roots, in the ax^2 + bx
//    + c form, taking in consideration the existence of real
//    roots (delta > 0, the equation has two real and distinct
//    roots; delta = 0, the equation's roots are equal; delta
//    < 0, the equation has no real roots).
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {

    int a;
    int b;
    int c;

    int delta;
    int x1;
    int x2;

    printf("Insert the first coefficient (a): \n");
    scanf("%d", &a);
    fflush(stdin);
    system("cls");

    printf("Insert the second coefficient (b): \n");
    scanf("%d", &b);
    fflush(stdin);
    system("cls");

    printf("Insert the third coefficient (c): \n");
    scanf("%d", &c);
    fflush(stdin);
    system("cls");

    delta = (b*b) - 4 * a * c;

    if (delta < 0) {
        printf("There are no real roots for this equation.\n");
    }
    else if (delta > 0) {
        x1 = (-b + sqrt(delta)) / 2 * a;
        x2 = (-b - sqrt(delta)) / 2 * a;
        printf("There are two real roots: x1 '%d' and x2 '%d'.\n", x1, x2);
    }
    else {
        x1 = (-b + sqrt(delta)) / 2 * a;
        printf("There is a single real root. x '%d'.\n", x1);
    }

    printf("Press any key to continue...");
    getchar();

    return 0;
}


