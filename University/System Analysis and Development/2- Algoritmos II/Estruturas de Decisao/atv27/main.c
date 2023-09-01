// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 27) A gas station is selling fuel with the following table
//     of discounts:
//     Alcohol - Below 20L, 3% per L. Above 20L, 5% per L.
//     Gasoline - Below 20L, 4% per L. Above 20L, 6% per L.
//
//     Write an algorithm that reads the number of liters sold,
//     the type of fuel (A - Alcohol, G - Gas), calculate and
//     print the value to be paid by the client knowing that the
//     price of the gas is $3.45 per liter and for the alcohol,
//     $2.69 per liter.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    char typeFuel;
    int quantityLiters;
    float price;

    printf("Which type of fuel do you want? (A - Alcohol ; G - Gasoline)\n");
    scanf("%c", &typeFuel);
    fflush(stdin);
    system("cls");

    printf("How much fuel do you want to buy? (In liters).\n");
    scanf("%d", &quantityLiters);
    fflush(stdin);
    system("cls");

    switch(typeFuel) {
        case 'A':
            if (quantityLiters <= 20) {
                price = 2.69 * quantityLiters - (quantityLiters * (2.69 * 0.03));
            }
            else {
                price = 2.69 * quantityLiters - (quantityLiters * (2.69 * 0.05));
            }
            printf("Price: $%.2f\n", price);
            break;
        case 'G':
            if (quantityLiters <= 20) {
                price = 3.45 * quantityLiters - (quantityLiters * (3.45 * 0.04));
            }
            else {
                price = 3.45 * quantityLiters - (quantityLiters * (3.45 * 0.06));
            }
            printf("Price: $%.2f\n", price);
            break;
        default:
            printf("Invalid type of fuel!\n");
            break;
    }

    printf("Press any key to continue...");
    getchar();

    return 0;
}
