// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 29) A fruit shop is selling fruits with the following price
//     table:
//                  Up to 5Kg  ---- Above 5Kg
//     Strawberry    $2.50/Kg  ----  $2.20/Kg
//     Apple         $1.80/Kg  ----  $1.50/Kg
//
//     If the client buys more than 8Kg in fruits or the order
//     price exceeds $25.00, he'll receive an additional 10%
//     discount over the full price of the order.
//     Write an algorithm to read the quantity (Kg) of strawberries
//     and apples bought and write the value to be paid by the
//     client.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    int appleQty;
    int strawberryQty;
    float applePrice;
    float strawberryPrice;
    float discount;
    float total;

    printf("Please insert the quantity of apples bought (Kg):\n");
    scanf("%d", &appleQty);
    fflush(stdin);
    system("cls");

    printf("Please insert the quantity of strawberries bought (Kg): \n");
    scanf("%d", &strawberryQty);
    fflush(stdin);
    system("cls");

    if (appleQty <= 5) {
        applePrice = 1.80;
    }
    else {
        applePrice = 1.50;
    }

    if (strawberryQty <= 5) {
        strawberryPrice = 2.50;
    }
    else {
        strawberryPrice = 2.20;
    }

    total = applePrice * appleQty + strawberryPrice * strawberryQty;

    if (appleQty + strawberryQty >= 8 || total >= 25) {
        total -= (total * 0.1);
    }

    printf("Final price of order: $%.2f\n", total);

    printf("Press any key to continue...");
    getchar();

    return 0;
}
