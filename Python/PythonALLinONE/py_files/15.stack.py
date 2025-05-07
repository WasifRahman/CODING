book = []
book.append("C")
book.append("C++")
book.append("python")
print(book)

book.pop() #LIFO = last input first out; last e jei item input hoise oita first e remove hobe
print(book)
print("Now the top book is:", book[-1]) #or [1] 

book.pop() #LIFO = last input first out; last e jei item input hoise oita first e remove hobe
print(book)
print("Now the top book is:", book[-1]) #or [0] 

book.pop() #LIFO = last input first out; last e jei item input hoise oita first e remove hobe
if not book:
    print('No books left')
