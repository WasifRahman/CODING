
#**Relation Operators 
a = 30 > 20
print(a)

print(30 > 20)
print(30 < 20)
print(30 >= 20)
print(30 <= 20)
print(30 == 20)
print(30 != 20) #never equal
print("Wasif"=="Wasif")

#***Arithmetic Operators
a=18 # Don't need space
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #reminder after division
print(a//b) #print Whole number / Floor (Closest under whole num) After Division
print(4**2)  # To the power / Exponentiation
# float (point number)

#***assignment operators
a=20    
a +=10  #same==> a = a + 10
a -=10  #same==> a = a - 10
a *=10  #same==> a = a * 10
a /=10  #same==> a = a / 10
a %=10  #same==> a = a % 10
a **=10  #same==> a = a ** 10 or power
print(a)

#*easier way to do the same thing
from math import*
print(max(20, 10))
print(min(20, 10))
print(abs(-4))
print(pow(2, 3))  #To the power
print(sqrt(25))   #Square Root
print(round(5.8)) #Closest whole number
print(floor(5.8)) #Closest under whole number
print(ceil(5.8))  #Closest upper whole number

#!BUILD_IN FUNCTIONS
x= 3.14
y= 4
z= 5
result = round(x)
result = abs(y) # absolute value it means 4 units away from 0
result = pow(4, 3) #power or index
result = max(x, y, z) # maximum value in x, y and z
result = min(x, y, z) # minimum value in x, y and z
print(result)


#!MATH MODULES
import math
x= 9.1
print(math.pi)
print(math.e)
result = math.sqrt(x)
result = math.ceil(x) #IT will round up the number up like 9.1 is 9
result = math.floor(x)
print(result)

#***Logical Operators (not , and , or) think it as gate
print(not False)
print(not True) #False
print(True and True) #True
print(True and False) #False


a = 20
b = 30
print(not (a>b)) #a is not greater than b => False ==> not False => True
print(a>b or a<b)
print(a>b and a<b) #False #both condition must be true
print(a>b and a>b)  #False #both condition must be true
print(a<b or a<b)  #True #both condition must be true
print(a<b and a<b)  #True #both condition must be true
print("OR Operator:", (a==b) or (a>b)) #False #both condition must be true
print("AND Operator:", (a==b) and (a>b)) #False #both condition must be true


p= True
q= False
print(p and q) #False think true as 1 and false as 0
print(p or q) #True
print(not p or q) #False
print(not p and q) #False   #not has higher precedence than and or or
print(not (p and q)) #True
print(not (p or q)) #False #not has higher precedence than and or or


#***Ternary Operators
a=20
b=10

if a>b:
    print(a)
else:
    print(b)

# another way
max= (a if a>b else b)
print("Maximum =" ,max)


# ************************************************Extra----------------------


#****Membership Operators
a = "Wasif"
print("W" in a) #True #in is used to check if a character is in a string
print("W" not in a) #False  #not in is opposite of in
print("W" in a) #True #not in is opposite of in
print("W" not in a) #False #not in is opposite of in

a = [1,2,3,4,5]
print(1 in a) #True #in is used to check if an element is in a list 
print(1 not in a) #False #not in is opposite of in
print(1 in a) #True #in is used to check if an element is in a list
print(1 not in a) #False #not in is opposite of in

a = (1,2,3,4,5)
print(1 in a) #True #in is used to check if an element is in a tuple    
print(1 not in a) #False #not in is opposite of in 
print(1 in a) #True #in is used to check if an element is in a tuple 
print(1 not in a) #False #not in is opposite of in

a = {1,2,3,4,5}
print(1 in a) #True #in is used to check if an element is in a set
print(1 not in a) #False #not in is opposite of in
print(1 in a) #True #in is used to check if an element is in a set
print(1 not in a) #False #not in is opposite of in

a = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}
print(1 in a) #True #in is used to check if a key is in a dictionary
print(1 not in a) #False #not in is opposite of in
print(1 in a) #True #in is used to check if a key is in a dictionary
print(1 not in a) #False #not in is opposite of in




