# Elif statement
# Else if = elif

# from math import

marks = 23
if 80 <= marks <= 100:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("A-")
    
elif marks >= 50:
    print("B")
elif marks >= 40:
    print("C")
elif marks >= 33:
    print("D")
else:
    print("Fail")


if 2>3:
    print("Yep! It looks good.")
else:
    print("Nope. Not true.")



#LISTING

camping_list= ["knife", "tent" , "oil", "water", "pi"]
print("He")
print(type(camping_list))

camp_sit = ["Crystal Lake", 404, 89.3, True] #string , integer, float, boolean

you= camping_list[2] #camping_list[-3]
me = camping_list[0]
print(you)
print(me)
print(camping_list)
print(camp_sit[-1])


# # Logical Operator "or and not"
# name = input("What's your name?")

# if not name == "Ben":
#     # if name != "Ben": != is not
#     print(name)
# else:
#     print("No name")


name= input("What's your name?")

if name == "Ben":
    status = input("Are you evil?")
    if status == "yes":      #This is a nested ifs.
        print("Get out!!!")
    else:
        print("You are one of the good Bens")
else:
    print("Come in")









