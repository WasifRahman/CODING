## Table of Contents
1. [Beginner Level](#beginner-level)
2. [Intermediate Level](#intermediate-level)
3. [Advanced Level](#advanced-level)
4. [Projects](#projects)

## Beginner Level

### 1. Variables and Data Types

Python variables store data that can be used and manipulated throughout your program. Python has several built-in data types:

```python
# Strings - text enclosed in quotes
name = "Python Learner"
print(name)  # Output: Python Learner

# Integers - whole numbers
age = 25
print(age)  # Output: 25

# Floating point numbers - decimal numbers
height = 5.9
print(height)  # Output: 5.9

# Boolean - True or False
is_student = True
print(is_student)  # Output: True

# Lists - ordered, mutable collections
hobbies = ["reading", "coding", "hiking"]
print(hobbies)  # Output: ['reading', 'coding', 'hiking']

# Dictionaries - key-value pairs
person = {"name": "Alex", "age": 30, "city": "New York"}
print(person)  # Output: {'name': 'Alex', 'age': 30, 'city': 'New York'}
```

### 2. Basic Operators

Operators perform operations on variables and values:

```python
# Arithmetic operators
a = 10
b = 3

print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.3333...
print(a % b)  # Modulus (remainder): 1
print(a ** b)  # Exponentiation: 1000
print(a // b)  # Floor division: 3

# Comparison operators
print(a == b)  # Equal to: False
print(a != b)  # Not equal to: True
print(a > b)   # Greater than: True
print(a < b)   # Less than: False
print(a >= b)  # Greater than or equal to: True
print(a <= b)  # Less than or equal to: False

# Logical operators
x = True
y = False
print(x and y)  # Logical AND: False
print(x or y)   # Logical OR: True
print(not x)    # Logical NOT: False
```

### 3. Control Flow

Control flow statements determine the order in which code executes:

```python
# If-elif-else statements
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")
# Output: Grade: B

# While loops
count = 0
while count < 5:
    print(count)
    count += 1
# Output: 0 1 2 3 4

# For loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple banana cherry

# Range function
for i in range(3):
    print(i)
# Output: 0 1 2

# Break and continue
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Stop at 7
    print(i)
# Output: 0 1 2 4 5 6
```

### 4. Functions

Functions are reusable blocks of code that perform specific tasks:

```python
# Basic function
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")  # Output: Hello, Alice!

# Function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # Output: 8

# Default parameter values
def greet_with_message(name, message="Good day"):
    print(f"{message}, {name}!")

greet_with_message("Bob")  # Output: Good day, Bob!
greet_with_message("Charlie", "Welcome")  # Output: Welcome, Charlie!

# *args for variable number of arguments
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4))  # Output: 10

# **kwargs for variable keyword arguments
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="David", age=35, job="Developer")
# Output:
# name: David
# age: 35
# job: Developer
```

### 5. Lists and List Comprehensions

Lists are versatile data structures for storing collections of items:

```python
# List operations
numbers = [1, 2, 3, 4, 5]
print(len(numbers))      # Length: 5
print(numbers[0])        # First element: 1
print(numbers[-1])       # Last element: 5
print(numbers[1:3])      # Slicing: [2, 3]

# List methods
numbers.append(6)        # Add to end: [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)     # Insert at index: [0, 1, 2, 3, 4, 5, 6]
numbers.remove(3)        # Remove value: [0, 1, 2, 4, 5, 6]
popped = numbers.pop()   # Remove and return last: 6, list becomes [0, 1, 2, 4, 5]
numbers.sort()           # Sort in place: [0, 1, 2, 4, 5]
numbers.reverse()        # Reverse in place: [5, 4, 2, 1, 0]

# List comprehensions
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # Output: [4, 16, 36, 64, 100]
```

### 6. Dictionaries and Sets

Dictionaries and sets are powerful data structures for unique items and key-value pairs:

```python
# Dictionary operations
student = {"name": "Emma", "age": 22, "major": "Computer Science"}
print(student["name"])  # Access by key: Emma
student["gpa"] = 3.8    # Add new key-value pair
student["age"] = 23     # Modify existing value

# Dictionary methods
keys = student.keys()        # Get all keys
values = student.values()    # Get all values
items = student.items()      # Get all key-value pairs
student.pop("gpa")           # Remove key-value pair
student.get("major", "N/A")  # Safe access with default value

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Sets
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)  # Check membership: True

# Set operations
more_fruits = {"orange", "banana", "kiwi"}
all_fruits = fruits.union(more_fruits)  # Union
common_fruits = fruits.intersection(more_fruits)  # Intersection
unique_to_fruits = fruits.difference(more_fruits)  # Difference

# Set comprehension
even_set = {x for x in range(10) if x % 2 == 0}
print(even_set)  # Output: {0, 2, 4, 6, 8}
```

### 7. String Manipulation

Strings in Python are versatile with many built-in methods:

```python
# String methods
text = "Hello, Python World!"
print(len(text))                 # Length: 20
print(text.upper())              # Uppercase: HELLO, PYTHON WORLD!
print(text.lower())              # Lowercase: hello, python world!
print(text.replace("Hello", "Hi"))  # Replace: Hi, Python World!
print(text.split(","))           # Split: ['Hello', ' Python World!']
print(text.find("Python"))       # Find substring: 7 (index)
print("Python" in text)          # Membership test: True

# String formatting
name = "Alice"
age = 30
# f-string (Python 3.6+)
print(f"{name} is {age} years old")  # Alice is 30 years old
# format() method
print("{} is {} years old".format(name, age))  # Alice is 30 years old
# % operator
print("%s is %d years old" % (name, age))  # Alice is 30 years old

# Multiline strings
multiline = """
This is a
multiline string
in Python
"""
print(multiline)
```

### 8. File Handling

Python can work with files for reading and writing data:

```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, file handling in Python!\n")
    file.write("This is a second line.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes the newline

# Appending to a file
with open("example.txt", "a") as file:
    file.write("\nThis line is appended.")

# Working with CSV files
import csv

# Writing CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "Boston"])

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

## Intermediate Level

### 9. Exception Handling

Exception handling allows your program to gracefully handle errors:

```python
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    num = int("abc")
except ValueError:
    print("Invalid conversion")
except ZeroDivisionError:
    print("Cannot divide by zero")
except:
    print("Something else went wrong")

# try-except-else-finally
try:
    num = int("123")
except ValueError:
    print("Invalid conversion")
else:
    print(f"Conversion successful: {num}")
finally:
    print("This always executes")

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age is too high")
    return age

try:
    validate_age(-5)
except ValueError as error:
    print(error)  # Output: Age cannot be negative

# Creating custom exceptions
class CustomError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self.message)

try:
    raise CustomError("Something went wrong", 500)
except CustomError as e:
    print(f"Error {e.code}: {e.message}")
```

### 10. Object-Oriented Programming (OOP)

OOP in Python helps you organize and structure your code using classes and objects:

```python
# Basic class definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        return f"Hello, my name is {self.name}"

# Creating objects
person1 = Person("Alice", 30)
print(person1.name)   # Output: Alice
print(person1.greet())  # Output: Hello, my name is Alice

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        
    def study(self):
        return f"{self.name} is studying"

student1 = Student("Bob", 22, "S12345")
print(student1.greet())  # Output: Hello, my name is Bob
print(student1.study())  # Output: Bob is studying

# Encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute
        self.__balance = balance  # Private attribute
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return amount
        return 0
            
    def get_balance(self):
        return self.__balance

account = BankAccount("123456", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

# Polymorphism
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

def make_sound(animal):
    return animal.sound()

dog = Dog()
cat = Cat()
print(make_sound(dog))  # Output: Woof!
print(make_sound(cat))  # Output: Meow!

# Special (magic/dunder) methods
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output: Vector(5, 7)
print(len(v1))  # Output: 3
```

### 11. Modules and Packages

Modules and packages help you organize and reuse code:

```python
# Using built-in modules
import math

print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.141592653589793

# Importing specific functions
from math import sqrt, sin
print(sqrt(25))  # Output: 5.0
print(sin(0))    # Output: 0.0

# Aliasing imports
import math as m
print(m.cos(0))  # Output: 1.0

from datetime import datetime as dt
print(dt.now())  # Current date and time

# Creating and using your own module
# Save this in mymodule.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# In another file
import mymodule

print(mymodule.greet("World"))  # Output: Hello, World!
print(mymodule.add(3, 4))       # Output: 7

# Creating a package
# Directory structure:
# mypackage/
#   __init__.py
#   module1.py
#   module2.py

# In module1.py
def function1():
    return "Function 1"

# In module2.py
def function2():
    return "Function 2"

# In __init__.py
from . import module1
from . import module2

# Using the package
import mypackage

print(mypackage.module1.function1())  # Output: Function 1
print(mypackage.module2.function2())  # Output: Function 2

# Or with direct imports
from mypackage.module1 import function1
print(function1())  # Output: Function 1
```

### 12. Working with Date and Time

Python has built-in modules for handling date and time:

```python
import datetime

# Current date and time
now = datetime.datetime.now()
print(now)  # Output: 2023-03-09 14:30:45.123456

# Creating date objects
date1 = datetime.date(2023, 3, 9)
print(date1)  # Output: 2023-03-09

# Creating time objects
time1 = datetime.time(14, 30, 45)
print(time1)  # Output: 14:30:45

# Formatting dates
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Output: 2023-03-09 14:30:45
print(now.strftime("%A, %B %d, %Y"))       # Output: Thursday, March 09, 2023

# Parsing strings to dates
date_string = "2023-03-09 14:30:45"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_date)  # Output: 2023-03-09 14:30:45

# Date calculations
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
print(tomorrow)  # Output: 2023-03-10

one_week_ago = datetime.date.today() - datetime.timedelta(weeks=1)
print(one_week_ago)  # Output: 2023-03-02

# Time differences
date1 = datetime.datetime(2023, 3, 1)
date2 = datetime.datetime(2023, 3, 9)
diff = date2 - date1
print(diff.days)  # Output: 8
print(diff.seconds)  # Output: 0

# Working with timezones
from datetime import datetime
import pytz  # You might need to install this: pip install pytz

# Current time in UTC
utc_now = datetime.now(pytz.UTC)
print(utc_now)  # Output: 2023-03-09 19:30:45.123456+00:00

# Convert to a different timezone
ny_tz = pytz.timezone('America/New_York')
ny_time = utc_now.astimezone(ny_tz)
print(ny_time)  # Output: 2023-03-09 14:30:45.123456-05:00
```

### 13. Regular Expressions

Regular expressions help you search and manipulate text patterns:

```python
import re

# Basic pattern matching
text = "The quick brown fox jumps over the lazy dog"
pattern = r"fox"
match = re.search(pattern, text)
if match:
    print(f"Found '{pattern}' at position {match.start()}")
# Output: Found 'fox' at position 16

# Finding all occurrences
text = "The fox jumps over the dog. The fox is quick."
pattern = r"fox"
matches = re.findall(pattern, text)
print(matches)  # Output: ['fox', 'fox']

# Using character classes
text = "The year is 2023, and the code is ABC-1234"
pattern = r"\d+"  # One or more digits
matches = re.findall(pattern, text)
print(matches)  # Output: ['2023', '1234']

# Using special sequences
text = "Email me at user@example.com or admin@website.org"
pattern = r"\w+@\w+\.\w+"  # Simple email pattern
matches = re.findall(pattern, text)
print(matches)  # Output: ['user@example.com', 'admin@website.org']

# Groups and capturing
text = "John Smith: 555-123-4567"
pattern = r"(\w+ \w+): (\d{3}-\d{3}-\d{4})"
match = re.search(pattern, text)
if match:
    print(f"Name: {match.group(1)}, Phone: {match.group(2)}")
# Output: Name: John Smith, Phone: 555-123-4567

# Substitution
text = "The fox jumps over the dog"
replaced = re.sub(r"fox", "cat", text)
print(replaced)  # Output: The cat jumps over the dog

# Splitting text
text = "apple,banana;orange,grape;pear"
split_text = re.split(r"[,;]", text)  # Split by comma or semicolon
print(split_text)  # Output: ['apple', 'banana', 'orange', 'grape', 'pear']
```

### 14. Lambda Functions and Functional Programming

Python supports functional programming concepts like lambda functions, map, filter, and reduce:

```python
# Lambda functions (anonymous functions)
add = lambda a, b: a + b
print(add(5, 3))  # Output: 8

# Using lambda with sorted()
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
sorted_students = sorted(students, key=lambda student: student["grade"], reverse=True)
print(sorted_students)
# Output: [{'name': 'Bob', 'grade': 92}, {'name': 'Alice', 'grade': 85}, {'name': 'Charlie', 'grade': 78}]

# map() function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Using map with a regular function
def celsius_to_fahrenheit(c):
    return 9/5 * c + 32

celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(celsius_to_fahrenheit, celsius))
print(fahrenheit)  # Output: [32.0, 50.0, 68.0, 86.0, 104.0]

# filter() function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # Output: [2, 4, 6, 8, 10]

# reduce() function
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120 (1*2*3*4*5)

# Combining functional techniques
words = ["apple", "banana", "cherry", "date", "elderberry"]
result = list(
    map(
        lambda s: s.upper(),
        filter(lambda s: len(s) > 5, words)
    )
)
print(result)  # Output: ['BANANA', 'CHERRY', 'ELDERBERRY']
```

### 15. Iterators and Generators

Iterators and generators help you work with data sequences efficiently:

```python
# Iterators
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3

# Creating an iterator class
class CountDown:
    def __init__(self, start):
        self.start = start
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# Using the iterator
countdown = CountDown(5)
for i in countdown:
    print(i)  # Output: 5 4 3 2 1

# Basic generator function
def simple_generator():
    yield 1
    yield 2
    yield 3

for value in simple_generator():
    print(value)  # Output: 1 2 3

# Generator for Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for number in fibonacci(10):
    print(number)  # Output: 0 1 1 2 3 5 8 13 21 34

# Generator expressions
squares_gen = (x**2 for x in range(5))
for square in squares_gen:
    print(square)  # Output: 0 1 4 9 16

# Using generators for memory efficiency
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Usage (assuming large_file.txt exists)
# for line in read_large_file("large_file.txt"):
#     print(line)
```

### 16. Decorators

Decorators modify or enhance functions without changing their code:

```python
# Basic decorator
def simple_decorator(func):
    def wrapper():
        print("Something happens before the function is called.")
        func()
        print("Something happens after the function is called.")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something happens before the function is called.
# Hello!
# Something happens after the function is called.

# Decorator with arguments
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, Keyword arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

result = add(3, 5, keyword=True)
# Output: Arguments: (3, 5), Keyword arguments: {'keyword': True}

# Decorator with parameters
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
# Output: ['Hello, Alice!', 'Hello, Alice!', 'Hello, Alice!']

# Multiple decorators
def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def format_text(text):
    return text

print(format_text("Hello, World!"))
# Output: <b><i>Hello, World!</i></b>

# Class as a decorator
class Timer:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        import time
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"{self.func.__name__} took {end - start:.5f} seconds to run")
        return result

@Timer
def slow_function():
    import time
    time.sleep(1)
    return "Function completed"

print(slow_function())
# Output: slow_function took 1.00XXX seconds to run
# Function completed
```

## Advanced Level

### 17. Context Managers

Context managers help you manage resources properly:

```python
# Using with statement with built-in context managers
with open("example.txt", "w") as file:
    file.write("Hello, World!")
# File is automatically closed after the block

# Creating a context manager using a class
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return True to suppress exceptions, False otherwise
        return False

# Using the custom context manager
with FileManager("example.txt", "w") as file:
    file.write("Using custom context manager")

# Creating a context manager using contextlib
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()

# Using the contextlib-based context manager
with file_manager("example.txt", "w") as file:
    file.write("Using contextlib context manager")

# Nested context managers
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    content = infile.read()
    outfile.write(content.upper())

# Context manager for timing
import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Elapsed time: {end - start:.5f} seconds")

# Using the timer context manager
with timer():
    # Some time-consuming operation
    time.sleep(1)
# Output: Elapsed time: 1.00XXX seconds
```

### 18. Multithreading and Multiprocessing

Python provides modules for concurrent execution:

```python
# Threading for I/O-bound tasks
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(0.5)
        print(f"Number {i}")

def print_letters():
    for letter in 'ABCDE':
        time.sleep(0.5)
        print(f"Letter {letter}")

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Threading example completed")

# Thread with arguments
def worker(name, delay):
    for i in range(3):
        time.sleep(delay)
        print(f"Worker {name}: Step {i}")

# Create and start threads with arguments
thread1 = threading.Thread(target=worker, args=('One', 1))
thread2 = threading.Thread(target=worker, args=('Two', 0.5))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

# Multiprocessing for CPU-bound tasks
import multiprocessing

def calculate_square(numbers, result, index):
    result[index] = sum(n * n for n in numbers)

if __name__ == "__main__":
    numbers_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result_array = multiprocessing.Array('i', 3)
    
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=calculate_square, 