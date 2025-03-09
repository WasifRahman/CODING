
#***Input value. User's help 
name= input("Enter your name: ")
age= input("Enter your age: ")
GPA= input("Enter your GPA: ")
print("")
print("Student Information")
print("--------------------")
print("Name= " ,name)
print("Age= " ,age)
print("GPA= " ,GPA) 



#!'''CGPA Percentage'''
a = float(input("Enter your Math CGPA:"))
b = float(input("Enter your English CGPA:"))
c = float(input("Enter your Bangla CGPA:"))

CGPA = (a+b+c)/3
CGPAPer = 9.5*CGPA
print("Your CGPA Percentage is",CGPAPer)

#!
print("Enter your number")
inpnum = int(input())
print("You Enter = ", inpnum+10)  # int(inpnum)+10

#! CALCULATOR
#Calculator
print("First Number = ")
x = int(input())
print("Second Number = ")
y = int(input())
print("Total = ", x+y)
#or,
x = input("Enter first Number = ")
y = input("Enter second Number  = ")
print("Total = ", int(x)+int(y))

#!=====================EXERCISE 1
#!Input Function
name = input("Enter your name: ")
print(f"Hello {name}.")

age = float(input("Enter your age: "))
#! age = int(age) + 1
print(f"You are {age} years old.")

#!mad libs game
adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an adjective: ")

print(f'Today I went to a {adjective1} zoo.')
print(f"In an exhibit, I saw {noun}.")
print(f"{noun} was {adjective2} and {verb}ing.")
print(f"I was {adjective3}.")