#***Identity Operators ==========================
a = 10  #a is a reference to 10
b = 10  #b is a reference to 10
print(a is b) #True #a and b are pointing to the same object
print(a is not b) #False #a and b are pointing to the same object   #is not is opposite of is   #is is used to compare the memory location of two objects 
print(id(a)) #memory location of a
print(id(b)) #memory location of b #id() is used to get the memory location of an object

a = [1,2,3]
b = [1,2,3]
print(a is b) #False #a and b are not pointing to the same object
print(a is not b) #True #a and b are not pointing to the same object
print(id(a)) #memory location of a
print(id(b)) #memory location of b #id() is used to get the memory location of an object

a = (1,2,3)
b = (1,2,3)
print(a is b) #False #a and b are not pointing to the same object
print(a is not b) #True #a and b are not pointing to the same object
print(id(a)) #memory location of a
print(id(b)) #memory location of b #id() is used to get the memory location of an object

a = {1,2,3}
b = {1,2,3}
print(a is b) #False #a and b are not pointing to the same object
print(a is not b) #True #a and b are not pointing to the same object
print(id(a)) #memory location of a
print(id(b)) #memory location of b #id() is used to get the memory location of an object

a = {1:"one", 2:"two", 3:"three"}
b = {1:"one", 2:"two", 3:"three"}
print(a is b) #False #a and b are not pointing to the same object
print(a is not b) #True #a and b are not pointing to the same object
print(id(a)) #memory location of a
print(id(b)) #memory location of b #id() is used to get the memory location of an object

a = "Wasif"
b = "Wasif"
print(a is b) #True #a and b are pointing to the same object
print(a is not b) #False #a and b are pointing to the same object
print(id(a)) #memory location of a
print(id(b)) #memory location of b #id() is used to get the memory location of an object





#***Bitwise Operators
a = 10
b = 4
print(a & b) #bitwise and operator 
print(a | b) #bitwise or operator  
print(a ^ b) #bitwise xor operator 
print(~a) #bitwise not operator 
print(a << 2) #bitwise left shift operator 
print(a >> 2) #bitwise right shift operator 

a = 10
b = 4
print(bin(a)) #binary of a
print(bin(b)) #binary of b
print(bin(a & b)) #binary of a & b
print(bin(a | b)) #binary of a | b
print(bin(a ^ b)) #binary of a ^ b
print(bin(~a)) #binary of ~a
print(bin(a << 2)) #binary of a << 2
print(bin(a >> 2)) #binary of a >> 2


#***Operator Precedence
#1. Parentheses
#2. Exponentiation
#3. Multiplication, Division, Floor division, Modulus
#4. Addition, Subtraction
#5. Bitwise shift operators
#6. Bitwise AND
#7. Bitwise XOR
#8. Bitwise OR
#9. Comparison operators
#10. Logical operators
#11. Assignment operators
#12. Identity operators
#13. Membership operators
#14. Bitwise NOT
#15. Unary plus and minus
#16. Multiplication, Division, Floor division, Modulus (again)
#17. Addition, Subtraction (again)
#18. Bitwise shift operators (again)
#19. Bitwise AND (again)
#20. Bitwise XOR (again)
#21. Bitwise OR (again)
#22. Comparison operators (again)
#23. Logical operators (again)
#24. Assignment operators (again)
#25. Identity operators (again)
#26. Membership operators (again)
#27. Comma
#28. Lambda

#***Operator Associativity
#1. Exponentiation (Right-to-left)
#2. Unary plus and minus (Right-to-left)
#3. Multiplication, Division, Floor division, Modulus (Left-to-right)
#4. Addition, Subtraction (Left-to-right)
#5. Bitwise shift operators (Left-to-right)
#6. Bitwise AND (Left-to-right)
#7. Bitwise XOR (Left-to-right)
#8. Bitwise OR (Left-to-right)
#9. Comparison operators (Left-to-right)
#10. Logical operators (Left-to-right)
#11. Assignment operators (Right-to-left)
#12. Identity operators (Left-to-right)
#13. Membership operators (Left-to-right)
#14. Comma (Left-to-right)
#15. Lambda (Left-to-right)

