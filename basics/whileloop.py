#while loop
x = 1
while x < 5:
    print("run")
    x+=1
print("stop")
#break
for i in range (1,11):
    if(i==7):
        print("out of loop")
        break
    else:
        print(i)
#continue
for i in range (1,11):
    if(i==7):
        continue
    else:
        print(i)
#else executes afer the loop compleates normally
fruits =["apple", "banana", "mango"]
for fruit in fruits :
    print(fruit)
else:
    print ("*******")
