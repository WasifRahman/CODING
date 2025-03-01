list1 = ["Wasif", "Larry", "Carry", "Harry"]

for item in list1:
	print(item)
	
list2 = ("Wasif", "Larry", "Carry", "Harry")
for item in list2:
	print(item)

	
list3 = [["Wasif",1], ["Larry",2], ["Carry",3], ["Harry",250]]
dict1 = dict(list3)
for item, lollypop in list3:
	print(item, "and lolly is", lollypop)
for item, lollypop in dict1.items():
	print(item, "and lolly is", lollypop)
for item in dict1:
    print(item)


#Quiz
items = [int, float, "wasif", 5,4,12,15,16] 

for item in items:
	if str(item).isnumeric() and item>6:
		print(item)
		






