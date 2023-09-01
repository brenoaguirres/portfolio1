// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 12) Make an algorithm to read a salary and update it
//     accordingly with the following table.
//     Salary   ---------------------   Raise
//     $<----600                        30%
//     $601-1100                        25%
//     $1101-2400                       20%
//     $2401-3550                       15%
//     $3551---->                       10%
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    double salary;

    printf("Insert your salary value: \n");
    scanf("%lf", &salary);
    fflush(stdin);
    system("cls");

    if (salary <= 600) {
        salary = salary + (salary * 0.3);
    }
    else if (salary > 600 && salary <= 1100) {
        salary = salary + (salary * 0.25);
    }
    else if (salary > 1100 && salary <= 2400) {
        salary = salary + (salary * 0.2);
    }
    else if (salary > 2400 && salary <= 3550) {
        salary = salary + (salary * 0.15);
    }
    else {
        salary = salary + (salary * 0.1);
    }

    printf("Your new salary is: %.2lf\n", salary);

    printf("Press any key to continue...");
    getchar();

    return 0;
}
