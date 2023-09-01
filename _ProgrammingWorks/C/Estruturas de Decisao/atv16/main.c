// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 16) Make a program that will have as input the cost price of
//     a product and an origin code, and it will return the price
//     along with it's code. In case the code its none of the
//     specified, the product should be classified as imported.
//     Origin code: 1 - South, 2 - North, 3 - East, 4 - West,
//     5 or 6 - North East, 7 or 8 - Center West.
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    float costPrice;
    int originCode;
    char originLocation[13];

    printf("Register the cost price of the product: \n");
    scanf("%f", &costPrice);
    fflush(stdin);
    system("cls");

    printf("Register the origin code of the product: \n");
    scanf("%d", &originCode);
    fflush(stdin);
    system("cls");

    switch (originCode) {
    case 1:
        strcpy(originLocation, "South");
        break;
    case 2:
        strcpy(originLocation, "North");
        break;
    case 3:
        strcpy(originLocation, "East");
        break;
    case 4:
        strcpy(originLocation, "West");
        break;
    case 5:
    case 6:
        strcpy(originLocation, "North East");
        break;
    case 7:
    case 8:
        strcpy(originLocation, "Center West");
        break;
    default:
        strcpy(originLocation, "Imported");
        break;
    }

    printf("New product registered.\n");
    printf("-------------------------\n");
    printf("Cost price: %.2f\n", costPrice);
    printf("Origin: %s\n", originLocation);

    printf("Press any key to continue...");
    getchar();

    return 0;
}

