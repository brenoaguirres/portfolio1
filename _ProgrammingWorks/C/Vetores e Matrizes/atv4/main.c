// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 21/08/23
//
// -----------------------------------------------------------
// 4) Make an algorithm that reads an array s[20] and a variable a'.
//    Then, show the product of a by the array.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int s[20], a;

    for(int i = 0; i < 20; i++) {
        printf("Please insert the %d number:\n", i+1);
        scanf("%d", &s[i]);
    }

    printf("Now insert the number 'a' to multiply the numbers:\n");
    scanf("%d", a);

    for(int i = 0; i < 20; i++) {
        s[i] = s[i] * a;
        printf("%d ", s[i]);
    }

    printf("Press any key to continue...\n");
    getchar();

    return 0;
}
