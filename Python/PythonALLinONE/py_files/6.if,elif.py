
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



### **4. Check if a Year is a Leap Year**
#! **Problem:**
#$Write a program that takes a year as input and checks if it is a **leap year** or not.
#? **Leap Year Conditions:**
#? - Divisible by 4.
#? - Not divisible by 100, unless also divisible by 400.

#@ **Solution:**
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


### **6. Simple ATM Withdrawal System**
#! **Problem:**
#$Write a program that asks the user to enter a withdrawal amount. It should check if the balance is sufficient and process the transaction.

#@ **Solution:**
balance = 5000  # Example balance

withdraw = int(input("Enter amount to withdraw: "))

if withdraw > balance:
    print("Insufficient balance.")
elif withdraw <= 0:
    print("Invalid amount entered.")
else:
    balance -= withdraw
    print(f"Withdrawal successful! Remaining balance: {balance}")


### **7. Rock, Paper, Scissors Game**
#! **Problem:**
#$Write a simple **Rock, Paper, Scissors** game where the user plays against the computer.

#@ **Solution:**
import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
user = input("Enter rock, paper, or scissors: ").lower()

if user not in choices:
    print("Invalid choice! Please enter rock, paper, or scissors.")
elif user == computer:
    print(f"Both chose {user}. It's a tie!")
elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
    print(f"You win! {user} beats {computer}.")
else:
    print(f"You lose! {computer} beats {user}.")




### **1. Age-Based Movie Ticket Pricing System**
#! **Problem:**
#$ Create a program that determines the ticket price based on the user's age.
#$ - Below 5 years → Free
#$ - 5-12 years → $10
#$ - 13-60 years → $20
#$ - Above 60 years → $15

#@ **Solution:**
age = int(input("Enter your age: "))

if age < 5:
    price = 0
elif age <= 12:
    price = 10
elif age <= 60:
    price = 20
else:
    price = 15

print(f"Your movie ticket price is: ${price}")


### **2. Login System with Username and Password**
#! **Problem:**
#$Create a simple **login system** where a user enters a username and password. The program should verify the credentials.

#@ **Solution:**
username = "admin"
password = "12345"

user_input = input("Enter username: ")
pass_input = input("Enter password: ")

if user_input == username and pass_input == password:
    print("Login successful!")
elif user_input != username:
    print("Invalid username.")
else:
    print("Invalid password.")


### **3. Simple Discount Calculator**
#! **Problem:**
#$ Create a program that calculates a discount based on the purchase amount.
#$ - Below $50 → No discount
#$ - $50 - $100 → 10% discount
#$ - $100 - $200 → 20% discount
#$ - Above $200 → 30% discount
#@ **Solution:**
amount = float(input("Enter purchase amount: "))

if amount < 50:
    discount = 0
elif amount <= 100:
    discount = 0.10
elif amount <= 200:
    discount = 0.20
else:
    discount = 0.30

final_price = amount - (amount * discount)
print(f"Final price after discount: ${final_price:.2f}")

## **1. Basic Calculator**
#! **Problem:**
#$Create a simple calculator that performs addition, subtraction, multiplication, or division based on user input.

#@ **Solution:**
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Error! Division by zero."
    else:
        result = num1 / num2
else:
    result = "Invalid operation!"

print(f"Result: {result}")


## **3. Password Strength Checker**
#! **Problem:**
#$ Check if a user’s password is **weak, moderate, or strong** based on its length.
#$ - **Less than 6 characters** → Weak
#$ - **6-10 characters** → Moderate
#$ - **More than 10 characters** → Strong

#@ **Solution:**
password = input("Enter a password: ")
length = len(password)

if length < 6:
    print("Weak password! Try making it longer.")
elif length <= 10:
    print("Moderate password! Try adding numbers or symbols.")
else:
    print("Strong password! Good choice.")

## **4. Temperature Converter**
#! **Problem:**
#$Convert temperature between **Celsius** and **Fahrenheit** based on user choice.
#@ **Solution:**
choice = input("Convert to (C)elsius or (F)ahrenheit? ").lower()
temp = float(input("Enter temperature value: "))

