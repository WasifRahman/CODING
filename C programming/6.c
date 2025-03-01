//Arithmetic Operator +-*/   %-remainder
//Write a program that takes two integer and display sum.
#include<stdio.h>
int main()
{
    int num1,num2,sum;
    printf("Enter two numbers= ");
    scanf("%d %d" ,&num1, &num2);
    sum = num1 + num2;
    printf("\aThe sum is = %d\n", sum);
}

//Shows Sum and Average
#include<stdio.h>
int main()
{
    int num1,num2,sum;
    float avg;

    printf("Enter two numbers= ");
    scanf("%d %d" ,&num1, &num2);

    sum = num1 + num2;
    printf("The sum is = %d\n", sum);

    avg = (float)sum / 2;  //type Casting
    printf("\aThe average is = %.2f\n",avg);
}

//Plus, Minus, Multipication, Division
#include<stdio.h>
int main()
{
    int num1,num2,result;

    printf("Enter two numbers= ");
    scanf("%d %d" ,&num1, &num2);

    result = num1 + num2;
    printf("\aThe sum is = %d\n", result);

    result = num1 - num2;
    printf("\aThe sub is = %d\n", result);

    result = num1 * num2;
    printf("\aThe mul is = %d\n", result);

    result = num1 / num2;
    printf("\aThe Div is = %d\n", result);

    result = num1 % num2;
    printf("\aThe Reminder = %d\n", result);
}

//Write a program that calculates the Area of Triangle.
#include<stdio.h>
int main()
{
    float base, height, Area;
    printf("Base = ");
    scanf("%f",&base);

    printf("Height= ");
    scanf("%f",&height);

    Area = (float)1/2 * base * height;  //.5 deoa jabe
    printf("The Area of Triangle is = %.2f\n",Area);
}

//3 numbers sum, avg...
#include<stdio.h>
int main()
{
    int num1, num2, num3, sum;
    float avg;
    printf("Enter Three Number = ");
    scanf("%d %d %d", &num1, &num2, &num3);

    sum = num1 + num2+ num3;

    avg = (float)sum/ (float)3; // or sum/ (float)3; or (float)sum/3 or sum/3;

    printf("\aSum = %d\n", sum);
    printf("\aAverage = %.2f\n", avg);
}
