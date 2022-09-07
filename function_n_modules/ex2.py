#return value
def area():
    l = int(input("ENTER THE LENGTH"))
    b = int(input("ENTER THE BREADTH"))
    area = l* b
    return area
#calling

# print("area=",area())

# ans = area()
# print("area=",ans)

# ans = area() + area() -area()
# print("TOTAL AREA=",ans)

def minmax():
    x =[23,3,4,5,4,34,4,434,]
    return min(x),max(x)#returning more then one value

values = minmax()
x,y = minmax()
print(values)
print(x,y)
print(minmax())

