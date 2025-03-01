//YT=
//Finished=6, not 4
#include<stdio.h>
int main()
{
    float a,b,c,d,x1,x2;
    printf("Enter a b c = ");
    scanf("%f %f %f", &a, &b, &c);

    d= sqrt(b*b-4*a*c);

    x1 = (-b+d)/(2*a);
    x2 = (-b-d)/(2*a);

    printf("x1 = %f , x2 = %f", x1,x2);
}










