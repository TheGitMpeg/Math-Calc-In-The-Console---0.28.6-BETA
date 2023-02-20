#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>
char OperationStrVar[40];

void Addition() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
    float additi1, additi2, additires;
    printf("Type the numbers to add: NOTE: DON'T TYPE ANY LETTER WHEN YOU'RE IN THE NUMBERS INPUT PAGE!\n");
    printf("First number:\n");
    scanf("%f", &additi1);
    printf("Second number:\n");
    scanf("%f", &additi2);
    additires = additi1 + additi2;
    printf("The result of your addition is:\n");
    printf("%f", additires);
    sleep(10);
    printf("\nOperation: %f + %f = %f", additi1, additi2, additires);
    sleep(5);
}
void Subtraction() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
    float subtra1, subtra2, subtrares;
    printf("Type the numbers to subtract: NOTE: DON'T TYPE ANY LETTER WHEN YOU'RE IN THE NUMBERS INPUT PAGE!\n");
    printf("First number:\n");
    scanf("%f", &subtra1);
    printf("Second number:\n");
    scanf("%f", &subtra2);
    subtrares = subtra1 - subtra2;
    printf("The result of your subtraction is:\n");
    printf("%f", subtrares);
    sleep(10);
    printf("\nOperation: %f - %f = %f", subtra1, subtra2, subtrares);
    sleep(5);
}
void Multiplication() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
    float multip1, multip2, multipres;
    printf("Type the numbers to multiply: NOTE: DON'T TYPE ANY LETTER WHEN YOU'RE IN THE NUMBERS INPUT PAGE!\n");
    printf("First number:\n");
    scanf("%f", &multip1);
    printf("Second number:\n");
    scanf("%f", &multip2);
    multipres = multip1 * multip2;
    printf("The result of your multiplication is:\n");
    printf("%f", multipres);
    sleep(10);
    printf("\nOperation: %f * %f = %f", multip1, multip2, multipres);
    sleep(5);
}
void Division() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
    float divisi1, divisi2, divisires;
    printf("Type the numbers to divide: NOTE: DON'T TYPE ANY LETTER WHEN YOU'RE IN THE NUMBERS INPUT PAGE!\n");
    printf("First number:\n");
    scanf("%f", &divisi1);
    printf("Second number:\n");
    scanf("%f", &divisi2);
    divisires = divisi1 / divisi2;
    printf("The result of your division is:\n");
    printf("%f", divisires);
    sleep(10);
    printf("\nOperation: %f + %f = %f", divisi1, divisi2, divisires);
    sleep(5);
}
void ExitTheApp() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
    exit(0);
}
void MainApplicationFunction() {
    printf("Math: Calc In The Console - Four Operations\nAvailable operations:\nAdd\nSubtract\nMultiply\nDivide\nExit\nPlease note that they are case-sensitive.\nSelect operation: ");
    scanf("%s", OperationStrVar);
}
int main() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
    MainApplicationFunction();
    while (1) {
        if (strcmp(OperationStrVar, "Add") == 0) {
            Addition();
            #ifdef _WIN32
                system("cls");
            #else
                system("clear");
            #endif
            MainApplicationFunction();
        } else if (strcmp(OperationStrVar, "Subtract") == 0) {
            Subtraction();
            #ifdef _WIN32
                system("cls");
            #else
                system("clear");
            #endif
            MainApplicationFunction();
        } else if (strcmp(OperationStrVar, "Multiply") == 0) {
            Multiplication();
            #ifdef _WIN32
                system("cls");
            #else
                system("clear");
            #endif
            MainApplicationFunction();
        } else if (strcmp(OperationStrVar, "Divide") == 0) {
            Division();
            #ifdef _WIN32
                system("cls");
            #else
                system("clear");
            #endif
            MainApplicationFunction();
        } else if (strcmp(OperationStrVar, "Exit") == 0) {
            ExitTheApp();
        } else if (strcmp(OperationStrVar, "") == 0) {
            printf("\nYou typed nothing of these available operations.");
            MainApplicationFunction();
        } else {
            printf("\n", "What you typed is not an operation. Try again. You can do it.", OperationStrVar);
            MainApplicationFunction();
        }
    }
    return 0;
}
