// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 26/08/23
//
// -----------------------------------------------------------
// 11) Write an algorithm that reads an array G of 10 char
//     elements which represents the result of an exam. Next,
//     for each one of the five students of the class, read the
//     array of answers (r) of the student and count the number
//     of correct answers. Show the number of correct answers of
//     each student and a message saying if its "APPROVED", in
//     case the answer's sum is greater than or equal to 6, or
//     "DISAPPROVED" otherwise.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

#define N_QUESTIONS 10
#define N_STUDENTS 5

int main()
{
    char g[N_QUESTIONS], r[N_STUDENTS][N_QUESTIONS];
    int final_result[N_STUDENTS] = {0, 0, 0, 0, 0};

    for(int i = 0; i < N_QUESTIONS; i++) {
        printf("Please insert the test's correct answer for question %d:\n 'a'  'b'  'c'  'd'  'e' \n", i+1);
        scanf("%c", &g[i]);
        while(getchar() != '\n');
        system("cls");
    }

    for(int i = 0; i < N_STUDENTS; i++) {
        for(int j = 0; j < N_QUESTIONS; j++) {
            printf("Please insert student %d's %d answer:\n 'a'  'b'  'c'  'd'  'e' \n", i+1, j+1);
            scanf("%c", &r[i][j]);
            while(getchar() != '\n');
            system("cls");

            if(r[i][j] == g[j]) {
                final_result[i] += 1;
            }
        }
    }

    for(int i = 0; i < N_STUDENTS; i++) {
        printf("Student %d's results:\n", i+1);
        for(int j = 0; j < N_QUESTIONS; j++) {
            printf("%c  ", r[i][j]);
        }
        printf("\nFinal Score: %d", final_result[i]);
        printf("\nStudent Status: ");
        if (final_result[i] >= 6) {
            printf("APPROVED");
        }
        else {
            printf("NOT APPROVED");
        }
        printf("\n\n");
    }

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