if choice == "c":
    converted = (temp - 32) * 5/9
    print(f"Temperature in Celsius: {converted:.2f}°C")
elif choice == "f":
    converted = (temp * 9/5) + 32
    print(f"Temperature in Fahrenheit: {converted:.2f}°F")
else:
    print("Invalid choice!")


## **5. Electricity Bill Calculator**
#! **Problem:**
#$ Calculate an electricity bill based on units consumed.
#$ - **Up to 100 units** → $5 per unit
#$ - **101-200 units** → $7 per unit
#$ - **Above 200 units** → $10 per unit

#@ **Solution:**
units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print(f"Total electricity bill: ${bill}")


## **6. Number Guessing Game**
#! **Problem:**
#$The user has to guess a randomly generated number.

#@ **Solution:**
import random

secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Congratulations! You guessed it right.")
elif guess < secret_number:
    print("Too low! Try again.")
else:
    print("Too high! Try again.")

print(f"The correct number was {secret_number}.")


## **7. Currency Converter**
#! **Problem:**
#$Convert currency between **USD, EUR, and INR** based on user input.
#@ **Solution:**
amount = float(input("Enter amount: "))
currency = input("Convert to (USD, EUR, INR): ").upper()

if currency == "USD":
    converted = amount * 0.013
    print(f"Amount in USD: ${converted:.2f}")
elif currency == "EUR":
    converted = amount * 0.012
    print(f"Amount in EUR: €{converted:.2f}")
elif currency == "INR":
    converted = amount * 82.5
    print(f"Amount in INR: ₹{converted:.2f}")
else:
    print("Invalid currency choice!")


## **9. Hotel Room Booking System**
#! **Problem:**
#$ Assign rooms based on the number of guests.
#$ - **1 person** → Single room
#$ - **2 people** → Double room
#$ - **3 or more** → Family suite

#@ **Solution:**
guests = int(input("Enter number of guests: "))

if guests == 1:
    room = "Single Room"
elif guests == 2:
    room = "Double Room"
else:
    room = "Family Suite"

print(f"Assigned room: {room}")


## **10. Discount Calculator Based on Customer Type**
#! **Problem:**
#$ Apply different discounts based on the **customer type**.
#$ - **Regular Customer** → 5% discount
#$ - **Premium Customer** → 10% discount
#$ - **VIP Customer** → 20% discount

#@ **Solution:**
customer_type = input("Enter customer type (Regular, Premium, VIP): ").lower()
amount = float(input("Enter purchase amount: "))

if customer_type == "regular":
    discount = 0.05
elif customer_type == "premium":
    discount = 0.10
elif customer_type == "vip":
    discount = 0.20
else:
    discount = 0
    print("Invalid customer type! No discount applied.")

final_price = amount - (amount * discount)
print(f"Final price after discount: ${final_price:.2f}")

## **1. Text-Based Adventure Game**
### **Problem:**
#$Create a simple text-based adventure game where the player makes choices to navigate through a haunted house.
### **Solution:**
print("Welcome to the Haunted House! You find yourself in a dark hallway.")
choice1 = input("Do you go 'left' or 'right'? ").lower()

if choice1 == "left":
    choice2 = input("You see a creepy door. Do you 'open' it or 'ignore' it? ").lower()
    if choice2 == "open":
        print("A ghost appears and scares you away! Game Over.")
    else:
        print("You ignore the door and safely exit the house. You win!")

elif choice1 == "right":
    choice2 = input("You find stairs leading down. Do you 'go down' or 'stay'? ").lower()
    if choice2 == "go down":
        print("You find a treasure chest and escape safely. You win!")
    else:
        print("A vampire finds you and you lose! Game Over.")
else:
    print("Invalid choice! Game Over.")


## **2. Banking System (Deposit, Withdraw, Check Balance)**
### **Problem:**
#$Create a simple banking system that allows the user to **deposit, withdraw, and check balance**.
### **Solution:**
balance = 1000  # Initial balance

print("Welcome to the Bank!")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = int(input("Choose an option (1-3): "))

if choice == 1:
    print(f"Your current balance is: ${balance}")
