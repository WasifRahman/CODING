
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
    print("You have got 'B'..Need more practise..")
else:
    print("Fail....Bad luck.")
print("-------------------------")




#Input Function
name = input("Enter your name: ")
print(f"Hello {name}.")

age = float(input("Enter your age: "))
# age = int(age) + 1
print(f"YOu are {age} years old.")

#mad libs game
adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an adjective: ")

print(f'Today I went to a {adjective1} zoo.')
print(f"In an exhibit, I saw {noun}.")
print(f"{noun} was {adjective2} and {verb}ing.")
print(f"I was {adjective3}.")


#area cal
length = int(input("Enter the length of a rectangular: "))
width = float(input("Enter the width of a rectangular: "))
area = length * width
print(f"The area is {area}cm^2.")

#Volume cal
length = int(input("Enter the length of a rectangular: "))
width = float(input("Enter the width of a rectangular: "))
height = float(input("Enter the width of a rectangular: "))
volume = length * width * height
print(f"The volume is {volume}cm^3.")

#Shopping cart
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity
print(f"You have bought {quantity} {item}/s")
print(f"Your total is : ${round(total, 2)}.")  







