// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 20) Make a program that reads two partial grades received by
//     a student in a course along the semester, and calculate
//     its mean. The attribution of score is given by the table
//     below:
//       Mean --------------- Score
//     9.0-10.0                 A
//     7.5-9.0                  B
//     6.0-7.5                  C
//     6.0-4.0                  D
//     4.0-Zero                 E
//
//     The algorithm should show on screen the grades, the mean,
//     the score, and the message "APPROVED" for A, B and C, or
//     "FAILED" for D and E.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    float gradeA;
    float gradeB;
    float mean;
    char score;
    char message[10];

    printf("Please insert the student's first grade: \n");
    scanf("%f", &gradeA);
    fflush(stdin);
    system("cls");

    printf("Please insert the student's second grade: \n");
    scanf("%f", &gradeB);
    fflush(stdin);
    system("cls");

    mean = (gradeA + gradeB) / 2.0;

    if (mean >= 9.0) {
        score = 'A';
    }
    else if (mean < 9.0 && mean >= 7.5) {
        score = 'B';
    }
    else if (mean < 7.5 && mean >= 6.0) {
        score = 'C';
    }
    else if (mean < 6.0 && mean >= 4.0) {
        score = 'D';
    }
    else {
        score = 'E';
    }

    switch (score) {
        case 'A':
        case 'B':
        case 'C':
            strcpy(message, "APPROVED");
            break;
        case 'D':
        case 'E':
            strcpy(message, "FAILED");
            break;
        default:
            printf("ERR --");
            break;
    }

    printf("----SCHOOL REPORT----\n");
    printf("Grade A: %.1f\n", gradeA);
    printf("Grade B: %.1f\n", gradeB);
    printf("Final Score: %c\n", score);
    printf("---------------------\n");
    printf("Status: %s\n", message);

    printf("Press any key to continue...");
    getchar();

    return 0;
}
