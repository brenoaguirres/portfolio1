// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 26) Make a program that ask 5 questions for a person about
//     a crime. The questions are:
//     "Did you telephoned for the victim?"
//     "Were you at the crime scene?"
//     "Do you live near the victim?"
//     "Do you had a debt with the victim?"
//     "Have you ever worked with the victim?"
//
//     The program should issue a classification about the
//     involvement of the user in the crime.
//     If the person answer positively to two questions, it
//     should be classified as "Suspect", between 3 to 4 as
//     "Accomplice" and 5 as "Killer". Otherwise, he'll be
//     classified as "Innocent".
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    char answer;
    int score = 0;

    printf("Police interrogation - Answer the questions with Y/N\n");
    printf("Press any key...\n");
    getchar();

    printf("Did you telephoned for the victim?\n");
    scanf("%c", &answer);
    fflush(stdin);
    system("cls");
    if (answer == 'Y') {
        score +=1;
    }

    printf("Were you at the crime scene?\n");
    scanf("%c", &answer);
    fflush(stdin);
    system("cls");
    if (answer == 'Y') {
        score +=1;
    }

    printf("Do you live near the victim's place?\n");
    scanf("%c", &answer);
    fflush(stdin);
    system("cls");
    if (answer == 'Y') {
        score +=1;
    }

    printf("Did you had a debt with the victim?\n");
    scanf("%c", &answer);
    fflush(stdin);
    system("cls");
    if (answer == 'Y') {
        score +=1;
    }

    printf("Have you ever worked with the victim?\n");
    scanf("%c", &answer);
    fflush(stdin);
    system("cls");
    if (answer == 'Y') {
        score +=1;
    }

    if (score < 2) {
        printf("You've been classified as Innocent!\n");
    }
    else if (score == 2) {
        printf("You've been classified as Suspect!\n");
    }
    else if (score == 3 || score == 4) {
        printf("You've been classified as Accomplice!\n");
    }
    else {
        printf("You've been classified as the Killer!\n");
    }

    printf("Press any key to continue");
    getchar();

    return 0;
}
