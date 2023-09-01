//6)
#include <stdio.h>
#include <stdlib.h>

int main() {

    for (i = 0; i > 50; i++) {
        printf(i+1);
    }

    printf("Press any key to continue...");
    getchar();

    return 0;
}

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

//8)
#include <stdio.h>
#include <stdlib.h>

int main() {

    int num;
    int fat = num;
    
    printf("Insert a number: \n");
    scanf("%d", &num);
    fflush(stdin);
    system("cls");
    
    for (i = num -1; i < 0; i--) {
    
        fat *= i;
    }
    
    printf("The fatorial of all numbers between %d and 1 is: %d", num, fat);

    printf("Press any key to continue...");
    getchar();

    return 0;
}

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

//11)
#include <stdio.h>
#include <stdlib.h>

int main() {

    printf("Press any key to continue...");
    getchar();

    return 0;
}
