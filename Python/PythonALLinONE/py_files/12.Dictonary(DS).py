
#***Dictonary
studentId={
    "1": "Wasif", #?Comma must
    "2": "Wasia",
    "3": "Ilmun",
    "4": "Ariyan", 
}
print(studentId["2"])
print(studentId.get("2"))
print(studentId.get("5")) #$Output: None
print(studentId.get("5","Not a valid studentid"))#$Output: Not a valid studentid
print(studentId.get("1","Not a valid studentid"))#$Output: Wasif (jodi find na hoy tahole not a valid st. show korbe)

#! or, integer diea:
studentId={
    1: "Wasif", #?Comma must
    2: "Wasia",
    3: "Ilmun",
    4: "Ariyan", 
}
print(studentId[1])
print(studentId.get(2))

