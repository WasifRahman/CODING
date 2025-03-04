
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






