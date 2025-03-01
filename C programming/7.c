//The area of Tringle when there are 3 length...
//area = sqrt(s*(s-a)*(s-b)*(s-c))
#include<stdio.h>
int main()
{
    double a,b,c,area,s;
    printf("Enter 3 values = ");
    scanf("%lf %lf %lf", &a, &b, &c);

    s= (a+b+c)/2;

    area = sqrt(s*(s-a)*(s-b)*(s-c));

    printf("\aThe Area of Triangle = %.2lf",area);
}

//The Area of Rectangular.
//area of rectangle = length * width
#include<stdio.h>
int main()
{
    float length, width, area;
    printf("Enter length= ");
    scanf("%f", &length);


    printf("Enter width= ");
    scanf("%f", &width);


     area = length * width;
    printf("The area of Rectangular = %.2f\n", area);
}

//The Area of Circle
//area = 3.1416* radius* radius
#include<stdio.h>
//#include<math.h>
int main()
{
    float radius, area; //PI age diea daoa

    printf("Enter Radius = ");
    scanf("%f", &radius);

    area = 3.1416* radius* radius;  //M_PI dile o hobe but arek ta libary function lagbe

    printf("The Area of Circle is = %.2f\n", area);
}

//Celcius to Farenheit
// F= (C*1.8) + 32
#include<stdio.h>
int main()
{
    float C, F;
    printf("Input the value of Centigrade = ");
    scanf("%f", &C);
    F = ((9*C)/5)+32;  //Upore Arekta Suttro
    printf("The value of Fahrenheit = %.2f", F);
}

//Farenheit to Celcius
//C= (F-32)/1.8 or C= (5/9)*(F-32)
#include<stdio.h>
int main()
{
    float C, F;
    printf("Input the value of Fahrenheit = ");
    scanf("%f", &F);
    C = (F-32)/1.8;  //Upore Arekta Suttro
    printf("The value of Centrigrade = %.2f", C);
}

//Swaping Two numbers With Temporary Variable...
#include<stdio.h>
int main()
{
    int num1 = 10;
    int num2 = 5;

    int temp;
    temp = num1;   //temp = 10
    num1 = num2;  // num1 = 5
    num2 = temp;  // num2 = 10

    printf("num1 = %d\n", num1);
    printf("num2 = %d\n", num2);
}

//Swaping two numbers Without Temporary Variable...
#include<stdio.h>
int main()
{
    int num1 = 10;
    int num2 = 5;

    num1 = num1 - num2;  //num1 = 5
    num2 = num1 + num2;  //num2 = 10
    num1 = num2 - num1;  //5

    printf("num1 = %d\n", num1);
    printf("num2 = %d\n", num2);
}

//Quadratic Equation = ax^2+bx+c solve the x...
#include<stdio.h>
int main()
{
    double a,b,c,d,x1,x2;

    printf("Enter a b c = ");
    scanf("&if %if %if", &a, &b, &c);

    d = sqrt(b*b-4*a*c);

    x1 = (-b+d)/(2*a);
    x2 = (-b-d)/(2*a);

    printf("\ax1 = %lf\n", x1);
    printf("x2 = %lf\n", x2);
}

