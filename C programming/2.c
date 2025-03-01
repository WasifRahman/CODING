//Printing Two number together.
#include<stdio.h>
int main()
{
    int num1=20, num2=30;
    printf("Numbers are %d, %d.\n", num1,num2);
}

//Write a program that prints a floating, Double and Character.
#include<stdio.h>
int main()
{
    float num1;
    double num2;
    char ch ='a';
    num1= 10.5;
    num2=10.55554;
    printf("num1 = %.1f\n", num1);  //.1 mane ek ghor
    printf("num2 = %lf\n", num2);
    printf("ch = %c\n", ch);
    printf("The numbers are %.1f,  %lf", num1, num2);
}

//Write a program that takes an integer and print that number.
#include<stdio.h>
int main()
{
    int num;
    printf("Please enter an integer : ");
    scanf("%d",&num);
    printf("You have pressed : %d",num);
}

//Taking values from user.
#include<stdio.h>
int main()
{
    int num1, num2;
    printf("Enter First integer= ");
    scanf("%d", &num1);

    printf("Enter Second integer= ");
    scanf("%d", &num2);
    printf("Numbers are= %d, %d\n", num1,num2);
}

//With one or many int or float or both.
#include<stdio.h>
int main()
{
    int num1;
    float num2;
    printf("Enter an integer and a floating number= ");
    scanf("%d %f", &num1,&num2);
    printf("Numbers are= %d, %.1f\n", num1,num2); 
}

