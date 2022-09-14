# lambda a,b:a+b
# #<function_main_.<lambda>(a,b)>

# adder = lambda a, b:a+b
# print(adder(60,568))

# def exp(power):
#     return lambda l : [a**power for a in 1]
# four = exp(4)
# four([2,4,6,8,10])

y=[2,6,7,9,8,4,8,9]
x=[1,2,4,5,8,7,3,8]
o =list( map(lambda i:i**2, x))
print(o)

xy = list(map(lambda a,b:a+b,x,y))
print(xy)

y3 =list(filter(lambda i :i>3,x))
print(y3)
name =("Raj Singh","Vijay Singh" ,"Vibhu Awasthi","Ajay Singh","Vijay Pandey" )
name_singh =list(filter(lambda n:n.endswith("Singh",),name))
print(name_singh)

name_r = list(filter(lambda n:n.startswith("R"),name))
print(name_r)

