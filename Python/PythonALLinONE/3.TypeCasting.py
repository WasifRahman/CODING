
#***Type casting (we can change the type of the variable, we need to do something)
age = 18
actual_age = 17.24 #float(decimal)
print(type(name))
print(type(age))
print(type(actual_age))

#!
#***Type conversion(it means we can change the type of the variable, we need to do something) 
#*Type Conversion(a=2, b=2.0, c="2" and TYPE CONVERSION: c=int(c) , then we can do print(a+b+c)
name = 'Wasif'  
age = 21
gpa = 3.6
student = True
a = None
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))
print(type(a))


#!
num1 = int(float(input("Enter first number:"))) # We use float for decimal number
num2 = int(float(input("Enter second number:")))

result = num1 + num2
print("The print(+) is" ,result)

result = num1 - num2
print("The print(-) is" ,result)

result= num1 * num2
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

#***Explicit casting (we can change the type of the variable, we need to do something)
name = str(name)
print(name)
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


#***Implicit Casting(automatically change the type of the variable, we don't need to do anything)
x =2
y= 2.0
x=x/y
print(x) #float answer

#!
mystrey = "Wasif is a good boy"
print(mystrey) 
print(mystrey[4]) #4th index
print(mystrey[0:21]) #0 to 20
print(mystrey[0:21:2])#character skip 2
print(mystrey[::]) # by deafult 0:full:1
print(mystrey[0:180]) #if we give more than the length of the string it will print the full string
print(mystrey[0:5]) #0 to 4
print(len(mystrey)) #length of the string
print(mystrey[-4:]) #last 4 character
print(mystrey[::-1]) #reverse

print(type(mystrey)) #string
print(mystrey.isalnum())#no space true
print(mystrey.isalpha()) 
#no space sapce alphabet
print(mystrey.endswith("boy")) # because end with boy --bdoy --false
print(mystrey.count("o")) # 3 ta o ase
print(mystrey.capitalize()) # capitalize first letter
print(mystrey.find("is")) #after 6  #find the index of is 
print(mystrey.lower()) 
print(mystrey.upper()) 
print(mystrey.replace("is", "are")) #replace is with are




