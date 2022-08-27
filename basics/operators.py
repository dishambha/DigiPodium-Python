#OPERATORS

a=46
b=3

#arithmatic operators
print("Addition = " , a+b)
print("substraction = " , a-b)
print("division = ",a/b)
print("multiplication = " ,a*b)
print("modulus = " ,a%b)
print("power = ",a**b)
print("floor division =" ,a//b)


#assignment operators
x=15
x += 3
print("x+=3 ", x)

x -= 4
print("x -=4", x)
x *= 5
print("x *=5",x)

x /=4
print("x /=4",x)
x **=3
print("x **=3", x)
x //=4
print("x //=4", x)
x %=4
print("x %=4" , x)
 
a=7
b=8
c=7

#comparision operators

print ("a>=b",a>=b)
print("a!=b", a!=b)
print("a>b",a>b)
print("a<b",a<b)
print("a==b",a==b)
print("a<=b",a<=b)
print("a>=C",a>=c)
print("a!=c",a!=c)
print("a>c",a>c)
print("a<C",a>c)
print("a==c",a==c)
print("a<=c",a<=c)
print("b<c",b<c)
print("b>c",b>c)
print("b==c",b==c)
print("b!=c",b!=c)
print("b<=c",b<=c)
print("b>=c",b>=c)

#logical operators
#and
x=183
y=264
z=199

if x>y and z<=x :
    print ("yaa")
else :
    print("nah")

#or

if x>y or z<=x:
    print ("yay")
else :
    print ("nah")
 
#not 
print(not ( (x>y) ))

#membership operators 

fruits =["apple","grapes" ,"banana","mango"]
name = "Digipodium"
print("grapes" in fruits )
print("xgfs" in name)

print ("papaya" not in fruits )
print ("pod" not in name)

#formatted String
value = 1000
discount =100
print (f"The payable amount is{value} and your discount is {discount}")