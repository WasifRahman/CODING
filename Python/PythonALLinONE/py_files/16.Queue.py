
from collections import deque
bank = deque(['Wasif','Wasia','Anis'])
print(bank)
bank.pop() #last item remove
print(bank)
bank.popleft() # first item remove
print(bank)
bank.popleft()
print(bank)
if not bank:
    print("No person left.")

