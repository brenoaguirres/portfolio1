

//11)
#include <stdio.h>
#include <stdlib.h>

int main() {

    float rcv;
    float sum = 0.0;
    int count = 0;
    float mean;
    
    do {
       printf("Insert a student grade: \n Type a negative number to exit...");
       scanf("%f", &rcv);
       fflush(stdin);
       system("cls");
       sum += rcv;
       count++;
    } while (rcv > 0);
    
    mean = sum / count;
    
    printf("The mean of the grades is: %.1f\n", mean);

    printf("Press any key to continue...");
    getchar();

    return 0;
}

//12)
#include <stdio.h>
#include <stdlib.h>

int main() {

    

    printf("Press any key to continue...");
    getchar();

    return 0;
}