elif choice == 2:
    deposit = float(input("Enter amount to deposit: "))
    if deposit > 0:
        balance += deposit
        print(f"Deposit successful! New balance: ${balance}")
    else:
        print("Invalid amount.")
elif choice == 3:
    withdraw = float(input("Enter amount to withdraw: "))
    if withdraw > balance:
        print("Insufficient funds!")
    elif withdraw <= 0:
        print("Invalid amount!")
    else:
        balance -= withdraw
        print(f"Withdrawal successful! New balance: ${balance}")
else:
    print("Invalid option!")

## **4. Train Ticket Pricing System**
### **Problem:**
#$ A train charges ticket prices based on **age and travel distance**:
#$ - **Children (below 5 years)** → Free
#$ - **Students (5-18 years)** → $0.5 per km
#$ - **Adults (19-60 years)** → $1 per km
#$ - **Seniors (above 60 years)** → $0.7 per km

#$ Calculate the **total ticket cost**.
### **Solution:**

age = int(input("Enter your age: "))
distance = float(input("Enter travel distance (in km): "))

if age < 5:
    price = 0
elif age <= 18:
    price = distance * 0.5
elif age <= 60:
    price = distance * 1
else:
    price = distance * 0.7

print(f"Total ticket cost: ${price:.2f}")

## **5. Smart Home Temperature Controller**
### **Problem:**
#$ A smart home system automatically **adjusts the AC temperature** based on the **room temperature**:
#$ - **Below 18°C** → Increase AC temperature
#$ - **18-25°C** → Maintain temperature
#$ - **Above 25°C** → Decrease AC temperature
### **Solution:**
temperature = float(input("Enter current room temperature (°C): "))

if temperature < 18:
    print("It's too cold! Increasing AC temperature.")
elif temperature <= 25:
    print("Temperature is normal. No change needed.")
else:
    print("It's too hot! Decreasing AC temperature.")


## **6. Online Shopping Discount System**
### **Problem:**
#$ Apply **discounts based on the total purchase amount**:
#$ - **Below $50** → No discount
#$ - **$50 - $100** → 5% discount
#$ - **$101 - $200** → 10% discount
#$ - **Above $200** → 20% discount
### **Solution:**
amount = float(input("Enter total purchase amount: "))

if amount < 50:
    discount = 0
elif amount <= 100:
    discount = 0.05
elif amount <= 200:
    discount = 0.10
else:
    discount = 0.20

final_price = amount - (amount * discount)
print(f"Final price after discount: ${final_price:.2f}")

## **7. Bus Fare Calculator**
### **Problem:**
#$ Calculate bus fare based on **age** and **travel distance**.
#$ - **Children (under 5)** → Free
#$ - **Students (5-18 years)** → $0.3 per km
#$ - **Adults (19-60 years)** → $0.6 per km
#$ - **Seniors (above 60 years)** → $0.4 per km
### **Solution:**
age = int(input("Enter your age: "))
distance = float(input("Enter distance in km: "))

if age < 5:
    fare = 0
elif age <= 18:
    fare = distance * 0.3
elif age <= 60:
    fare = distance * 0.6
else:
    fare = distance * 0.4

print(f"Your bus fare is: ${fare:.2f}")


## **8. Zodiac Sign Finder**
### **Problem:**
#$Ask the user for their **birth month and day**, and determine their **Zodiac sign**.
### **Solution:**
month = input("Enter your birth month: ").lower()
day = int(input("Enter your birth day: "))

if (month == "march" and day >= 21) or (month == "april" and day <= 19):
    zodiac = "Aries"
elif (month == "april" and day >= 20) or (month == "may" and day <= 20):
    zodiac = "Taurus"
elif (month == "may" and day >= 21) or (month == "june" and day <= 20):
    zodiac = "Gemini"
else:
    zodiac = "Unknown (Add more conditions for full zodiac signs)"

print(f"Your Zodiac sign is {zodiac}.")


## **1. AI-Based Chatbot (Rule-Based)**
### **Problem:**
#$Create a simple **rule-based chatbot** that responds to user messages.
### **Solution:**
user_input = input("You: ").lower()

