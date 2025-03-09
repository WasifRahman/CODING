
#***LISTING(ARRAY)***
#?List is a collection which is ordered and changeable. Allows duplicate members, and is written with square brackets.
#?Array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together.
#?Array is a fixed size data structure while Python lists are dynamic.

camping_list= ["knife", "tent" , "oil", "water", "pi"]
print("He")
print(type(camping_list))

camp_sit = ["Crystal Lake", 404, 89.3, True] #string , integer, float, boolean

you= camping_list[2] #?camping_list[-3] 
me = camping_list[0] #?camping_list[-5]
print(you) #?print the value of the index
print(me) #?print the value of the index
print(camping_list) #?print the full list
print(camp_sit[-1]) #?True
#***List Slicing
print(camp_sit[0:3]) #?0 to 2 
print(camp_sit[0:3:2]) #?character skip 2
print(camp_sit[::]) #?by default 0:full:1
print(camp_sit[0:180]) #?if we give more than the length of the string it will print the full string
print(camping_list[0:5]) #?0 to 4
print(camping_list[-1]) #?print the last element
print(len(camping_list)) #?length of the list
print(camping_list[-4:]) #?print the last 4 element
print(camping_list[-5:]) #?print the last 5 element
print(camping_list[-5:-1]) #?print the 0 to 3 element
print(camping_list[-5:-1:2]) #?print the 0 to 3 element with skip 2
print(camping_list[-5:5]) #?print the 0 to 4 element
print(camping_list[-5:5:2]) #?print the 0 to 4 element with skip 2
print(camping_list[-5:180]) #?print the 0 to 4 element
print(camping_list[-5:180:2]) #?print the 0 to 4 element with skip 2


#!===================EXERCISE 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:5]) #print 2 to 4
print(a[0:5]) #print 1 to 4


#***lIST SLICING***
#?List slicing in Python is a feature that allows us to extract a subset of elements from a list.
#?List slicing is a flexible tool to build new lists out of an existing list.



#***LIST METHODS***
#?append()	Adds an element at the end of the list
#?clear()	Removes all the elements from the list
#?copy()	Returns a copy of the list
#?count()	Returns the number of elements with the specified value
#?extend()	Add the elements of a list (or any iterable), to the end of the current list
#?index()	Returns the index of the first element with the specified value
#?insert()	Adds an element at the specified position
#?pop()	Removes the element at the specified position
#?remove()	Removes the item with the specified value
#?reverse()	Reverses the order of the list
#?sort()	Sorts the list
camping_list.append("knife") #add the element at the end of the list
print(camping_list) #print the full list
camping_list.clear() #remove all the elements from the list
print(camping_list) #print the full list
camping_list= ["knife", "tent" , "oil", "water", "pi"]
print(camping_list) #print the full list
camping_list2 = camping_list.copy() #copy the list
print(camping_list2) #print the full list
print(camping_list.count("knife")) #count the number of the element
camping_list.extend(camping_list2) #add the elements of a list to the end of the current list
print(camping_list) #print the full list
print(camping_list.index("tent")) #print the index of the element
camping_list.insert(2, "fire") #add an element at the specified position
print(camping_list) #print the full list
camping_list.pop(2) #remove the element at the specified position
print(camping_list) #print the full list
camping_list.remove("oil") #remove the item with the specified value
print(camping_list) #print the full list
camping_list.reverse() #reverse the order of the list
print(camping_list) #print the full list
camping_list.sort() #sort the list
print(camping_list) #print the full list
camping_list.sort(reverse=True) #sort the list in reverse order
print(camping_list) #print the full list
print(camping_list2) #print the full
camping_list2.append("fire") #add the element at the end of the list
print(camping_list2) #print the full list
camping_list2.sort() #sort the list
print(camping_list2) #print the full list


#! Print the list element from 1 to last(etc)
subjects = ["Wasif", "c", "c++", "Python", "android", "OS"]

for x in subjects:
    print(x) #?print the list element from 1 to last(etc) or print(subjests) diyeo kora jay

