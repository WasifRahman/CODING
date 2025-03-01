uname=input("Username: ")
print("Hi,",uname+".",)
a=input("Do you want to play a game,"+uname+"? [Y/N]")
if a == "y":
    print("Take a number between 1 to 10," + uname)
    print("Multiply it by 2," + uname)
    print("Add 8 with the number.")
    print("Subtract: Current number - Original Number")
else:
    print("Oh...Sorry.Do you want to exit?")

b=input("Have you done the math? [Y/N]")
if b == "y":
    print("I have a guess.")
else:
    print("Oops...Sorry.")
print("I think your number is 14.")
