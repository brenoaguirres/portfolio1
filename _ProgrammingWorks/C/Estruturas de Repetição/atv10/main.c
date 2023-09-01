//10
#include <stdio.h>
#include <stdlib.h>

int main() {

    int num;
    float e_rslt = 1;

    printf("Please insert a number: \n");
    scanf("%d", &num);
    fflush(stdin);
    system("cls");

    for (i = 0; i < num; i++) {
        float fat = i + 1;

        for (j = i; j > 1; j--) {
            fat *= j;
        }

        e_rslt += 1 / fat;
    }

    printf("E = %.4f", &e_rslt);

    printf("Press any key to continue...");
    getchar();

    return 0;
}
