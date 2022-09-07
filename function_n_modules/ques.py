def prime_number():
    x=[]
    for num in range(2,100):
        for i in range(2,num):
            if num%i ==0:
                break
        else:
            x.append(num)
            print(num,end=" ")
prime_number()
ans =len("hello")+ len("student")
print(ans)
