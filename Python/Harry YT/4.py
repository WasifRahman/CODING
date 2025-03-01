#Dictionary
d1 = {"Harry":"Burger", "Rohan":"Fish", "Wasif":"Pizza", "Wasia": {"B":"maggie", "L":"roti", "D": "Chicken"}}
d1["Ilmun"] = "Junk Food"
d1["Ankit"] ="Kabab"
del d1["Ankit"]
print(type(d1))
print(d1["Wasia"]["B"]) # square bracket
""" print(d1) """
d2 = d1.copy() 
del d2["Wasif"]

#print(d1.copy())
print(d2)
print(d1.get("Wasif"))
d1.update({"Rina":"Toffee"})
print(d1.keys())
print(d1.items())
