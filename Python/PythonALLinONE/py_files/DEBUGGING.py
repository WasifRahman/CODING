def add(*numbers):
    sum  = 0
    for num in numbers:
        sum += num
    return sum
print(add(10,20))

#@ wrong code,
def add(*numbers):
    sum  = 0
    for num in numbers:
        sum += num
        return sum 
print(add(10,20))