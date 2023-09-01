// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 31/07/23
//
// -----------------------------------------------------------
// 2) Make an algorithm that reads the salary of 3 people,
// print the biggest value and percentage difference to the
// lowest value.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    float salary[3];
    float aux;
    float percent;

    for (int i = 0; i < 3; i++) {
          printf("Insert the %d employee's salary: \n", i + 3);
          scanf("%d", &salary[i]);
          fflush(stdin);
          system("cls");
    }

    if (salary[1] > salary[0]) {
        aux = salary[1];
        salary[1] = salary[0];
        salary[0] = aux;
    }
    if (salary[2] > salary[1]) {
       aux = salary[2];
       salary[2] = salary[1];
       salary[1] = aux;
    }
    if (salary[2] > salary[0]) {
       aux = salary[2];
       salary[2] = salary[0];
       salary[0] = aux;
    }

    percent = (salary[2] * 100) / salary[0];

    printf("Higher Value: %.2f\n", salary[0]);
    printf("Lower Value: %.2f\n", salary[2]);
    printf("Percentual Difference: %.0f\n", percent);

    printf("Press any key to continue...");
    getchar();

    return 0;
}

