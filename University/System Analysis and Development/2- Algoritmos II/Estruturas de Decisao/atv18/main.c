// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 18) Make a program that asks for the price of three products
//     and report which product you'll should buy, knowing that
//     the decision is always for the cheapest.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    float priceA;
    float priceB;
    float priceC;
    char cheapestProduct;
    float price;

    printf("Please insert the price of product A: \n");
    scanf("%f", &priceA);
    fflush(stdin);
    system("cls");

    printf("Please insert the price of product B: \n");
    scanf("%f", &priceB);
    fflush(stdin);
    system("cls");

    printf("Please insert the price of product C: \n");
    scanf("%f", &priceC);
    fflush(stdin);
    system("cls");

    if (priceA <= priceB && priceA <= priceC) {
        cheapestProduct = 'A';
        price = priceA;
        printf("The cheapest product is product %c with cost: $%.2f\n", cheapestProduct, price);
    }
    else if (priceB <= priceA && priceB <= priceC) {
        cheapestProduct = 'B';
        price = priceB;
        printf("The cheapest product is product %c with cost: $%.2f\n", cheapestProduct, price);
    }
    else {
        cheapestProduct = 'C';
        price = priceC;
        printf("The cheapest product is product %c with cost: $%.2f\n", cheapestProduct, price);
    }

    printf("Press any key to continue...");
    getchar();

    return 0;
}