if "hello" in user_input or "hi" in user_input:
    response = "Hello! How can I assist you today?"
elif "how are you" in user_input:
    response = "I'm just a bot, but I'm doing great! How about you?"
elif "your name" in user_input:
    response = "I'm a simple chatbot created using Python!"
elif "bye" in user_input:
    response = "Goodbye! Have a great day!"
else:
    response = "Sorry, I don't understand that."

print(f"Bot: {response}")


## **2. ATM Simulator**
### **Problem:**
#$Simulate an **ATM system** with options for **balance inquiry, withdrawal, and deposit**.
### **Solution:**
balance = 5000  # Initial balance

print("Welcome to the ATM")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = int(input("Choose an option (1-3): "))

if choice == 1:
    print(f"Your balance is: ${balance}")
elif choice == 2:
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"Deposit successful! New balance: ${balance}")
    else:
        print("Invalid deposit amount!")
elif choice == 3:
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds!")
    elif amount <= 0:
        print("Invalid withdrawal amount!")
    else:
        balance -= amount
        print(f"Withdrawal successful! New balance: ${balance}")
else:
    print("Invalid option!")


## **3. Hospital Appointment System**
### **Problem:**
#$A hospital allows patients to book appointments with doctors. Based on the **department** they choose, assign a doctor.
#### **Departments & Assigned Doctors:**
#$ - **Cardiology** → Dr. Smith
#$ - **Dermatology** → Dr. Johnson
#$ - **Neurology** → Dr. Brown
#$ - **General** → Dr. White
### **Solution:**
department = input("Enter department (Cardiology, Dermatology, Neurology, General): ").lower()

if department == "cardiology":
    doctor = "Dr. Smith"
elif department == "dermatology":
    doctor = "Dr. Johnson"
elif department == "neurology":
    doctor = "Dr. Brown"
elif department == "general":
    doctor = "Dr. White"
else:
    doctor = None

if doctor:
    print(f"Appointment confirmed with {doctor}.")
else:
    print("Invalid department!")


## **4. Employee Payroll System**
### **Problem:**
#$Calculate an **employee's salary** based on their role and working hours.
#### **Salary Structure:**
#$ - **Manager** → $50 per hour
#$ - **Engineer** → $40 per hour
#$ - **Intern** → $20 per hour
### **Solution:**
role = input("Enter employee role (Manager, Engineer, Intern): ").lower()
hours_worked = int(input("Enter hours worked: "))

if role == "manager":
    salary = hours_worked * 50
elif role == "engineer":
    salary = hours_worked * 40
elif role == "intern":
    salary = hours_worked * 20
else:
    salary = None

if salary:
    print(f"Total salary: ${salary}")
else:
    print("Invalid role!")

## **5. E-Commerce Shopping Cart System**
### **Problem:**
#$A simple shopping cart system where users can **add products** and see the total bill.
#### **Product Prices:**
#$ - **Laptop** → $1000
#$ - **Phone** → $500
#$ - **Tablet** → $300
### **Solution:**
product = input("Enter product name (Laptop, Phone, Tablet): ").lower()
quantity = int(input("Enter quantity: "))

if product == "laptop":
    price = 1000 * quantity
elif product == "phone":
    price = 500 * quantity
elif product == "tablet":
    price = 300 * quantity
else:
    price = None

if price:
    print(f"Total price: ${price}")
else:
    print("Invalid product!")


## **6. Library Management System**
### **Problem:**
#$A library allows users to **borrow books**. Check if a book is available before issuing it.
#### **Available Books:**
#$ - **Python Programming**
#$ - **Data Science**
#$ - **Artificial Intelligence**
### **Solution:**
book = input("Enter the book you want to borrow: ").lower()

if book == "python programming":
    print("Python Programming book is available. You can borrow it.")
elif book == "data science":
    print("Data Science book is available. You can borrow it.")
elif book == "artificial intelligence":
    print("Artificial Intelligence book is available. You can borrow it.")
else:
    print("Sorry, this book is not available.")


