// Author: Breno Freitas Aguirres
// 2 semester - Technology in Systems Analysis and Development
// Instituto Federal de Goiás - IFG
// Course: Algorithms II
// 29/07/23
//
// -----------------------------------------------------------
// 15) Make a program that will calculate a payroll, knowing
//     that the discounts are from income tax, which depends
//     on the gross salary, and 3% for the syndicate and that
//     the FGTS corresponds to 1% of the gross salary, but its
//     not discounted. The net salary corresponds to the gross
//     salary minus the discounts. The program should ask the
//     user for his/her hourly rate and the quantity of hours
//     worked on the current month. Follow these rules:
//     IT discounts:
//     Gross salary up to $900 - Exempt.
//     Gross salary up to $1500 - 5% discount.
//     Gross salary up to $2500 - 10% discount.
//     Gross salary above $2500 - 20% discount.
//
//     Print to the screen the following info, shown like the
//     example below:
//     Gross Salary: (5 * 220)  :   $1100.00
//     (-) IT (5%)              :   $55.00
//     (-) INSS (10%)           :   $110.00
//     FGTS (1%)                :   $11.00
//     Total discounts          :   $165.00
//     Net Salary               :   $935.00
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int main() {

    float hourlyRate;
    int hoursWorked;

    double grossSalary;
    float it;
    int itPercentage;
    float inss;
    float fgts;
    double netSalary;

    printf("Please insert your hourly rate: \n");
    scanf("%f", &hourlyRate);
    fflush(stdin);
    system("cls");

    printf("Please insert the number of worked hours this month: \n");
    scanf("%d", &hoursWorked);
    fflush(stdin);
    system("cls");

    grossSalary = hourlyRate * hoursWorked;
    inss = grossSalary * 0.1;
    fgts = grossSalary * 0.01;

    if (grossSalary <= 900) {
        it = grossSalary * 0;
        itPercentage = 0;
    }
    else if (grossSalary <= 1500) {
        it = grossSalary * 0.05;
        itPercentage = 5;
    }
    else if (grossSalary <= 2500) {
        it = grossSalary * 0.1;
        itPercentage = 10;
    }
    else {
        it = grossSalary * 0.2;
        itPercentage = 20;
    }

    netSalary = grossSalary - it - inss;

    printf("Gross Salary: ($%.2f * %dh)  :   $%.2lf\n", hourlyRate, hoursWorked, grossSalary);
    printf("(-) IT (%d\%)              :   $%.2f\n", itPercentage, it);
    printf("(-) INSS (10%)           :   $%.2f\n", inss);
    printf("FGTS (1%)                :   $%.2f\n", fgts);
    printf("Total discounts          :   $%.2f\n", it + inss);
    printf("Net Salary               :   $%.2lf\n", netSalary);

    printf("Press any key to continue...");
    getchar();

    return 0;
}


