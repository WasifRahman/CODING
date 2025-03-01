#Important

""" print(r"c:\docs\\navin") #Raw string
print(name[1:])
print(len(myname)) """
""" Exercise = nums. append/sort....etc """



                #"""3"""
print(5 // 2) #integer Division
print((8+2)*3)
print(2**3)
print(10//3)
print(10%3) #Reminders
print("Wasif")
print("Wasif's Laptop")
print("Wasif's 'Laptop'")
print('Wasif\'s Laptop')
print('Wasif '*3)
print("c:\docs\navin") # Don't want this
print(r"c:\docs\navin") #Raw string or below
print("c:\docs\\navin")

             #"""4"""
x=2
print(x+3)
y=3
print(x+y)

x=9
print(x+y)
print(x+10)
print(-+y) #why we cannot use underscore

name= "youtube"
print(name)
print(name, "rocks "*3)

print(name[0])
print(name[1])
print(name[-1]) # -1 starts from end and start with 0
print(name[0:2]) # : is used with two words
print(name[1:4])
print(name[1:]) # kothay sesh hobe boli nai tai sesh porjonto jabe.
print(name[:4])
print(name[3:10]) # don't give you error
print("my",name[3:])

myname = "Wasif Rahman"
print(len(myname)) #joto gula word ase tar amount  #the length of the string

                    #'''5'''
nums = [25, 12, 36, 95, 14]
print(nums)
print(nums[0])
print(nums[4])
print(nums[2:])
print(nums[-1])
print(nums[-4])
print(nums[-5])

names = ["Wasif", "Rhythm", "Wasia"]
print(names)

values = [9.5, "Wasif", 25]
print(values)

mil=[nums, names]
print(mil)

nums.append(45) #insert at last
print(nums)
nums.insert(2,77) #in in the middle where to put, number
print(nums)
nums.remove(14)
print(nums)
nums.pop(1)
print(nums)
nums.pop() #donot espesify it will remove last one.
print(nums)
del nums[2:]
print(nums)
nums.extend([29, 12,14,36])
print(nums)
nums.sort() #in a sorted formated small to larger
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))






                    #'''7'''
tup = (21, 36,14,25) # you can not change values
print(tup)
print(tup[1])

s = {22, 25, 14,21,5}#set
print(s)
s={25,14,98,63,75,98}
print(s)

data = {1:"Wasif", 2:"Wasia", 4:"Ilmun"} # Dictionary
print(data)
print(data[4])
print(data[1])
print(data.get(2))
print(data.get(3)) # none because is not defined
print(data.get(1, "Not found")) # because 1 is defined
print(data.get(3, "Not found")) # 3 is not defined

keys= ['Wasif', 'wasia', 'Ilmun']
values = ["Python", "Java", "JS"]
data= dict(zip(keys,values)) #***dictionary toirir format
print(data)

print(data['Wasif'])
data['World'] = "CS"
print(data)

del data['World']
print(data)

prog = {"JS":"Atom", "CS":"VS", "Python":['Pycharm','Sublime'], "Java":{"JSE":"Netbeans","JEE":"Eclipse"}}
print(prog)
print(prog["JS"])
print(prog["Python"])
print(prog["Python"][1])
print(prog["Java"]["JEE"])








from math import floor, ceil

num =5
print(id(num))
name= "Wasif"
print(id(name)) #id=address

a=10
b=a
print(a)
print(b)
print(id(a))
print(id(b)) #same address
print(id(10))
k= 10
print(id(k))

a =9
print(id(a)) #different
print(id(b))

k=a
print(id(k))

b=8
PI =3.14
print(PI)
PI=3.15
print(PI)
print(type(PI))

"""
none when it is not defined

Numeric: int, float, complex, bool

"""

num=2.5
print(type(num))
num=5
print(type(num))
num=6+9j         #a+bj is the format of complex number
print(type(num))

a=5.6
b=int(a)
print(b)
print(type(b))

k =float(b)
print(type(k))
print(k)
k=6
c=complex(a,k)
print(type(c))
print(c)

#bool = boolean
print(b<k) #b=5 k=6
bool = b<k
print(type(bool))
print(b>k)
print(int(True))
print(int(False))

"""Sequence: List, Tuple, Set, String, Range"""
lst = [25, 36, 45, 12]
print(type(lst))
s= {25, 2,13, 24}
print(type(s))
t = (25, 34, 34)
print(type(t))
str = "Wasif"
print(type(str))
st= 'a'
print(type(st))
range(0,10)
print(list(range(10)))
print(list(range(2,11,2)))


d= {"Wasif": "Samsung", "Wasia":"Xiome", "Ilmun":"IPhone"} #dictinary
print(d)
print(d.keys())
print(d.values())

print(d["Wasif"])
print(d.get("Ilmun"))






