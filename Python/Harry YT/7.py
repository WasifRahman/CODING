""" var1 = 6
var2 = 56
var3 = int(input())
if var3 > var2:
   print("Greater")
elif var3 == var2:
   print("Equal")
else:
   print("Lower") """

List1 = [5, 7, 3]
print(5 in List1)
print(15 not in List1)
if 5 in List1:
    print("Yes, in the list")

x = float(input("What is your age? => "))
if 100 > x > 18:
    print("You can drive.")
elif x ==18:
   print("We can not decide.You have to come.")
else:
   print("You can not drive.")
