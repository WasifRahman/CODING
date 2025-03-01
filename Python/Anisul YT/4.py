# #Area of Triangle
base = float(input("Enter base: ")) #Don't use int() because it choose the lowest value.
height = float(input("Input height: ")) #Float takes decimal

area = 0.5 * base * height
print("The area of the triangle is",area)



#Area of Circle
radius = float(input("Enter radius= "))
area = 3.1416 * radius**2
print("The area of Circle is",area)




#Area of Rectangular
length= float(input("Enter length:"))
width= float(input(("Enter your width:")))

Area= length*width
print("The Area of the Rectangular is", Area)


#                    Ogmanted Operator
friends = 10

friends = friends + 1
friends += 1
friends = friends - 2
friends -= 2
friends = friends * 3
friends *= 3
friends = friends/ 2
friends /= 2
friends = friends ** 2
friends **= 2
remainder = friends % 3

print(friends)
print(remainder)




#                 BUILD_IN FUNCTIONS
x= 3.14
y= 4
z= 5

result = round(x)
result = abs(y) # absolute value it means 4 units away from 0
result = pow(4, 3) #power or index
result = max(x, y, z) # maximum value in x, y and z
result = min(x, y, z) # minimum value in x, y and z

print(result)


#                   MATH MODULES
import math
x= 9.1

print(math.pi)
print(math.e)
result = math.sqrt(x)
result = math.ceil(x) #IT will round up the number up like 9.1 is 9
result = math.floor(x)

print(result)



 #        EXERCISE#1 CIRCUMFERENCE OF A CIRCLE
import math

radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")


#         EXERCISE#2 AREA OF A CIRCLE
import math
radius = float(input("Enter the radius of a circle: "))
area = math.pi * (radius**2) #pow(radius, 2)

print(f"The total area of the circle is {round(area, 3)}cm^2")


 #         EXERCISE#3 HYPOTENUSE 
import math
base = float(input("Enter the base of a right angle triangle: "))
perpendicular = float(input("Enter the perpendicular of the right triangle: ")) 

hypotenuse = math.sqrt(pow(base, 2) + pow(perpendicular, 2))

print(f"The hypotenuse of the right angle triangle is: {hypotenuse}cm")

















