
#! *
#! **
#! ***
n = 3
for i in range(1,n+1,1): # or range(n+1)
    print("*" * i)

#! *
#! ***
#! *****
n=5
for i in range(1,n+1,2):
    print(i*"*")

# or,
n=3 # 3 karon n+1 e 3 porjonto ..i er value 0,1,2,3 (0 er jonno ekta gap ase)
for i in range(n+1):
    print((2*i-1)*"*")

#!   *
#!  ** 
#! ***
n = 3
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i)

#!   *
#!  ***
#! *****
n = 3
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))







