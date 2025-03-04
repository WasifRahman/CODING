
#!Area of Triangle
base = float(input("Enter base: ")) #Don't use int() because it choose the lowest value.
height = float(input("Input height: ")) #Float takes decimal

area = 0.5 * base * height
print("The area of the triangle is",area)



#!Area of Circle
radius = float(input("Enter radius= "))
area = 3.1416 * radius**2
print("The area of Circle is",area)




#!Area of Rectangular
length= float(input("Enter length:"))
width= float(input(("Enter your width:")))

Area= length*width
print("The Area of the Rectangular is", Area)



 #!CIRCUMFERENCE OF A CIRCLE
import math

radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")


#! AREA OF A CIRCLE
import math
radius = float(input("Enter the radius of a circle: "))
area = math.pi * (radius**2) #pow(radius, 2)

print(f"The total area of the circle is {round(area, 3)}cm^2")


 #!HYPOTENUSE 
import math
base = float(input("Enter the base of a right angle triangle: "))
perpendicular = float(input("Enter the perpendicular of the right triangle: ")) 

hypotenuse = math.sqrt(pow(base, 2) + pow(perpendicular, 2))

print(f"The hypotenuse of the right angle triangle is: {hypotenuse}cm")


#!area cal
length = int(input("Enter the length of a rectangular: "))
width = float(input("Enter the width of a rectangular: "))
area = length * width
print(f"The area is {area}cm^2.")

#!Volume cal
length = int(input("Enter the length of a rectangular: "))
width = float(input("Enter the width of a rectangular: "))
height = float(input("Enter the width of a rectangular: "))
volume = length * width * height
print(f"The volume is {volume}cm^3.")

#!Shopping cart
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity
print(f"You have bought {quantity} {item}/s")
print(f"Your total is : ${round(total, 2)}.")  