## **7. Movie Ticket Booking System**
### **Problem:**
#$Calculate **movie ticket price** based on age.
#### **Ticket Prices:**
#$ - **Below 5 years** → Free
#$ - **5-12 years** → $8
#$ - **13-60 years** → $12
#$ - **Above 60 years** → $6
### **Solution:**
age = int(input("Enter your age: "))

if age < 5:
    price = 0
elif age <= 12:
    price = 8
elif age <= 60:
    price = 12
else:
    price = 6

print(f"Movie ticket price: ${price}")


## **8. Car Rental System**
### **Problem:**
#$Rent a car based on the **car type and number of rental days**.
#### **Car Rental Prices:**
#$ - **Sedan** → $50 per day
#$ - **SUV** → $80 per day
#$ - **Luxury** → $150 per day
### **Solution:**
car_type = input("Enter car type (Sedan, SUV, Luxury): ").lower()
days = int(input("Enter number of days to rent: "))

if car_type == "sedan":
    price = 50 * days
elif car_type == "suv":
    price = 80 * days
elif car_type == "luxury":
    price = 150 * days
else:
    price = None

if price:
    print(f"Total rental cost: ${price}")
else:
    print("Invalid car type!")


## **9. Job Application System**
### **Problem:**
#$Check if a person is **eligible for a job** based on qualifications and experience.
#### **Job Criteria:**
#$ - **Bachelor’s Degree** → Required
#$ - **Experience:**
#$   - **0-2 years** → Junior Role
#$   - **3-5 years** → Mid-Level Role
#$   - **6+ years** → Senior Role
### **Solution:**
degree = input("Do you have a Bachelor's Degree? (yes/no): ").lower()
experience = int(input("Enter years of experience: "))

if degree == "yes":
    if experience < 3:
        role = "Junior Position"
    elif experience <= 5:
        role = "Mid-Level Position"
    else:
        role = "Senior Position"
    print(f"Congratulations! You are eligible for a {role}.")
else:
    print("Sorry, a Bachelor's degree is required for this job.")

#***********MORE QUESTIONS**********

#### **Problem Statement:**
#$ Create an AI-based exam proctor system that evaluates a student's **behavior during an online exam**.  
#$ - If a student **looks away** from the screen **3 times**, they are given a **warning**.  
#$ - If they look away **5 times**, the exam is **terminated**.  
#$ - If a student tries to **open another tab**, they get an **instant fail**.  
#$ - If no suspicious behavior is detected, the exam continues.  
#@ **Input:** Number of times a student looked away and whether they switched tabs.  
#@ **Output:** Warning, Termination, Fail, or Continue.


### **2. Cybersecurity Login System**
#### **Problem Statement:**
#$ Create a **multi-layer authentication system** where:  
#$ - The user enters a **password**.  
#$ - If the password is incorrect **3 times**, **security questions** are asked.  
#$ - If security questions are answered incorrectly, **access is locked for 24 hours**.  
#$ - If both are correct, **access is granted**.  
#@ **Input:** Password attempts and security question answers.  
#@ **Output:** Access Granted, Security Questions Asked, Account Locked.

### **3. Smart Traffic Light Control**
#### **Problem Statement:**
#$ Develop a **smart traffic light system** that operates based on:  
#$ - **Time of day** (Morning, Afternoon, Evening, Night).  
#$ - **Traffic density** (Low, Medium, High).  
#$ - If **emergency vehicles** are detected, the light **immediately turns green**.  
#$ - If **pedestrians are waiting**, the light **stays red longer**.  
#@ **Input:** Time of day, traffic density, emergency vehicle presence, pedestrian crossing request.  
#@ **Output:** Traffic light status (Green, Yellow, Red).

### **4. Advanced Fraud Detection System**
#### **Problem Statement:**
#$ Develop a fraud detection system for a **banking app**:  
#$ - If a **large transaction** (over $10,000) is detected from an **unfamiliar location**, the system **flags it**.  
#$ - If a **user logs in from a new device** and a large transaction is attempted, the account is **temporarily frozen**.  
#$ - If multiple failed login attempts occur, the account is **locked**.  
#$ - If everything is normal, the transaction is **approved**.  
#@ **Input:** Transaction amount, login device history, location, failed login attempts.  
#@ **Output:** Transaction Approved, Flagged, Frozen, or Account Locked.


