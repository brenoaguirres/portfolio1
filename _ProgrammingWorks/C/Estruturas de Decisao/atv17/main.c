// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 17) Make a program to verify if the letter is a vowel or a
//     consonant.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    char letter;

    printf("Please insert a letter: \n");
    scanf("%c", &letter);
    fflush(stdin);
    system("cls");

    if (letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u') {
        printf("This letter is a vowel.\n");
    }
    else {
        printf("This letter is a consonant.\n");
    }

    printf("Press any key to continue...");
    getchar();

    return 0;
}