#***Operator Overloading
#Operator overloading is the ability to define a function for a specific operator.
#Python supports operator overloading.
#For example, the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.
#This feature in Python that allows the same operator to have different meanings according to the context is called operator overloading.
#So what happens when we use the + operator with two strings?
#The + operator is used to concatenate two strings.
#What happens when we use the + operator with two lists?
#The + operator is used to merge two lists.
#What happens when we use the + operator with two numbers?
#The + operator is used to add two numbers.
#This is an example of operator overloading.

#***Operator Overloading Example
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1 + p2) #Output: (3,5)

#In the above example, we have overloaded the + operator.
#The __add__ method is called when the + operator is used.
#The __str__ method is called whenever the print() function is called.
#The __init__ method is called when the Point class is instantiated.
#The __init__ method is also called the constructor method.
#The __str__ method is called the string representation method.
#The __add__ method is called the operator overloading method.
#The __add__ method takes two arguments self and other.
#The self argument represents the left operand.
#The other argument represents the right operand.
#The __add__ method returns a Point object.
#The x-coordinate of the Point object is the sum of the x-coordinates of the two Point objects.
#The y-coordinate of the Point object is the sum of the y-coordinates of the two Point objects.
#The __str__ method returns the string representation of the Point object.

#***Operator Overloading Example
class Point:
    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return "({0})".format(self.x)

    def __add__(self, other):
        x = self.x + other.x
        return Point(x)

p1 = Point(1000)
p2 = Point(2000)

print(p1 + p2) #Output: (3000)

#In the above example, we have overloaded the + operator.
#The __add__ method is called when the + operator is used.
#The __str__ method is called whenever the print() function is called.
#The __init__ method is called when the Point class is instantiated.
#The __init__ method is also called the constructor method.
#The __str__ method is called the string representation method.
#The __add__ method is called the operator overloading method.
#The __add__ method takes two arguments self and other.
#The self argument represents the left operand.
#The other argument represents the right operand.
#The __add__ method returns a Point object.
#The x-coordinate of the Point object is the sum of the x-coordinates of the two Point objects.
#The __str__ method returns the string representation of the Point object.




#*********************************** Types of Operators in Python(AI):********************

# 1. **Arithmetic Operators**
# 2. **Comparison (Relational) Operators**
# 3. **Logical Operators**
# 4. **Bitwise Operators**
# 5. **Assignment Operators**
# 6. **Identity Operators**
# 7. **Membership Operators**


#*** 1. Arithmetic Operators

#$ | Operator | Description               | Example  |
#$ | -------- | ------------------------- | -------- |
#$ | `+`      | Addition                  | `a + b`  |
#$ | `-`      | Subtraction               | `a - b`  |
#$ | `*`      | Multiplication            | `a * b`  |
#$ | `/`      | Division                  | `a / b`  |
#$ | `%`      | Modulus (Remainder)       | `a % b`  |
#$ | `**`     | Exponentiation (Power)    | `a ** b` |
#$ | `//`     | Floor Division (Quotient) | `a // b` |


#*** 2. Comparison (Relational) Operators

#! Used to compare values and return `True` or `False`.

#$ | Operator | Description              | Example  |
#$ | -------- | ------------------------ | -------- |
#$ | `==`     | Equal to                 | `a == b` |
#$ | `!=`     | Not equal to             | `a != b` |
#$ | `>`      | Greater than             | `a > b`  |
#$ | `<`      | Less than                | `a < b`  |
#$ | `>=`     | Greater than or equal to | `a >= b` |
#$ | `<=`     | Less than or equal to    | `a <= b` |

#@ Example:

a = 10
b = 5

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: True
print(a < b)   # Output: False
print(a >= b)  # Output: True
print(a <= b)  # Output: False

#*** 3. Logical Operators

#! Used to combine conditional statements.

