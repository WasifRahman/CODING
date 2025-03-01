//Absolute Value  library function : abs
#include<stdio.h>
int main()
{
    int result = abs(-25); //25 same
    printf("The Absolute Number is = %d", result);
}

// Square Root Library function : sqrt
#include<stdio.h>
int main()
{
    float x,result;
    printf("Enter any number = ");
    scanf("%f", &x);

    result = sqrt(x);
    printf("The Square Root is = %.2f", result);
}

// Power Library function : pow
#include<stdio.h>
int main()
{
    int x, y;
    printf("Enter x = ");
    scanf("%d", &x);

    printf("Enter y = ");
    scanf("%d", &y);

    float result = pow(x, y);
    printf("\aThe Number is = %.2f", result);
}

//Log, Log10
#include<stdio.h>
int main()
{
    double x = 10.5;

    double result = log(x);
    printf("log10(%.2lf) = %lf\n",x,result);
}

//
#include<stdio.h>
int main()
{
    double x = .35;

    double result = exp(x);
    printf("exp(%lf) = %lf\n",x,result);
}

//sin, tan, cos...
#include<stdio.h>
int main()
{
    double x = .35;

    double result = sin(x);
    printf("sin(%lf) = %lf\n",x,result);
}

#include<stdio.h>
int main()
{
    double x = 5.35;

    double result = round(x);
    printf("round(%lf) = %lf\n",x,result);
}

#include<stdio.h>
int main()
{
    double x = 5.56535;

    double result = trunc(x);
    printf("trunc(%lf) = %lf\n",x,result);
}

#include<stdio.h>
int main()
{
    double x = 3.3;

    double result = ceil(x);
    printf("ceil(%lf) = %lf\n",x,result);
}

#include<stdio.h>
int main()
{
    double x = -1.5;

    double result = floor(x);
    printf("floor(%lf) = %lf\n",x,result);
}

//Complete
