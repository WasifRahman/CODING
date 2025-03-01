/*//Enter a letter to check vowel or consonent using logical operator (&, || , !)
#include<stdio.h>
int main()
{
    char ch;
    printf("Enter a letter = ");
    scanf("%c", &ch);

    if(ch == 'a')
        printf("Vowel");
    else if(ch == 'e')
        printf("Vowel");
    else if(ch == 'i')
        printf("Vowel");
    else if(ch == 'o')
        printf("Vowel");
    else if(ch == 'u')
        printf("Vowel");

    else
        printf("Consonent");
    getch();
}

#include<stdio.h>
int main()
{
    char ch;
    printf("Enter a letter = ");
    scanf("%c", &ch);

    if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
        printf("Vowel");
    else
        printf("Consonent");
    getch();
}

//Write a program that read that three numbers and display maximum
#include<stdio.h>
int main()
{
    int num1, num2, num3;
    printf("Enter three numbers = ");
    scanf("%d %d %d", &num1, &num2, &num3);

    if(num1>num2 && num1>num3)
        printf("Highest number = %d\n", num1);
    else if(num2>num1 && num2>num3)
        printf("Highest number = %d\n", num2);
    else if(num3>num1 && num3>num2)
        printf("Highest number = %d\n", num3);
    else
        printf("Numbers are equal");
    getch();
}
*/
/*//Find out the largest from three numbers
#include<stdio.h>
int main()
{
    int num1, num2, num3;
    printf("Enter any three numbers = ");
    scanf("%d %d %d", &num1, &num2, &num3);

    if(num1>num2 && num1>num3)
        printf("Largest = %d", num1);
     else if(num2>num1 && num2>num3)
        printf("Largest = %d", num2);
     else if(num3>num1 && num3>num2)
        printf("Largest = %d", num3);
    else
        printf("Numbers are Equal.");
    getch();
}
*/
/*//How to find out Leap Year
#include<stdio.h>
int main()
{
    int year;
    printf("Enter any Year = ");
    scanf("%d", &year);

    if(year %400 == 0)
        printf("Leap Year");
    else if(year%4 == 0 && year%100 != 0 )
        printf("Leap Year");
    else
        printf("Not Leap Year");
    getch();
}
*/
/*//Capital letter or Small Letter
#include<stdio.h>
int main()
{
    char ch;
    printf("Enter any letter = ");
    scanf("%c", &ch);

    if(ch>='a' && ch<= 'z')
        printf("Small Letter");
    else if(ch>='A' && ch<='Z')
        printf("Capital letter");
    else
        printf("Not a letter");
    getch();
}
*/
/*//Vowel or Consonant Logical Operator
#include<stdio.h>
int main()
{
    char ch;
    printf("Enter any Letter = ");
    scanf("%c", &ch);

    if(ch == 'a' || ch == 'e' ||ch == 'i' ||ch == 'o' ||ch == 'u' )
        printf("Vowel");
    else if(ch == 'A' || ch == 'E' ||ch == 'I' ||ch == 'O' ||ch == 'U' )
        printf("Vowel");

    else
        printf("Consonant");
    getch();
}
*/
/*//Pass or Fail
#include<stdio.h>
int main()
{
    int mark;
    printf("Enter Mark = ");
    scanf("%d", &mark);

    if(mark>=33)
        printf("Pass");
    else
        printf("Fail");
    getch();
}
*/

Yt 82 theke


















