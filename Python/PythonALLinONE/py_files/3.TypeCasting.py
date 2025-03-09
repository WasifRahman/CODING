
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


#***Typecasting (or type conversion) in Python refers to converting one data type into another. It is useful when we want to perform operations that require compatible data types.

#! Types of Typecasting
#? Python supports two types of typecasting:
#? 1. **Implicit Typecasting (Automatic Conversion)**
#? 2. **Explicit Typecasting (Manual Conversion)**

#@ 1. Implicit Typecasting (Automatic Conversion)
#?Python automatically converts one data type to another when no data loss occurs.

#$ Example:

#*** Implicit Typecasting Example
a = 10    # Integer
b = 5.5   # Float

result = a + b  # Integer is converted to Float automatically

print(result)  # Output: 15.5
print(type(result))  # Output: <class 'float'>

#@ Explanation:
#?- Python automatically converts `int` to `float` because float has a higher precision.


#*** 2. Explicit Typecasting (Manual Conversion)
#$ Explicit typecasting is when we manually convert one data type to another using built-in functions:
#$ - `int()` - Converts to integer
#$ - `float()` - Converts to float
#$- `str()` - Converts to string
#$ - `list()` - Converts to list
#$ - `tuple()` - Converts to tuple
#$ - `set()` - Converts to set
#$ - `dict()` - Converts to dictionary

#@ Example:
#@ Explicit Typecasting Example
x = "10"  # String
y = "5.5"

#! Convert string to integer
num1 = int(x)
print(num1, type(num1))  # Output: 10 <class 'int'>

#! Convert string to float
num2 = float(y)
print(num2, type(num2))  # Output: 5.5 <class 'float'>

#@ Explanation:
#$ - The string `'10'` is converted to an integer using `int()`.
#$ - The string `'5.5'` is converted to a float using `float()`.

#@ Common Typecasting Scenarios
#! 1. Converting Float to Integer

f = 5.99
int_val = int(f)
print(int_val)  # Output: 5

#? - **Note:** The decimal part is truncated (not rounded).

#!2. Converting Integer to String
num = 100
str_val = str(num)
print(str_val, type(str_val))  # Output: '100' <class 'str'>


#! 3. Converting List to Tuple and Vice Versa
lst = [1, 2, 3]
tup = tuple(lst)
print(tup, type(tup))  # Output: (1, 2, 3) <class 'tuple'>

new_list = list(tup)
print(new_list, type(new_list))  # Output: [1, 2, 3] <class 'list'>


#! 4. Converting String to List
s = "Hello"
list_s = list(s)
print(list_s)  # Output: ['H', 'e', 'l', 'l', 'o']


#! 5. Converting List of Tuples to Dictionary
tuple_list = [("name", "John"), ("age", 30)]
dict_data = dict(tuple_list)
print(dict_data)  # Output: {'name': 'John', 'age': 30}



#***Advanced Typecasting Concepts
#! 1. Using `eval()` for Dynamic Type Conversion

expr = "10 + 5"
result = eval(expr)  # Evaluates the expression as Python code
print(result)  # Output: 15


#! 2. Using `map()` for Bulk Typecasting
str_list = ["1", "2", "3"]
int_list = list(map(int, str_list))
print(int_list)  # Output: [1, 2, 3]


#! 3. JSON String to Dictionary
import json
json_data = '{"name": "Alice", "age": 25}'
dict_data = json.loads(json_data)
print(dict_data)  # Output: {'name': 'Alice', 'age': 25}


#@ Summary
#$ | Function | Converts To |
#$ |----------|------------|
#$ | `int(x)` | Integer |
#$ | `float(x)`| Float |
#$ | `str(x)` | String |
# $| `list(x)` | List |
#$ | `tuple(x)` | Tuple |
#$ | `set(x)` | Set |
#$ | `dict(x)` | Dictionary |

#?Typecasting is an essential concept in Python that allows flexibility in data handling. Understanding when and how to convert types properly ensures smooth coding and prevents errors.




