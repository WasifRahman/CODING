
#***Type casting
name ="Wasif"
age = 18
actual_age = 17.24 #float(decimal)
print(type(name))
print(type(age))
print(type(actual_age))

#!
num1 = int(float(input("Enter first number:"))) # We use float for decimal number
num2 = int(float(input("Enter second number:")))

result = num1 + num2
print("The print(+) is" ,result)

result = num1 - num2
print("The print(-) is" ,result)

result = num1 * num2
print("The print(*) is" ,result)

result= num1 / num2
print("The print(/) is" ,result)

result= num1 % num2
print("The print(%) is" ,result) #% is for remainder

result= num1 ** num2  
print("The print(%) is" ,result) # here ** is for power

#***Type casting
name= 'Wasif'
age =21 
gpa = 3.6
student = True #Boolean must be capital letter
a = None #None must be capital letter
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))
print(type(a))

#***Explicit casting
age = float(age)
print(age)
gpa = int(gpa)
print(gpa)
student = str(student)
print(student)
print(type(student))
age= bool(age)
print(age)
name=""
name= bool(name)
print(name)


#***Implicit Casting
x =2
y= 2.0
x=x/y
print(x) #float answer

# input name and print it



