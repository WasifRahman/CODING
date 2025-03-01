""" i = 1
while i <= 100:
    print(i)
    i = i + 1
    if i == 20:
        break
print("Hello")
 """


i = 1
while i <= 100:
    if i == 20:
        continue
    print(i)
    i = i + 1

#1+3+5+......+499 er total
total = 0
i=1
while i <= 499:
    total = total + i
    i = i + 2
print(total) 
