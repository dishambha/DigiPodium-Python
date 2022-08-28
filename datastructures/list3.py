#getting a slice of a list

a = [12,23,377,83,938,63,36,37]
slice1 = a[3:-2]
print(slice1)
slice2 = a[:5]
print(slice2)
slice3 = a[-5:]  #last  5
print(slice3)
slice4 = a[5:len(a)]
print(slice4)
slice5 = a[5:]
print(slice5)