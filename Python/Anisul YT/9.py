#Pass/ Fail , if else statement

mark=80
if mark>=33:
    print("Result:Pass")
else:
    print("Result:Fail")

#Largest
a=-20
b=10
if a>b:
    print(a)
else:
    print(b)

#Even /odd
d=5
if d%2==0:         #Important to remember (reminder)
    print("Even")
else:
    print("Odd")

#=================IF STATEMENTS
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


#===================EXERCISE1
response = input("What you like food? (Y/N): ")

if response == "y":
    print("Have some food.") 
else:
    print("No food for you.")


#===================EXERCISE 2
name =input("Enter your name: ")

if name == "":
    print("Put a name.")
else:
    print(f"Hello, {name}")

Boolean
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




