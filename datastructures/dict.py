from tkinter.ttk import Style


movies = { 
    "m1" : "sholay",
    "m2" :"spider man : no way home",
    "m3" :"shrek"
}

#traversing a dictonary -> style 1
print("style1")
for name in movies :
    print(name)

#traversing in dictonary -> stylr 2
print("style2")
for key in movies :
    print(movies[key])

#traversing i dictonary -> style 3 
print("style 3")
for keys in movies :
    print(keys,movies[keys])

#traversing i dictonary -> style 4
print("style 4")
for k, v in movies.items():
    print(k,v)





