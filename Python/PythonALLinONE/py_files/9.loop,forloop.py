
#! USING WHILE LOOP(Difficult)
num = [10,22,20,30,50]

index = 0
n = len(num)
while index<n:
    print(num[index])
    index+=1
# or, 
index = 0
while index<len(num): #or, while index<5
    print(num[index])
    index+=1

#! USING FOR LOOP(Easy)
num = [10,22,20,30,50]
for i in num: #i is a variable, it can be any name
    print(i)
#!sum of all elements
sum = 0
for i in num:
    sum+=i
print(sum)
#!========Exercise 1=========
#sum of 1 to 10
sum = 0
for i in range(1,11): #1 to 10
    sum+=i
print(sum)

#!1+2+3+....+n (tinta jinish mone rakhbo :suru, sesh ar difference)
n = input("Enter a number: ")
n = int(n)
sum = 0
for i in range(1, n+1, 1):
    sum += i
print(sum)

#!2+4+6+....+n
n = input("Enter a number: ")
n = int(n)
sum = 0
for i in range(2, n+1, 2): #n+1 because, n tahole ashbe, n nile n er ag porjonto ashbe
    sum += i
print(sum)

#!1*1+2*2+3*3+....+n*n
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1,1):
    sum+=i*i
print(sum)

#!1*2*3*....*n
n = int(input("Enter a number: "))
sum = 1
for i in range(1,n+1,1):
    sum*=i
print(sum)

#!1+1/2+1/3+....+1/n
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1,1):
    sum+=1/i
print(sum)

#!1/2+2/3+3/4+....+n/n+1
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1,1):
    sum+=i/(i+1)
print(sum)

#!1*2*3*....*n
n = int(input("Enter a number: "))
sum = 1
for i in range(1,n+1,1):
    sum*=i
print(sum)

#!1*2+2*3+3*4+....+n*n
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n,1):
    sum+=i*(i+1)
print(sum)

#!1*2*3+2*3*4+3*4*5+....+n*n*n
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n,1):
    sum+=i*(i+1)*(i+2)
print(sum)

#!1*2*3*4+2*3*4*5+3*4*5*6+....+n*n*n*n
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n,1):
    sum+=i*(i+1)*(i+2)*(i+3)
print(sum)

#!1*2*3*4*5+2*3*4*5*6+3*4*5*6*7+....+n*n*n*n*n
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n,1):
    sum+=i*(i+1)*(i+2)*(i+3)*(i+4)
print(sum)

#!1!+2!+3!+....+n!
n = int(input("Enter a number: "))
sum = 0
fact = 1
for i in range(1,n+1,1):
    fact*=i
    sum+=fact
print(sum)

#!1!*2!+2!*3!+3!*4!+....+n!*(n+1)!
n = int(input("Enter a number: "))
sum = 0
fact = 1
for i in range(1,n,1):
    fact*=i
    sum+=fact*(fact+1)
print(sum)

#!1!*2!+2!*3!+3!*4!+....+n!*(n+1)!
n = int(input("Enter a number: "))
sum = 0
fact = 1
for i in range(1,n,1):
    fact*=i
    sum+=fact*(fact+1)
print(sum)

#!1+1*2+1*2*3+....+1*2*3*....*n
n = int(input("Enter a number: "))
sum = 0
fact = 1
for i in range(1,n+1,1):
    fact*=i
    sum+=fact
print(sum)



