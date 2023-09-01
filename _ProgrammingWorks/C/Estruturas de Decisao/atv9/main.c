// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 9) The academic management system from IFG, follows some
//    rules about the approval of determined student. Make an
//    algorithm that reads the name, the four grades, and the
//    number of absences of a student and writes their final
//    situation: Approved, disapproved by absences or
//    disapproved by grades mean. The mean for approval is 6.0,
//    the limit of absences is 25% of total classes. The total
//    classes taught was 72. The disapproval by absences
//    overlaps the disapproval by mean.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    char name[50];
    int grade1;
    int grade2;
    int grade3;
    int grade4;
    int absences;
    float mean;

    printf("Inform the student's name: \n");
    scanf("%s", &name);
    fflush(stdin);
    system("cls");

    printf("Inform the student's first grade: \n");
    scanf("%d", &grade1);
    fflush(stdin);
    system("cls");

    printf("Inform the student's second grade: \n");
    scanf("%d", &grade2);
    fflush(stdin);
    system("cls");

    printf("Inform the student's third grade: \n");
    scanf("%d", &grade3);
    fflush(stdin);
    system("cls");

    printf("Inform the student's fourth grade: \n");
    scanf("%d", &grade4);
    fflush(stdin);
    system("cls");

    printf("Inform the student's number of absences: \n");
    scanf("%d", &absences);
    fflush(stdin);
    system("cls");

    mean = (grade1 + grade2 + grade3 + grade4) / 4;
    if ((72 * 0.25) < absences) {
        printf("---------------------------------------------------\n");
        printf("SCHOOL REPORT - IFG\n");
        printf("---------------------------------------------------\n");
        printf("Name: %s\n", name);
        printf("Grade 1: %d\n", grade1);
        printf("Grade 2: %d\n", grade2);
        printf("Grade 3: %d\n", grade3);
        printf("Grade 4: %d\n", grade4);
        printf("---------------------------------------------------\n");
        printf("Total classes: 72.\n");
        printf("N of absences: %d.\n", absences);
        printf("---------------------------------------------------\n");
        printf("Final Mean: %.2f\n", mean);
        printf("---------------------------------------------------\n");
        printf("Status: Disapproved by Absences.");
    }
    else if (mean < 6.0){
        printf("---------------------------------------------------\n");
        printf("SCHOOL REPORT - IFG\n");
        printf("---------------------------------------------------\n");
        printf("Name: %s\n", name);
        printf("Grade 1: %d\n", grade1);
        printf("Grade 2: %d\n", grade2);
        printf("Grade 3: %d\n", grade3);
        printf("Grade 4: %d\n", grade4);
        printf("---------------------------------------------------\n");
        printf("Total classes: 72.\n");
        printf("N of absences: %d.\n", absences);
        printf("---------------------------------------------------\n");
        printf("Final Mean: %.2f\n", mean);
        printf("---------------------------------------------------\n");
        printf("Status: Disapproved by Mean.");
    }
    else {
        printf("---------------------------------------------------\n");
        printf("SCHOOL REPORT - IFG\n");
        printf("---------------------------------------------------\n");
        printf("Name: %s\n", name);
        printf("Grade 1: %d\n", grade1);
        printf("Grade 2: %d\n", grade2);
        printf("Grade 3: %d\n", grade3);
        printf("Grade 4: %d\n", grade4);
        printf("---------------------------------------------------\n");
        printf("Total classes: 72.\n");
        printf("N of absences: %d.\n", absences);
        printf("---------------------------------------------------\n");
        printf("Final Mean: %.2f\n", mean);
        printf("---------------------------------------------------\n");
        printf("Status: Approved.");
    }

    printf("Press any key to continue...");
    getchar();

    return 0;
}

