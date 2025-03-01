//Write a program that takes an integer and print that number.

#include <stdio.h>
int main()
{
    int number;
    double value;
    printf("ENter a number= \n");
    scanf("%d %lf", &number, &value);
    printf("The number is = %d and %lf", number, value);
}



//Octal to Hexa-Decimal
#include <stdio.h>
int main()
{
    int number;
    printf("Enter a octal number:");
    scanf("%o", &number);
    printf("The number is = %x", number);
}

//solve the equation
#include <stdio.h>
int main()
{
    float a,b,c,d,x1,x2;
    printf("Enter a,b,c = ");
    scanf("%f %f %f", &a, &b, &c);
    d=sqrt(b*b-4*a*c);
    x1=(-b+d)/2*a;
    x2=(-b-d)/2*a;
    printf("THe results are %f %f", x1, x2);
}

//*********************************************************************************//

#include<stdio.h>
int main()
{
    char ch;
    printf("Hello, Welcome to the world!\n");
    printf("I welcome you warrior.\n");
    printf("Please, Login to the server.\n");
    printf("Enter your gmail, please.\n");
    scanf("%c", &ch)
    printf("So, you are %c\n", ch);

    int a, b, c, d;
    printf("Input Your PIN : ");
    scanf("%1d" "%1d" "%1d" "%1d", &a, &b, &c, &d);
    printf("Output Your PIN : %1d %1d %1d %1d", a, b, c, d);
    return 0;
}























