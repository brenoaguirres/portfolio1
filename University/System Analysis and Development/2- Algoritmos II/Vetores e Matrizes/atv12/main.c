// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 26/08/23
//
// -----------------------------------------------------------
// 12) Write an algorithm that reads an array of 13 elements,
//     which is the answers of the lottery, containing the values
//     1 - column 1, 2- column 2, 3 - mid column. Read, next, for
//     each punter, the number of its card and an array of 13
//     answers. Verify, for each punter the number of correct
//     answers. Write the number of the punter and the number of
//     correct answers, if he has 13 correct answers, write WINNER!
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

#define ANSWERS 13

int main()
{

    int correctAnswers[ANSWERS], cardNumber, cardAnswers[ANSWERS], score = 0;

    for(int i = 0; i < ANSWERS; i++) {
        printf("Please insert the correct answer of question %d:\n1 - Left Column, 2 - Right Column, 3 - Mid Column\n", i+1);
        scanf("%d", &correctAnswers[i]);
        while(getchar() != '\n');
        system("cls");
    }

    printf("Please insert the number of the number of the punter's card:\n");
    scanf("%d", &cardNumber);
    while(getchar() != '\n');
    system("cls");

    for(int i = 0; i < ANSWERS; i++) {
        printf("Please insert the punter's answer for the question %d:\n1 - Left Column, 2 - Right Column, 3 - Mid Column\n", i+1);
        scanf("%d", &cardAnswers[i]);
        while(getchar() != '\n');
        system("cls");

        if(correctAnswers[i] == cardAnswers[i]) {
            score++;
        }
    }

    printf("Punter's card number:\n%d\n", cardNumber);
    printf("Punter's score:\n%d\n", score);
    if(score == ANSWERS) {
        printf("*****WINNER!*****");
    }
    else {
        printf("Not this time! Good luck for the next time.");
    }
    printf("\n\n");

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
