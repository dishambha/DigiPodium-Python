a= float(input(" ENTER THE FIRST NUMBER "))
b= float(input(" ENTER THE SECOND NUMBER "))
c= float(input(" ENTER THE THIRD NUMBER "))
if a>b and b>c:
    print(f"{a} is the greatest number")
    print(f"{c} is the smallest number")
elif a<b and b<c :
    print(f"{a} is the smallest number")
    print(f"{c} is the grestest number")
elif b>a and a>c :
    print(f"{b} is the greatest number")
    print(f"{c} is the smallest number")
elif b<a and a>c :
    print(f"{b} is the smallest number")
    print(f"{a} is the greatest number")
elif c>a and a>b :
    print(f"{c} is the grestest number")
    print(f"{b} is the smallest number")
elif c<b and b<a :
    print(f"{c} is the smallest number")
    print(f"{a} is the greatest number")
elif a==b and a<c:
    print(f"first number{a} and the second number{b} are equal and third nunber{c} is greatest")  
elif a==b and a>c:
    print(f"first number {a} and second number{b} are equal and third number {c} is smallest")
elif a==c and a<b:
    print(f"first number{a} and the third number{c} are equal and second number {b} is greatest")
elif a==c and a>b:
    print(f"first number {a} and third number {c} are equal and second number {b} is smallest")
elif b==c and b<a:
    print(f"second nmber {b} and third number {c} are equal and first number {a} is greatest")
elif b==c and b>a:
    print(f"second number {b} and third number {c} are equal and first number {a} is smallest")