#$ | Operator | Description                                    | Example            |
#$ | -------- | ---------------------------------------------- | ------------------ |
#$ | `and`    | Returns True if both conditions are True       | `a > 5 and b < 10` |
#$ | `or`     | Returns True if at least one condition is True | `a > 5 or b > 10`  |
#$ | `not`    | Reverses the result                            | `not(a > 5)`       |

#@ Example:

a = 10
b = 5

print(a > 5 and b < 10)  # Output: True
print(a > 5 or b > 10)   # Output: True
print(not (a > 5))       # Output: False


#*** 4. Bitwise Operators

#!Used to perform bitwise operations on binary numbers.

#$ | Operator | Description | Example    |     |     |
#$ | -------- | ----------- | ---------- | --- | --- |
#$ | `&`      | Bitwise AND | `a & b`    |     |     |
#$ | \`       | \`          | Bitwise OR | \`a | b\` |
#$ | `^`      | Bitwise XOR | `a ^ b`    |     |     |
#$ | `~`      | Bitwise NOT | `~a`       |     |     |
#$ | `<<`     | Left Shift  | `a << 2`   |     |     |
#$ | `>>`     | Right Shift | `a >> 2`   |     |     |

#@ Example:

a = 5  # 101 in binary
b = 3  # 011 in binary

print(a & b)  # Output: 1 (001)
print(a | b)  # Output: 7 (111)
print(a ^ b)  # Output: 6 (110)
print(~a)     # Output: -6
print(a << 1) # Output: 10 (1010)
print(a >> 1) # Output: 2 (10)


#*** 5. Assignment Operators

#! Used to assign values to variables.

#$ | Operator | Example   | Equivalent To |
#$ | -------- | --------- | ------------- |
#$ | `=`      | `a = 5`   | `a = 5`       |
#$ | `+=`     | `a += 2`  | `a = a + 2`   |
#$ | `-=`     | `a -= 2`  | `a = a - 2`   |
#$ | `*=`     | `a *= 2`  | `a = a * 2`   |
#$ | `/=`     | `a /= 2`  | `a = a / 2`   |
#$ | `%=`     | `a %= 2`  | `a = a % 2`   |
#$ | `**=`    | `a **= 2` | `a = a ** 2`  |
#$ | `//=`    | `a //= 2` | `a = a // 2`  |

#@ Example:

a = 10
a += 5  # Equivalent to a = a + 5
print(a)  # Output: 15


#*** 6. Identity Operators

#! Used to compare memory locations of objects.

#$ | Operator | Description                               | Example      |
#$ | -------- | ----------------------------------------- | ------------ |
#$ | `is`     | Returns True if objects are identical     | `a is b`     |
#$ | `is not` | Returns True if objects are not identical | `a is not b` |

#@ Example:
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # Output: True (same memory location)
print(a is c)  # Output: False (different memory locations)


#*** 7. Membership Operators

#!Used to check if a value exists in a sequence (list, tuple, string, etc.).

#$ | Operator | Description                            | Example      |
#$ | -------- | -------------------------------------- | ------------ |
#$ | `in`     | Returns True if a value is present     | `x in y`     |
#$| `not in` | Returns True if a value is not present | `x not in y` |

#@ Example:
nums = [1, 2, 3, 4]
print(3 in nums)  # Output: True
print(5 not in nums)  # Output: True



#@ Summary Table
#$ | Operator Type | Operators                                       |                           |
#$ | ------------- | ----------------------------------------------- | ------------------------- |
#$ | Arithmetic    | `+`, `-`, `*`, `/`, `%`, `**`, `//`             |                           |
#$ | Comparison    | `==`, `!=`, `>`, `<`, `>=`, `<=`                |                           |
#$ | Logical       | `and`, `or`, `not`                              |                           |
#$ | Bitwise       | `&`, \`                                         | `, `^`, `\~`, `<<`, `>>\` |
#$ | Assignment    | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=` |                           |
#$ | Identity      | `is`, `is not`                                  |                           |
#$ | Membership    | `in`, `not in`                                  |                           |

#? This guide covers all types of operators in Python, focusing on beginner-friendly explanations and gradually introducing advanced topics.








