def word_counter(s):
    words = s.split()
    return len(words)

def area(l,b):
    return l* b

def circumference (r):
    return 2* 3.14 * r 

print(word_counter("This is an example"))
print(word_counter("Wellcom to the code verse"))
print(word_counter("screenshot se kuch nahi hota"))
print(word_counter("rules and convenctions likh lo"))

#1.direct
print(area(10,20))

#2.user input
a= int(input("enter length "))
b= int(input("enter breadth "))
out = area(a,b)
print("area==>",out)

#3.shorter user input
out = area(int(input("length:")),int(input("breadth:")))
print("area=>",out)

#call circumference

