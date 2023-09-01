// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 7) Make an algorithm to read three real values and inform if
//    these could form or not the sides of a triangle and which
//    kind of triangle it would be: equilateral, isosceles,
//    or scalene.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    int side_A;
    int side_B;
    int side_C;

    int triangle_flag = 0;

    printf("Inform the first side of the triangle: \n");
    scanf("%d", &side_A);
    fflush(stdin);
    system("cls");

    printf("Inform the second side of the triangle: \n");
    scanf("%d", &side_B);
    fflush(stdin);
    system("cls");

    printf("Inform the third side of the triangle: \n");
    scanf("%d", &side_C);
    fflush(stdin);
    system("cls");

    // check to see if its a triangle;
    if (side_A + side_B > side_C) {
        if (side_B + side_C > side_A) {
            if (side_A + side_C > side_B) {
                triangle_flag = 1;
            }
        }
    }

    if (triangle_flag == 0) {
        printf("The informed values do not form a triangle.\n");
    }
    else {
        if (side_A == side_B && side_B == side_C) {
            printf("The informed triangle is equilateral.\n");
        }
        else if (side_A == side_B || side_B == side_C || side_C == side_A) {
            printf("The informed triangle is isosceles.\n");
        }
        else if (side_A != side_B && side_B != side_C) {
            printf("The informed triangle is scalene.\n");
        }
    }

    getchar();

    return 0;
}