### **5. AI Personal Finance Advisor**
#### **Problem Statement:**
#$ Build an **AI finance advisor** that suggests investment strategies based on:  
#$ - **Income level** (Low, Medium, High).  
#$ - **Risk appetite** (Low, Medium, High).  
#$ - **Savings percentage** (Less than 10%, 10-30%, More than 30%).  
#$ - If **high income** but **low savings**, suggest **better savings habits**.  
#$ - If **low risk appetite**, suggest **bonds and fixed deposits**.  
#$ - If **high risk appetite**, suggest **stocks and crypto**.  
#@ **Input:** Income level, risk appetite, savings percentage.  
#@ **Output:** Investment recommendation.

### **6. AI-Based Personalized Workout Generator**
#### **Problem Statement:**
#$ Create a system that generates a **custom workout plan** based on:  
#$ - **Fitness goal** (Weight Loss, Muscle Gain, Endurance).  
#$ - **Current fitness level** (Beginner, Intermediate, Advanced).  
#$ - **Time available per day** (Less than 30 min, 30-60 min, More than 60 min).  
#$ - If **goal is muscle gain** and **beginner**, assign **basic strength training**.  
#$ - If **goal is endurance** and **advanced**, assign **high-intensity running & cycling**.  
#@ **Input:** Fitness goal, fitness level, available time.  
#@ **Output:** Workout plan suggestion.


### **7. AI-Based Resume Screener**
#### **Problem Statement:**
#$ Develop a **resume screening system** for job applications:  
#$ - If the **degree and experience** match, the candidate is **shortlisted**.  
#$ - If **experience is less but skills match**, they are **marked for review**.  
#$ - If **degree is missing but experience is high**, they are **conditionally considered**.  
#$ - If neither **degree nor experience match**, they are **rejected**.  
#@ **Input:** Degree, experience, relevant skills.  
#@ **Output:** Shortlisted, Marked for Review, Conditionally Considered, Rejected.


### **8. AI-Based Disaster Response System**
#### **Problem Statement:**
#$ Create a **disaster response system** that prioritizes rescue missions based on:  
#$ - **Disaster type** (Earthquake, Flood, Fire, Hurricane).  
#$ - **Casualty reports** (Low, Medium, High).  
#$ - **Resources available** (Low, Medium, High).  
#$ - If **casualties are high** and **resources are low**, request **emergency aid**.  
#$ - If **casualties are medium** and **resources are high**, begin **rescue operations**.  
#$ - If **casualties are low**, monitor the situation.  
#@ **Input:** Disaster type, casualty reports, resources available.  
#@ **Output:** Emergency Aid Request, Rescue Operation, Monitor Situation.


### **9. Smart AI Home Security System**
#### **Problem Statement:**
#$ Design a **smart home security system** that:  
#$ - **Locks doors** if **nobody is detected** inside for **more than 10 minutes**.  
#$ - **Turns on lights** if motion is detected at night.  
#$ - **Alerts the owner** if an **unknown face** is detected on security cameras.  
#$ - **Calls authorities** if **multiple failed attempts** to enter are detected.  
#@ **Input:** Motion detection, unknown face detected, failed entry attempts.  
#@ **Output:** Lock Doors, Turn on Lights, Alert Owner, Call Authorities.


### **10. AI-Based Customer Support System**
#### **Problem Statement:**
#$ Develop a **customer support chatbot** that responds based on:  
#$ - **Query type** (Technical Issue, Billing, Account Support, Other).  
#$ - **Customer urgency** (Low, Medium, High).  
#$ - **Account type** (Free, Premium, VIP).  
#$ - If **VIP user** and **high urgency**, immediately **connect to a live agent**.  
#$ - If **technical issue**, offer **troubleshooting steps**.  
#$ - If **billing issue**, direct to **finance department**.  
#$ - If **other**, provide **FAQ links**.  
#@ **Input:** Query type, urgency, account type.  
#@ **Output:** Connect to Agent, Troubleshoot, Redirect to Finance, Provide FAQ.

