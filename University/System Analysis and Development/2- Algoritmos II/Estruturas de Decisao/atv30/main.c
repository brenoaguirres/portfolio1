// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 30) Supermarket Tabajara is making an offer on meats that
//     you wouldn't want to miss! Check out:
//                  Up to 5Kg ---- Above 5Kg
//     Tenderloin   $14.90/Kg      $12.90/Kg
//     Rump steak   $13.90/Kg      $11.80/Kg
//     Rump cap     $15.90/Kg      $13.80/Kg
//
//     To serve all customers, each client can buy only one
//     type of meat. If the order is made with the Tabajara
//     card, the client will receive an additional 5% over
//     the total price of the order.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    int typeMeat;
    char meatName[12];
    int quantity;
    float finalPrice;
    float price;
    float discount;
    int useCard;

    printf("Welcome to Tabajara Supermarket!\n");
    printf("Which kind of meat do you want to buy?\n0 - Tenderloin\n1 - Rump steak\n2 - Rump cap\n");
    scanf("%d", &typeMeat);
    fflush(stdin);
    system("cls");

    printf("How much do you want to buy (Kg)?\n");
    scanf("%d", &quantity);
    fflush(stdin);
    system("cls");

    printf("Will you use the Tabajara Card to pay?\n0 - False\n1 - True");
    scanf("%d", &useCard);
    fflush(stdin);
    system("cls");

    switch(typeMeat) {
        case 0:
            strcpy(meatName, "Tenderloin");
            if (quantity <= 5) {
                price = quantity * 14.90;
            }
            else {
                price = quantity * 12.90;
            }
            break;
        case 1:
            strcpy(meatName, "Rump Steak");
            if (quantity <= 5) {
                price = quantity * 13.90;
            }
            else {
                price = quantity * 11.80;
            }
            break;
        case 2:
            strcpy(meatName, "Rump Cap");
            if (quantity <= 5) {
                price = quantity * 15.90;
            }
            else {
                price = quantity * 13.80;
            }
            break;
        default:
            break;
    }

    if (useCard != 0) {
        discount = price * 0.05;
        finalPrice = price - discount;
    }
    else {
        finalPrice = price;
    }

    printf("---- Receipt ----\n%d --- %s\nQuantity --- %d\nTotal --- %.2f\nPaid w/ card --- %d\n", typeMeat, meatName, quantity, price, useCard);
    printf("Discount --- %.2f\nPayment --- %.2f\n", discount, finalPrice);

    printf("Press any key to continue...");
    getchar();

    return 0;
}
