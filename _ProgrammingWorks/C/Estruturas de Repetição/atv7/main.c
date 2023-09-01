//7)
#include <stdio.h>
#include <stdlib.h>

int main() {

    int num;
    int sum = num;

    printf("Insert a number: \n");
    scanf("%d", &num);
    fflush(stdin);
    system("cls");

    for (i = num -1; i < 0; i--) {
        sum += i;
    }

    printf("The sum of all numbers between %d and 1 is: %d", num, sum);

    printf("Press any key to continue...");
    getchar();

    return 0;
}
