namea =(input("TYPE YOUR NAME :"))
a=float(input("TYPE YOUR AGE  :"))
nameb =(input("TYPE YOUR NAME :"))
b=float(input("TYPE YOUR AGE :"))
namec =(input("TYPE YOUR NAME :"))
c=float(input("TYPE YOUR AGE :"))
named =(input("TYPE YOUR NAME :"))
d= float(input("TYPE YOUR AGE :")) 

if a==b and b==c and c==d:
    print (f"All {namea} ,{nameb}, {namec} and {named} are of same age")
elif a<=b and b<=c and c<=d:
    print(f"{namea} is youngest and {named} is eldest")
elif a>b and b>c and c>d:
    print(f"{namea} is eldest and {named} is the youngest")
elif a<=c and c<=d and d<=b:
    print(f"{namea} is youngest and {nameb} is eldest")
elif a>c and c>d and d>b:
    print(f"{namea} is eldest and {nameb} is youngest")
elif a<=b and b<=d and d<=c:
    print(f"{namea} is youngest and {namec} is eldest")
elif a>b and b>d and d>c:
    print(f"{namea} is eldest and {namec} is youngest")
elif b<=a and a<=d and d<=c:
    print(f"{nameb} is youngest and {namec} is eldest")
elif b>a and a>d and d>c:
    print(f"{nameb} is eldest and {namec} is youngest")
elif b<=a and a<=c and c<=d:
    print(f"{nameb} is youngest and {named} is eldest")
elif b>a and a>c and c>d:
    print(f"{nameb} is eldest and {named} is youngest")
elif c<=a and a<=b and b<=d:
    print(f"{namec} is youngest and {named} is eldest")
elif c>a and a>b and b>d:
    print(f"{namec} is eldest and {named} is youngest")
