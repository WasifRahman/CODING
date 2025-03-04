
#!            CLASS=1

foodlist = "Chicken, French Fry, Momos, Coke"
name = input("What is your name, Sir?\n")

print("Hello, Welcome to our shop, " +name+ "." "\nWhat you like to order?")
print("In our menu, we have " +foodlist + ".")
order = input()

print("\n\n\nYou have ordered " +order)
print("Thank you so much for coming today, " +name + ".")





#!         CLASS=2
foodlist = "Chicken, French Fry, Momos, Coke"

name = input("What is your name, Sir?\n")

print("Hello, Welcome to our shop, " +name+ "." "\nWhat you like to order?")
print("In our menu, we have " +foodlist + ".")
print("""PRICES: Chicken= 8$
French Fry= 8$
Momos= 8$
Coke= 8$""")
order = input()
number=input("How many you like to order? =>")

price = int(number) * 8

print("\n\n\nYou have ordered " +order)
print("Your total price is " +str(price)+"$.") # or ,price,
print("Sounds good " + name + ", we'll have your " +number+ " " +order+ " ready in a moment.")
print("Thank you so much for coming in today, " +name + ".")





#!           CLASS=3
foodlist = "Chicken, French Fry, Momos, Coke"

name = input("What is your name, Sir?\n")

if name == "Ben":
    print("You are no welcome here. GETOUT!!")
    exit() # EASY WAY
else:
    print("Hello, Welcome to our shop, " +name+ "." "\nWhat you like to order?")
    print("In our menu, we have " +foodlist + ".")
    print("""PRICES: Chicken= 8$
French Fry= 8$
Momos= 8$
Coke= 8$""")
order = input()
number=input("How many you like to order? =>")

price = int(number) * 8

print("\n\n\nYou have ordered " +order)
print("Your total price is " +str(price)+"$.") # or ,price,
print("Sounds good " + name + ", we'll have your " +number+ " " +order+ " ready in a moment.")
print("Thank you so much for coming in today, " +name + ".")






#!            CLASS =4
# foodlist = "Chicken, French Fry, Momos, Coke"

# name = input("What is your name, Sir?\n")

if name == "Ben" or name == "Loki" or name == "Bob":
    print("You are no welcome here. GETOUT!!")
    exit() # EASY WAY
print("Hello, Welcome to our shop, " +name+ ".")
print("In our menu, we have " +foodlist + ".")
print("""PRICES: Chicken= 8$
French Fry= 8$
Momos= 8$
Coke= 8$""")
print("What you like to order?")
order = input()
number=input("How many you like to order? =>")

price = int(number) * 8

print("\n\n\nYou have ordered " +order)
print("Your total price is $" +str(price)+".") # or ,price,
print("Sounds good, " + name + ", we'll have your " +number+ " " +order+ " ready in a moment.")
print("Thank you so much for coming in today, " +name + ".")




 
#!                    CLASS =5
foodlist = "Chicken, French Fry, Momos, Coke"

name = input("What is your name, Sir?\n")

if name == "Ben" or name == "Loki":
    evil= input("Are you EVIL?\n")
    deeds = int(input("How many good deeds have you done today? \n"))
    if evil == "yes" and deeds <= 4:
        print("You are no welcome here. GETOUT!!")
        exit() # EASY WAY

     
print("Hello, Welcome to our shop, " +name+ "." "\nWhat you like to order?")
print("In our menu, we have " +foodlist + ".")
print("""PRICES: Chicken= 8$
French Fry= 8$
Momos= 8$
Coke= 8$""")
order = input()
number=input("How many you like to order? =>")

price = int(number) * 8

print("\n\n\nYou have ordered " +order)
print("Your total price is $" +str(price)+".") # or ,price,
print("Sounds good " + name + ", we'll have your " +number+ " " +order+ " ready in a moment.")
print("Thank you so much for coming in today, " +name + ".")






#!             CLASS=6

foodlist = "Chicken, French Fry, Momos, Coke, Coffee"

name = input("What is your name, Sir?\n")

if name == "Ben" or name == "Loki":
    evil= input("Are you EVIL?\n")
    deeds = int(input("How many good deeds have you done today? \n"))
    if evil == "yes" and deeds <= 4:
        print("You are no welcome here. GETOUT!!")
        exit() # EASY WAY

     
print("Hello, Welcome to our shop, " +name+ ".")
print("In our menu, we have " +foodlist + ".")
print("""PRICES: Chicken= 15$
French Fry= 10$
Momos= 10$
Coke= 5$
Wipped Cream Latte=10$
Regular Latte= 8$
Coffee=16$""")
print("\nWhat you like to order?")


order = input()

if order == "chicken":
    price= 15
elif order == "fry":
    price = 10
elif order == "momos":
    price = 10
elif order == "coke":
    price = 5
elif order == "latte":
    _latte = input("Do you want a regular one or a wipped cream filled latte?  =>")
    if _latte == "regular":
        price = 8
    else:
        price = 10
elif order == "coffee":
    price = 16
else:
    print("We do not have it here.")
    exit()
number=input("How many you like to order? =>")

t_price= price * int(number)


print("\n\n\nYou have ordered " +order)
print("Your total price is $" +str(t_price)+".") # or ,price,
print("Sounds good " + name + ", we'll have your " +number+ " " +order+ " ready in a moment.")
print("Thank you so much for coming in today, " +name + ".")