for x in subjects:
    print(x) #?print the list element from 1 to last(etc)
    if x == "Python":
        break #?break the loop when the condition is true  

print(subjects[0]) #?print the first element ***
print(subjects[1]) #?print the second element ***
print(subjects[2:]) #?print the 3rd to last element***
print(subjects[:3]) #?print the 0 to 2 element***
print(subjects[2:4]) #?print the 2 to 3 element***
print(subjects[-4:]) #?print the last 4 element. last theke 4th ta ***
print(subjects[-5:]) #?print the last 5 element. last theke 5th ta
print(subjects[-5:-1]) #?print the 0 to 3 element. last theke 5th ta theke 1st ta
print(subjects[-5:-1:2]) #?print the 0 to 3 element with skip 2. last theke 5th ta theke 1st ta with skip 2
print(subjects[::-1]) #?print the reverse element
print(subjects[::2]) #?print the element with skip 2  

#! List element check 
print("swift" not in subjects) #?OUTPUT:TRUE .swift is not in the list
print("Wasif" in subjects) #?OUTPUT:TRUE .Wasif is in the list

#! List element add, multiply, delete
subjects[2] = "Java" #?update the 2nd element
del subjects[2] #?delete the 2nd element
subjects.append("Java") #?add the element in the list
subjects.insert(2, "Java") #?insert the element in the list
subjects.remove("Java") #?remove the element in the list
subjects.sort() #?sort the element in the list
subjects.pop(2) #?pop the element in the list
subjects1 = subjects.copy() #?copy the element in the list
print(subjects.index("Python")) #?print the index of the element
print(subjects.count("Python")) #?print the count of the element
subjects.clear() #?clear the element in the list
print(subjects + ["swift", 27]) #?add the element in the list ***
print(subjects * 3) #?multiply the list element. List er item gula 3 bar print korbe ***

#!
sub = ["C", "C++", "Java", "Basic", "C"]
print(len(sub)) #?print the length of the list
sub.append("TOC") #?add the element in the list
sub.insert(2, "OS") #?insert the element in the list, 2nd(0,1,2) position e OS add korbe
sub.remove("Basic") #?remove the element in the list
sub.sort() #?sort the element in the list, A-Z order e sort korbe, or 1-100 order
sub.reverse() #?reverse the element in the list, Z-A
sub.pop(2) #?pop(remove) the element in the list, 2nd(0,1,2) position er element pop korbe or pop() dile last element pop korbe
sub.clear() #?clear the element in the list, sob clear
sub1 = sub.copy() #?sub er list ke copy kore sub1 e rakbe
print(sub1)
position = sub.index("C") #?print the position of the element
print(position)
count = sub.count("C") #?C kotobar list e ase OUTPUT:2
print(count)

#!===================EXERCISE 2
x= [5,15,10,14,5,5]
x.reverse()
print(x)
x.sort()
print(x)
x.clear()
print(x)
z = x.count(5)
print(z)

#***range
#!
num = list(range(10)) #?0 theke 9 porjonto print korbe
print(num)
print(num[2]) #?2nd element print korbe Output:2
print(num[2:5]) #?2nd theke 4th element print korbe

#! range(start, end, step)
num1 = list(range(5, 11)) #?5 theke 10 porjonto print korbe
print(num1)

num3 = list(range(4,15,2)) #?4 theke 14 porjonto 2 step e print korbe
print(num3)

#!
num4 = [10,15,17,12,20]
print(num4)
index = 0
while index<= 5:
	print(num[index])

#***LIST COMPREHENSION*** ============EXTRA AI CODE
#?List comprehension is an elegant way to define and create lists based on existing lists.
#?List comprehension is generally more compact and faster than normal functions and loops for creating lists.
#?However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
#?Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.

#?Syntax: new_list = [expression for item in iterable if condition == True]

#?Example 1
#?Without List Comprehension
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)

#?With List Comprehension
squares = [i**2 for i in range(10)]
print(squares)

