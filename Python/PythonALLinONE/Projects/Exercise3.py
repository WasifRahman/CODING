#BMI 1 person
name = input("Enter Your name= ")
height = float(input("Enter your height= "))
weight = float(input("Enter your weight= "))

bmi = weight / (height**2)
print(name)
if bmi < 25:
    print("He is a handsome boy because his BMI is...")
else:
    print("You have to lose some weight because your BMI is....")
print(bmi)
if bmi < 25:
    print("So, he is not over weighted.")
else:
    print("Alas! He is over weighted.")

print("Be Safe, Be fit....")