#Accessing string character in python
str = 'Dishambha'
print('str =' ,str)

#first character
print('str[0] = ',str[0])

#second character
print('str[1] =',str[1])

#last character
print('str[-1]=',str[-1])

#second last character
print('str[-2] =',str[-2])  

#getting a slice
s = 'Dishambha'
slice1= s[4:len(s)]
slice2=s[0:]
print(slice1)
print(slice2)
print(len(s))