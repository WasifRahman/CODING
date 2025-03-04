
#***Pass/ Fail , if else statement
mark=80
if mark>=33:
    print("Result:Pass")
else:
    print("Result:Fail")

#!Largest
a=-20
b=10
if a>b:
    print(a)
else:
    print(b)
#!
if 7>3:
    if 7>6:
        print("Hi!")
    else:
        print("Hello")

#!Even /odd
d=5
if d%2==0:         #Important to remember (reminder)
    print("Even")
else:
    print("Odd")

#!IF STATEMENTS
age = int(input("ENter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't born yet")
elif age >= 100:
    print("You are too old to sign up")
else:
    print("You must be 18+ to sign up")


#!===================EXERCISE1
response = input("What you like food? (Y/N): ")

if response == "y":
    print("Have some food.") 
else:
    print("No food for you.")


#!===================EXERCISE 2
name =input("Enter your name: ")

if name == "":
    print("Put a name.")
else:
    print(f"Hello, {name}")
#!===================EXERCISE 3
marks = 23
if 80 <= marks <= 100:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("A-")
    
elif marks >= 50:
    print("B")
elif marks >= 40:
    print("C")
elif marks >= 33:
    print("D")
else:
    print("Fail")
#!===================EXERCISE 4
marks = 75
if 80<= marks <= 100:
    print("A+")
elif 70 <= marks <= 79:
    print("A")

if marks >= 80 and marks <= 100:
    print("A+")
elif marks >= 70 and marks <= 79:
        print("A")

#! USING Logical Operator "or and not"
name = input("What's your name?")

if not name == "Ben":
    # if name != "Ben": != is not
    print(name)
else:
    print("No name")
#!===================EXERCISE 5
name= input("What's your name?")

if name == "Ben":
    status = input("Are you evil?")
    if status == "yes":      #This is a nested ifs.
        print("Get out!!!")
    else:
        print("You are one of the good Bens")
else:
    print("Come in")
#!===================EXERCISE 6
name= input("Enter Your Name: ")
a= float(input("Enter your Math marks: "))
b= float(input("Enter your English marks: "))
c= float(input("Enter your Physics marks: "))

marks = a+b+c
z= marks/3
print( )
print("Student's Information")
print("----------------------")
print( )
print("Hello,"+name)
print("Here is your total marks:",marks)
print("Your percentage is",z)
if marks >= 240:
    print("YOU got A+....Congratulation.")
elif marks >= 220:
    print("You have got 'B'..Need more practice..")
else:
    print("Fail....Bad luck.")
print("-------------------------")


#!Boolean
for_sale = False
if for_sale:
    print("This item is for sale.")
else:
    print("This item is not for same")

Online = True
if Online:
    print("Player is online.")
else:
    print("Player is offline")



#*** ternary operator(conditional expression)
#? syntax: [on_true] if [expression] else [on_false]
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
'''
if num1 > num2:
    print(num1)
else:
    print(num2)
'''
print(num1 if num1 > num2 else num2) #This is the ternary operator 

#!Logical operator -> and, or, not
# ?large number from 3 numbers using logical operator
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)


