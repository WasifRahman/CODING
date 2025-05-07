
#*** introduction to function
#!
a = 20
b = 10
sum =a+b
print(sum)

#!
def add1(a, b):
    sum = a + b
    print(sum)
add1(10,60)
add1(10,6)  #bar bar code reuse kora
add1(10,90)
add1(10,50)

#!
def add2(a, b, c):
    sum = a + b + c
    print(sum)
add2(10, 20, 30)
add2(1, 2, 3)

#!
def sub(a, b):
    result = a - b
    print(result)
sub(20, 10)

#!
def message():
    print("hello everyone")
message()


#*** Returning value from function
#!
def add(a, b):
    sum =a + b
    return sum
result = add(20,30)
print("Result:", result)

#!
def add(a, b):
    return a + b

#!
def large_value(a,b):
    if a > b:
        return a
    else:
        return b
    
#? result1 = large_value(20,30)
#? print("Result(large)=", result1)
    #@ or,
print(large_value(20,30))
    #@ or,
#$ maximum = largeNumber
#$ result = add(10,20)
#$ print(result)
#$ print(maximum(20,30))
    #@ or,
def largeNumber(a,b):
    return  a if a > b else b


#*** xargs -> receive any number of parameters -> acts like tuples
#!
def student(id):
    print(id)
student(101)

#!
def student(id, name):
    print(id,name)
student(101,"Wasif")

#! or, 
def student(*details):
    print(details)
    print(details[1])
student(101, "Wasif")  #? *something dile sob print kore dibe, uporer shortcut
student(101, "Rokibul Islam", 3.92) #?tuples er moto

#! 
def add(a,b):
    sum = a + b
    print(sum)
add(20,30)
#$ kintu add(20,30,40) or add(20,30,40,50) print korte parbe na
#@ so shortcut holo xxargs:
#! ALERT: eta holo print korbe sum korbe na
def add(*sum):
    print(sum)
add(20,70)
add(20,70,50)
add(2,7,5)
#!
def add(*number):
    sum = 0
    for num in number:
        sum += num
    print(sum)
add(20,70)
add(20,70,50)
add(2,7,5)



#*** xxargs -> receive any number of parameters -> acts like dictionaries -> key, value
#!
def studentDetails(**details): #? double *
    print(details) #$Dictonary type e print
    print(details["id"]) #$ shudhu id print korbe

studentDetails(id= 101,Name = "Wasif Rahman")


#***Lambda Function
#?A function without name(Anonymous Function)
#? Not powerful as Named Function
#? It can work with single expression / single line of code
#!
def calculate(a,b):
    return a*a + 2*a*b + b*b
print(calculate(2,3))

#@ or shortcut:
print((lambda a,b : a*a + 2*a*b + b*b)(2,3)) #$sintax= (lambda parameter: expression)(value,value){CAREFUL with the brackets}
#@ or,
a = (lambda a,b : a*a + 2*a*b + b*b)(2,3) 
print(a)

#!
print((lambda a : a*a*a)(2)) #$Cube

#*** map function
def square(x):
    return x*x 

num = [1,2,3,4,5]
result = list(map(square,num)) #$ syntax: map(function,iterables) {so, function define korsi, ite. holo numbers gula}
print(result) #$ List akare square print korbe

#*** Filter 
num = [1,2,3,4,5]
result = list(filter(lambda x: x%2 == 0,num)) #$ x(list er number gula) ke 2 dara vag kore 0 na ashle list theke remove kore dibe
print(result)
