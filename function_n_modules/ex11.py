# i=0
# def change(i):
#     i=i+1
#     return i 
# change(1)
# print(i)

# class A:
#     def __init__(self,b):
#         self.b=b
#     def display(self):
#         print(self.b)
# obj=A("Hello")
# del obj
        
# def func(a, b=5, c=10):
#     print('a is',a, 'and b is',b,'and c is',c)

# func(3,7)
# func(25,c=24)
# func(c=50, a =100)

# def test(a, b= 5):
#     print(a , b)

# test(-3)
# class fruits:
#     def __init__(self,price):
#         self.price = price
# obj=fruits(50)

# obj.quantity=10
# obj.bags=2

# print(obj.quantity+len(obj.__dict__))

# class Demo:
#     def __init__(self):
#         pass

#     def __init__(self):
#         print(__name__)

# obj = Demo()
# obj.test()

class change:
    def __init__(self,x ,y ,z):
        self.a = x+y+z

x = change(1,2,3)
y = getattr(x,"a")
setattr(x, 'a', y+1)
print(x.a)