#?Example 2
#?Without List Comprehension
squares = []
for i in range(10):
    if i%2 == 0:
        squares.append(i**2)
print(squares)

#?With List Comprehension
squares = [i**2 for i in range(10) if i%2 == 0]
print(squares)

#?Example 3
#?Without List Comprehension
squares = []
for i in range(10):
    if i%2 == 0:
        squares.append(i**2)
    else:
        squares.append(i**3)
print(squares)

#?With List Comprehension
squares = [i**2 if i%2 == 0 else i**3 for i in range(10)]
print(squares)

#?Example 4
#?Without List Comprehension
squares = []
for i in range(10):
    if i%2 == 0:
        squares.append(i**2)
    else:
        squares.append(i**3)
print(squares)

#?With List Comprehension
squares = [i**2 if i%2 == 0 else i**3 for i in range(10)]
print(squares)


#***LIST AS INPUT FROM USER***

#@SUM of input values and store in the list
n = input("Enter the number of elements: ")
#$10 20 30 40 50
list = n.split() #?split the input
#$(10,20,30,40,50) and store in the list
print(list) #?print the list
sum = 0
for num in list: 
    sum += int(num) #?convert the string to integer
print(sum) #?print the sum of the list

#@Number of words,letters and digits in the list
text = input("Enter the elements: ") #$ My name is 123
number_of_letters = 0
number_of_words = 0
number_of_digits = 0

for i in text:
    i = i.lower()
    if i>='a' and i<='z':
        number_of_letters += 1
    if i>='0' and i<='9':
        number_of_digits += 1
    if i == ' ':
        number_of_words += 1
print("Number of Letters:", number_of_letters)
print("Number of Words:",number_of_words+1)
print("Number of Digits:",number_of_digits)

#************Projects//////
#!===============================
"""
Project 1: Task Manager System
Problem Statement:
Create a simple task manager where a user can:
- Add a task to a list.
- Remove a task by name.
- Mark a task as complete.
- View all tasks (completed and pending).
- Exit the program.
"""

tasks = []
def add_task(task):
    tasks.append({'task': task, 'completed': False})

def remove_task(task):
    global tasks
    tasks = [t for t in tasks if t['task'] != task]

def mark_complete(task):
    for t in tasks:
        if t['task'] == task:
            t['completed'] = True

def view_tasks():
    for t in tasks:
        status = "Completed" if t['completed'] else "Pending"
        print(f"{t['task']} - {status}")

#@ Example usage
add_task("Buy groceries")
add_task("Complete Python project")
mark_complete("Buy groceries")
view_tasks()

#!=======================
"""
Project 2: Grocery Shopping List Manager
Problem Statement:
Create a grocery shopping list application that allows users to:
- Add items to the list.
- Remove items from the list.
- Sort the list alphabetically.
- View the final list before shopping.
- Exit the program.
"""

grocery_list = []

def add_item(item):
    grocery_list.append(item)

def remove_item(item):
    if item in grocery_list:
        grocery_list.remove(item)

def sort_list():
    grocery_list.sort()

def view_list():
    print("Grocery List:", grocery_list)
#@ Example usage
add_item("Milk")
add_item("Eggs")
add_item("Bread")
sort_list()
view_list()

#!=======================
"""
Project 3: Student Grades Tracker
Problem Statement:
Build a student grade tracker where:
- The teacher can add student names and their grades.
- The teacher can update a student’s grade.
- If a student's grade is below 40%, mark them as Failing.
- If a student's grade is above 90%, mark them as Top Performer.
- View all students with their grades and performance status.
"""

students = {}

def add_student(name, grade):
    students[name] = grade

def update_grade(name, grade):
    if name in students:
        students[name] = grade

def view_students():
    for name, grade in students.items():
        status = "Top Performer" if grade > 90 else "Failing" if grade < 40 else "Normal"
        print(f"{name}: {grade}% - {status}")
#@ Example usage
add_student("Alice", 95)
add_student("Bob", 35)
add_student("Charlie", 70)
view_students()



















