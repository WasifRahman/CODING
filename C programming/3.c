//Size of int, char etc.
#include<stdio.h>
int main()
{
    int i;
    float f;
    double d;
    char c;

    printf("Size of int = %d bytes\n", sizeof(i));
    printf("Size of float = %d bytes\n", sizeof(f));
    printf("Size of double = % d bytes\n", sizeof(d));
    printf("Size of character = %d bytes\a", sizeof(c));
}

//Finding ASCII Character
#include<stdio.h>
int main()
{
    int n;
    printf("Enter any ASCII value=");
    scanf("%d",&n);
    printf("The ASCII Character is = %c", n);
}

//Finding ASCII Value
#include<stdio.h>
int main()
{
    char ch;
    printf("Enter your ASCII character = ");
    scanf("%c", &ch);
    printf("The number of ASCII Value is=  %d",ch);
}

//Lower case to Upper Case
#include<stdio.h>
int main()
{
    char lower;
    printf("Enter any lower case letter=");
    scanf("%c", &lower);  //a=97  b=98

    printf("The Upper Case letter is = %c", lower-32); //A=65 B=66 difference 32
}

//Upper Case to Lower Case
#include<stdio.h>
int main()
{
    char upper;
    printf("Enter any Upper Case Letter = ");
    scanf("%c", &upper);  //A = 65

    printf("The Lower Case letter is = %c", upper+32); //a=97
}

//With Library Function Upper to lower case.
#include<stdio.h>
int main()
{
    char lower, upper;
    printf("Enter any lower case letter=");
    scanf("%c", &lower);

    upper = toupper(lower);
    printf("Upper case letter = %c", upper);
}

//With library function Upper to Lower case.
#include<stdio.h>
int main()
{
    char lower,upper;
    printf("Enter any upper case letter = ");
    scanf("%c", &upper);
    lower= tolower(upper);
    printf("Lower case letter = %c", lower);
}

