//9
#include <stdio.h>
#include <stdlib.h>

int main() {

    int num;

    printf("Please insert a number: \n");
    scanf("%d", &num);
    fflush(stdin);
    system("cls");

    while (num > 1) {
          num = num / 2;
    }

    printf("Last division's result: %d\n", rslt);

    printf("Press any key to continue...");
    getchar();

    return 0;
}
