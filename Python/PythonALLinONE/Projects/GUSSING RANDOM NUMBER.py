import random #or, from random import randint(memeory save)

number = random.randint(1, 10) #or, number=randint(1,10)
tries = 1

uname = input("Hello, What is your name?")
print("Hello", uname + ".",)

question = input("Would you like to play a game?[y/n]")
if question == "n":
    print("oh..okay")

if question == "y":
    print("I'm thinking of a number between 1 & 10")
    guess = int(input("Have a guess:"))
    if guess > number:
        print("Guess lower..")
if guess < number:
    print("Guess higher..")
while guess != number:
    tries += 1
    guess = int(input("Try again: "))
    if guess < number:
        print("Guess Higher")
if guess == number:
    print("You're right! You win! The number was",number, \
          "and it only", tries, "tries!")
