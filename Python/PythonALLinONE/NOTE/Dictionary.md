# Comprehensive Guide to Dictionaries in Python

## Introduction to Dictionaries

A dictionary in Python is a collection of key-value pairs. Unlike sequences (such as lists or tuples) which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type (strings, numbers, tuples containing immutable objects). Dictionaries are mutable, and are optimized for retrieving the value when you know the key.

## Table of Contents
1. [Dictionary Basics](#dictionary-basics)
2. [Creating Dictionaries](#creating-dictionaries)
3. [Accessing and Modifying Dictionary Elements](#accessing-and-modifying-dictionary-elements)
4. [Dictionary Comprehensions](#dictionary-comprehensions)
5. [Dictionary Methods](#dictionary-methods)
6. [Nested Dictionaries](#nested-dictionaries)
7. [Common Dictionary Operations](#common-dictionary-operations)
8. [Dictionary Performance](#dictionary-performance)
9. [Advanced Dictionary Techniques](#advanced-dictionary-techniques)
10. [Practical Applications](#practical-applications)

## Dictionary Basics

A dictionary is an unordered collection of key-value pairs, where each key must be unique. The basic syntax for a dictionary is:

```python
dictionary = {key1: value1, key2: value2, ...}
```

## Creating Dictionaries

### Basic Dictionary Creation

```python
# Empty dictionary
empty_dict = {}
print(empty_dict)  # Output: {}

# Dictionary with initial values
student = {'name': 'John', 'age': 21, 'courses': ['Math', 'Physics']}
print(student)  # Output: {'name': 'John', 'age': 21, 'courses': ['Math', 'Physics']}

# Using dict() constructor
another_student = dict(name='Alice', age=20, courses=['Biology', 'Chemistry'])
print(another_student)  # Output: {'name': 'Alice', 'age': 20, 'courses': ['Biology', 'Chemistry']}
```

### Using dict() with Iterables

```python
# Creating a dictionary from a list of tuples
items = [('apple', 5), ('banana', 2), ('orange', 3)]
fruit_count = dict(items)
print(fruit_count)  # Output: {'apple': 5, 'banana': 2, 'orange': 3}

# Using zip to create a dictionary from two lists
keys = ['name', 'age', 'job']
values = ['Tom', 25, 'Developer']
person = dict(zip(keys, values))
print(person)  # Output: {'name': 'Tom', 'age': 25, 'job': 'Developer'}

# Creating a dictionary with keys from a sequence and same value
colors = dict.fromkeys(['red', 'green', 'blue'], 0)
print(colors)  # Output: {'red': 0, 'green': 0, 'blue': 0}

# Creating a dictionary with keys from a sequence and default value None
placeholder = dict.fromkeys('abc')
print(placeholder)  # Output: {'a': None, 'b': None, 'c': None}
```

## Accessing and Modifying Dictionary Elements

### Accessing Values

```python
student = {'name': 'John', 'age': 21, 'courses': ['Math', 'Physics']}

# Accessing values using keys
print(student['name'])  # Output: John

# Using get() method - safer, returns None or a default value if key doesn't exist
print(student.get('age'))  # Output: 21
print(student.get('phone'))  # Output: None
print(student.get('phone', 'Not Available'))  # Output: Not Available

# Checking if a key exists
if 'name' in student:
    print("Name exists in the dictionary")  # This will execute

if 'address' in student:
    print("Address exists in the dictionary")  # This won't execute
```

### Modifying Dictionaries

```python
student = {'name': 'John', 'age': 21}

# Adding new key-value pairs
student['email'] = 'john@example.com'
print(student)  # Output: {'name': 'John', 'age': 21, 'email': 'john@example.com'}

# Updating values
student['age'] = 22
print(student)  # Output: {'name': 'John', 'age': 22, 'email': 'john@example.com'}

# Adding multiple key-value pairs using update()
student.update({'phone': '555-1234', 'address': '123 Main St'})
print(student)  
# Output: {'name': 'John', 'age': 22, 'email': 'john@example.com', 'phone': '555-1234', 'address': '123 Main St'}

# Removing items
removed_value = student.pop('phone')  # Removes and returns the value
print(f"Removed: {removed_value}")  # Output: Removed: 555-1234
print(student)  
# Output: {'name': 'John', 'age': 22, 'email': 'john@example.com', 'address': '123 Main St'}

# Remove and return an arbitrary (key, value) pair
item = student.popitem()  # In Python 3.7+, this removes the last item added
print(f"Removed item: {item}")  # Output might be: Removed item: ('address', '123 Main St')
print(student)  
# Output: {'name': 'John', 'age': 22, 'email': 'john@example.com'}

# Deleting a specific key
del student['email']
print(student)  # Output: {'name': 'John', 'age': 22}

# Clearing all items
student.clear()
print(student)  # Output: {}
```

## Dictionary Comprehensions

Dictionary comprehensions provide a concise way to create dictionaries using expressions.

```python
# Basic dictionary comprehension
squares = {x: x*x for x in range(6)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Conditional dictionary comprehension
even_squares = {x: x*x for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Dictionary comprehension with two variables
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston']
populations = [8398748, 3990456, 2705994, 2325502]
city_populations = {city: population for city, population in zip(cities, populations)}
print(city_populations)  
# Output: {'New York': 8398748, 'Los Angeles': 3990456, 'Chicago': 2705994, 'Houston': 2325502}

# Transforming keys and values
word_lengths = {word.upper(): len(word) for word in ['apple', 'banana', 'cherry']}
print(word_lengths)  # Output: {'APPLE': 5, 'BANANA': 6, 'CHERRY': 6}

# Merging two dictionaries with comprehension
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {k: v for d in [dict1, dict2] for k, v in d.items()}
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4} (note: dict2's value for 'b' overwrites dict1's)
```

## Dictionary Methods

### Common Dictionary Methods

```python
student = {'name': 'John', 'age': 21, 'courses': ['Math', 'Physics']}

# Getting all keys, values, and items
keys = student.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'courses'])

values = student.values()
print(values)  # Output: dict_values(['John', 21, ['Math', 'Physics']])

items = student.items()
print(items)  # Output: dict_items([('name', 'John'), ('age', 21), ('courses', ['Math', 'Physics'])])

# Note: keys(), values(), and items() return view objects, which update when the dictionary changes
student['grade'] = 'A'
print(keys)  # Output: dict_keys(['name', 'age', 'courses', 'grade'])

# Converting views to lists
keys_list = list(student.keys())
print(keys_list)  # Output: ['name', 'age', 'courses', 'grade']

# setdefault - returns value for key, or sets it to default and returns default if key doesn't exist
email = student.setdefault('email', 'john@example.com')
print(email)  # Output: john@example.com
print(student)  # Output: {..., 'email': 'john@example.com', ...}

# Using get vs setdefault
# get() retrieves but doesn't modify the dictionary
phone = student.get('phone', '555-1234')
print(phone)  # Output: 555-1234
print('phone' in student)  # Output: False - key wasn't added

# setdefault() retrieves and potentially adds the key-value pair
phone = student.setdefault('phone', '555-1234')
print(phone)  # Output: 555-1234
print('phone' in student)  # Output: True - key was added
```

### Copy Method

```python
original = {'a': 1, 'b': 2, 'c': [1, 2, 3]}

# Shallow copy
shallow_copy = original.copy()
print(shallow_copy)  # Output: {'a': 1, 'b': 2, 'c': [1, 2, 3]}

# Modifying the original
original['a'] = 10
print(original)  # Output: {'a': 10, 'b': 2, 'c': [1, 2, 3]}
print(shallow_copy)  # Output: {'a': 1, 'b': 2, 'c': [1, 2, 3]} - 'a' is independent

# But nested mutable objects are shared
original['c'].append(4)
print(original)  # Output: {'a': 10, 'b': 2, 'c': [1, 2, 3, 4]}
print(shallow_copy)  # Output: {'a': 1, 'b': 2, 'c': [1, 2, 3, 4]} - 'c' is shared

# Deep copy
import copy
deep_copy = copy.deepcopy(original)
original['c'].append(5)
print(original)  # Output: {'a': 10, 'b': 2, 'c': [1, 2, 3, 4, 5]}
print(deep_copy)  # Output: {'a': 10, 'b': 2, 'c': [1, 2, 3, 4]} - 'c' is independent
```

## Nested Dictionaries

Dictionaries can contain other dictionaries, creating hierarchical or tree-like data structures.

```python
# Creating a nested dictionary
employees = {
    'john': {
        'id': 101,
        'position': 'developer',
        'salary': 65000
    },
    'alice': {
        'id': 102,
        'position': 'designer',
        'salary': 60000
    }
}

# Accessing nested values
print(employees['john']['position'])  # Output: developer

# Adding a new employee
employees['bob'] = {'id': 103, 'position': 'manager', 'salary': 75000}

# Modifying nested values
employees['alice']['salary'] = 62000

# Accessing with get() for safety
print(employees.get('charlie', {}).get('salary', 'Employee not found'))  # Output: Employee not found

# Iterating through a nested dictionary
for name, info in employees.items():
    print(f"{name.title()}: {info['position'].title()}, ${info['salary']}")
# Output:
# John: Developer, $65000
# Alice: Designer, $62000
# Bob: Manager, $75000
```

## Common Dictionary Operations

### Looping Through Dictionaries

```python
student = {'name': 'John', 'age': 21, 'courses': ['Math', 'Physics']}

# Iterating through keys (default)
for key in student:
    print(key)
# Output:
# name
# age
# courses

# Iterating through values
for value in student.values():
    print(value)
# Output:
# John
# 21
# ['Math', 'Physics']

# Iterating through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
# Output:
# name: John
# age: 21
# courses: ['Math', 'Physics']
```

### Sorting Dictionaries

```python
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}

# Sorting by keys
sorted_keys = sorted(scores.keys())
print(sorted_keys)  # Output: ['Alice', 'Bob', 'Charlie', 'David']

for key in sorted_keys:
    print(f"{key}: {scores[key]}")
# Output:
# Alice: 85
# Bob: 92
# Charlie: 78
# David: 95

# Sorting by values
sorted_by_score = sorted(scores.items(), key=lambda x: x[1])
print(sorted_by_score)  # Output: [('Charlie', 78), ('Alice', 85), ('Bob', 92), ('David', 95)]

# Creating a sorted dictionary (Python 3.7+ preserves insertion order)
sorted_scores = {k: v for k, v in sorted(scores.items(), key=lambda x: x[1], reverse=True)}
print(sorted_scores)  # Output: {'David': 95, 'Bob': 92, 'Alice': 85, 'Charlie': 78}

# Using sorted items
for name, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{name}: {score}")
# Output:
# David: 95
# Bob: 92
# Alice: 85
# Charlie: 78
```

## Dictionary Performance

Dictionaries in Python are implemented as hash tables, which provide very efficient lookups, inserts, and deletes.

```python
import time
import random

# Comparing dictionary and list performance
size = 10000
values = list(range(size))
random.shuffle(values)

# Dictionary: O(1) lookups
dict_lookup = {i: i for i in values}

# List: O(n) lookups
list_lookup = values.copy()

# Find all items
dict_time_start = time.time()
for i in range(size):
    if i in dict_lookup:  # O(1) lookup
        found = dict_lookup[i]
dict_time = time.time() - dict_time_start

list_time_start = time.time()
for i in range(size):
    if i in list_lookup:  # O(n) lookup
        found = list_lookup[list_lookup.index(i)]
list_time = time.time() - list_time_start

print(f"Dictionary time: {dict_time:.6f} seconds")
print(f"List time: {list_time:.6f} seconds")
print(f"Dictionary is approximately {list_time / dict_time:.2f}x faster")
```

## Advanced Dictionary Techniques

### Default Dictionaries

```python
from collections import defaultdict

# Regular dictionary throws KeyError if key doesn't exist
regular_dict = {}
# Uncommenting the next line would raise a KeyError
# regular_dict['new_key'] += 1

# defaultdict with int as default factory
# When a key is accessed that doesn't exist, int() is called (returning 0)
word_count = defaultdict(int)
words = "apple orange banana apple cherry orange apple".split()

for word in words:
    word_count[word] += 1

print(dict(word_count))  # Output: {'apple': 3, 'orange': 2, 'banana': 1, 'cherry': 1}

# defaultdict with list as default factory
# When a key is accessed that doesn't exist, list() is called (returning [])
groups = defaultdict(list)
people = [
    ('Math', 'Alice'),
    ('Physics', 'Bob'),
    ('Math', 'Charlie'),
    ('History', 'David'),
    ('Physics', 'Eve')
]

for subject, name in people:
    groups[subject].append(name)

print(dict(groups))  
# Output: {'Math': ['Alice', 'Charlie'], 'Physics': ['Bob', 'Eve'], 'History': ['David']}

# defaultdict with custom default factory
def default_value():
    return "Not specified"

user_info = defaultdict(default_value)
user_info['name'] = 'John'
print(user_info['name'])  # Output: John
print(user_info['email'])  # Output: Not specified
```

### Ordered Dictionaries

```python
from collections import OrderedDict

# In Python 3.7+, regular dictionaries maintain insertion order
regular_dict = {'banana': 3, 'apple': 1, 'orange': 2}
print(regular_dict)  # Output in Python 3.7+: {'banana': 3, 'apple': 1, 'orange': 2}

# OrderedDict is still useful for its special methods
ordered = OrderedDict([('banana', 3), ('apple', 1), ('orange', 2)])

# Move_to_end method
ordered.move_to_end('banana')
print(ordered)  # Output: OrderedDict([('apple', 1), ('orange', 2), ('banana', 3)])

# Move to beginning (using move_to_end with last=False)
ordered.move_to_end('banana', last=False)
print(ordered)  # Output: OrderedDict([('banana', 3), ('apple', 1), ('orange', 2)])

# popitem with last=True (default) removes items in LIFO order
item = ordered.popitem()
print(item)  # Output: ('orange', 2)

# popitem with last=False removes items in FIFO order
item = ordered.popitem(last=False)
print(item)  # Output: ('banana', 3)
```

### Counter Dictionary

```python
from collections import Counter

# Creating a Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
color_count = Counter(colors)
print(color_count)  # Output: Counter({'blue': 3, 'red': 2, 'green': 1})

# Creating from a string
letter_count = Counter('mississippi')
print(letter_count)  # Output: Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Creating from a dictionary
counter_from_dict = Counter({'red': 4, 'blue': 2})
print(counter_from_dict)  # Output: Counter({'red': 4, 'blue': 2})

# Updating a Counter
color_count.update(['red', 'yellow', 'red'])
print(color_count)  # Output: Counter({'red': 4, 'blue': 3, 'green': 1, 'yellow': 1})

# Most common elements
print(color_count.most_common(2))  # Output: [('red', 4), ('blue', 3)]

# Elements method - returns an iterator over elements repeating each as many times as its count
elements = list(color_count.elements())
print(elements)  # Output: ['red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'green', 'yellow']

# Arithmetic operations
counter1 = Counter(a=3, b=1)
counter2 = Counter(a=1, b=2)

# Addition - combines counts
print(counter1 + counter2)  # Output: Counter({'a': 4, 'b': 3})

# Subtraction - subtracts counts (drops counts that are zero or negative)
print(counter1 - counter2)  # Output: Counter({'a': 2})

# Intersection - takes the minimum of each element
print(counter1 & counter2)  # Output: Counter({'a': 1, 'b': 1})

# Union - takes the maximum of each element
print(counter1 | counter2)  # Output: Counter({'a': 3, 'b': 2})
```

### ChainMap - Multiple Dictionaries as a Single Mapping

```python
from collections import ChainMap

# Create individual dictionaries
defaults = {'theme': 'Default', 'language': 'English', 'showIndex': True}
user_settings = {'theme': 'Dark'}
command_line_args = {'language': 'Spanish'}

# Combine into a ChainMap
settings = ChainMap(command_line_args, user_settings, defaults)

# Lookups check each collection in order
print(settings['theme'])  # Output: Dark (from user_settings)
print(settings['language'])  # Output: Spanish (from command_line_args)
print(settings['showIndex'])  # Output: True (from defaults)

# Add a new dictionary on top of the chain
temporary_settings = {'theme': 'Light', 'timeout': 30}
settings = settings.new_child(temporary_settings)

print(settings['theme'])  # Output: Light (from temporary_settings)
print(settings['timeout'])  # Output: 30 (from temporary_settings)

# Remove the top dictionary
settings = settings.parents
print(settings['theme'])  # Output: Dark (back to user_settings)

# Access the dictionaries directly
print(settings.maps)  # Output: [{'language': 'Spanish'}, {'theme': 'Dark'}, {'theme': 'Default', 'language': 'English', 'showIndex': True}]
```

### Using Dictionaries as Switch Cases

```python
def perform_operation(operator, x, y):
    operations = {
        'add': lambda: x + y,
        'subtract': lambda: x - y,
        'multiply': lambda: x * y,
        'divide': lambda: x / y if y != 0 else "Cannot divide by zero",
    }
    
    # Get the operation or a default "Operation not found" message
    operation = operations.get(operator, lambda: "Operation not found")
    
    # Execute the function
    return operation()

print(perform_operation('add', 5, 3))  # Output: 8
print(perform_operation('multiply', 5, 3))  # Output: 15
print(perform_operation('divide', 5, 0))  # Output: Cannot divide by zero
print(perform_operation('power', 5, 3))  # Output: Operation not found
```

## Practical Applications

### Building a Simple Cache with Dictionary

```python
def fibonacci_with_cache():
    # Function that calculates Fibonacci numbers with cache
    cache = {}
    
    def fib(n):
        # If we've already calculated this number, return it from cache
        if n in cache:
            return cache[n]
        
        # Base cases
        if n <= 1:
            result = n
        else:
            # Recursive calculation
            result = fib(n-1) + fib(n-2)
        
        # Store result in cache before returning
        cache[n] = result
        return result
    
    return fib

# Create the memoized function
fibonacci = fibonacci_with_cache()

# Calculate some Fibonacci numbers
import time

# Measure time for a large Fibonacci number
start_time = time.time()
result = fibonacci(35)
end_time = time.time()

print(f"Fibonacci(35) = {result}")
print(f"Calculation time: {end_time - start_time:.6f} seconds")

# Without caching, this would be much slower
```

### Creating a Simple Database

```python
def create_student_db():
    students = {}
    
    def add_student(id, name, age=None, courses=None):
        if id in students:
            print(f"Student with ID {id} already exists!")
            return False
        
        students[id] = {
            'name': name,
            'age': age,
            'courses': courses if courses else []
        }
        return True
    
    def get_student(id):
        return students.get(id, None)
    
    def update_student(id, **kwargs):
        if id not in students:
            print(f"Student with ID {id} does not exist!")
            return False
        
        for key, value in kwargs.items():
            if key in students[id]:
                students[id][key] = value
        return True
    
    def delete_student(id):
        if id in students:
            del students[id]
            return True
        return False
    
    def add_course(id, course):
        if id not in students:
            print(f"Student with ID {id} does not exist!")
            return False
        
        if 'courses' not in students[id]:
            students[id]['courses'] = []
        
        if course not in students[id]['courses']:
            students[id]['courses'].append(course)
        return True
    
    def list_all_students():
        return students
    
    # Return the functions that operate on the database
    return {
        'add': add_student,
        'get': get_student,
        'update': update_student,
        'delete': delete_student,
        'add_course': add_course,
        'list_all': list_all_students
    }

# Create and use the student database
db = create_student_db()

# Add students
db['add'](1, "Alice Smith", 20)
db['add'](2, "Bob Johnson", 22, ["Math", "Physics"])

# Get student information
print(db['get'](1))  # Output: {'name': 'Alice Smith', 'age': 20, 'courses': []}

# Update student
db['update'](1, age=21, courses=["Computer Science"])
print(db['get'](1))  # Output: {'name': 'Alice Smith', 'age': 21, 'courses': ['Computer Science']}

# Add a course
db['add_course'](2, "Chemistry")
print(db['get'](2))  # Output: {'name': 'Bob Johnson', 'age': 22, 'courses': ['Math', 'Physics', 'Chemistry']}

# List all students
all_students = db['list_all']()
print("All students:")
for id, info in all_students.items():
    print(f"ID: {id}, Name: {info['name']}, Courses: {', '.join(info['courses'])}")
```

### Word Frequency Analysis

```python
import re
from collections import Counter

def word_frequency_analysis(text):
    # Convert to lowercase and split into words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count word frequencies
    word_counts = Counter(words)
    
    # Get the most common words
    most_common = word_counts.most_common(5)
    print("Most common words:")
    for word, count in most_common:
        print(f"{word}: {count}")
    
    # Calculate statistics
    word_length_sum = sum(len(word) * count for word, count in word_counts.items())
    total_words = sum(word_counts.values())
    avg_word_length = word_length_sum / total_words if total_words > 0 else 0
    
    print(f"\nTotal unique words: {len(word_counts)}")
    print(f"Total words: {total_words}")
    print(f"Average word length: {avg_word_length:.2f} characters")
    
    return word_counts

# Example text for analysis
sample_text = """
Python dictionaries are a fundamental data structure that store elements as key-value pairs.
Dictionaries are mutable, which means they can be changed after creation. Each key in a 
dictionary must be unique and immutable, while values can be of any type. Dictionaries are 
extremely versatile and widely used in Python programming for tasks ranging from simple data 
storage to complex algorithms.
"""

frequency = word_frequency_analysis(sample_text)
```

### Implementing a Simple Graph Using Dictionary

```python
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2, bidirectional=True):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        
        # Add edge from vertex1 to vertex2
        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)
            
        # If bidirectional, add edge from vertex2 to vertex1 as well
        if bidirectional and vertex1 not in self.graph[vertex2]:
            self.graph[vertex2].append(vertex1)
    
    def remove_edge(self, vertex1, vertex2, bidirectional=True):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
        
        if bidirectional and vertex2 in self.graph and vertex1 in self.graph[vertex2]:
            self.graph[vertex2].remove(vertex1)
    
    def remove_vertex(self, vertex):
        if vertex in self.graph:
            # Remove the vertex
            del self.graph[vertex]
            
            # Remove all edges pointing to this vertex
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)
    
    def get_neighbors(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        return []
    
    def breadth_first_search(self, start):
        if start not in self.graph:
            return []
        
        visited = []
        queue = [start]
        
        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.append(current)
                neighbors = self.graph[current]
                for neighbor in neighbors:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
        
        return visited
    
    def depth_first_search(self, start, visited=None):
        if visited is None:
            visited = []
        
        if start not in self.graph:
            return visited
        
        if start not in visited:
            visited.append(start)
            for neighbor in self.graph[start]:
                if neighbor not in visited:
                    self.depth_first_search(neighbor, visited)
        
        return visited
    
    def has_path(self, start, end):
        return end in self.breadth_first_search(start)
    
    def __str__(self):
        result = "Graph:\n"
        for vertex, neighbors in self.graph.items():
            result += f"{vertex}: {neighbors}\n"
        return result

# Create a graph
g = Graph()

# Add vertices and edges
g.add_vertex("A")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.add_edge("D", "E")

print(g)

# Test BFS
print("BFS starting from A:", g.breadth_first_search("A"))

# Test DFS
print("DFS starting from A:", g.depth_first_search("A"))

# Test path finding
print("Path from A to E exists:", g.has_path("A", "E"))
print("Path from E to A exists:", g.has_path("E", "A"))
```

## Conclusion

Python dictionaries are versatile and efficient data structures that serve as the foundation for many Python applications. From basic key-value storage to complex data organization, dictionaries provide an intuitive way to represent and manipulate data