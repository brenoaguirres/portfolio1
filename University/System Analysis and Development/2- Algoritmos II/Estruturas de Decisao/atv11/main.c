// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 11) A merchant has bought a product and wants to sell it
//     with 45% of profit if the order's value is less than
//     20$, otherwise, the profit will be of 30%. Make an
//     algorithm that will read the product's price and print
//     the selling value of it.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    float productValue;
    float sellingValue;

    printf("Insert the product's value: \n");
    scanf("%f", &productValue);
    fflush(stdin);
    system("cls");

    if (productValue < 20.0) {
        sellingValue = productValue + (productValue * 0.45);
        printf("The selling price will be of $%.2f\n", sellingValue);
    }
    else {
        sellingValue = productValue + (productValue * 0.3);
        printf("The selling price will be of $%.2f\n", sellingValue);
    }

    printf("Press any key to continue...");
    getchar();

    return 0;
}
