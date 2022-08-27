x=chr(65)
print(x)
x=chr(11111)
print(x)
x=ord("h")
print(x)
print(len("Dishambha"))
size = len("hope")
print(size)


w1 ='Dishambha '
w2 ='is '
w3 ='Amazing '
#concatination
msg=w1+w2+w3
print(msg)
#dublication
print(msg*1)

print('_'*10)
print("."*10)

for i in range (1,10):
    print(i * '*')
for i in range(10,0,-1):
    print(i *'*')
#right alignment
for i in range(1,10):
    print((i*" * ").rjust(50))
for i in range(1,15,2):
    print((i* " T ").center(50))


#reverse
name ="Dishambha"
rev_name = name[::-1]
print(rev_name)

#even index
even_name = name[::2]
#odd index
odd_name = name[1::2]
print(even_name,odd_name)


name = "Dishambha awasthi"
mname_rev = name [6:-8][::-1]
print(mname_rev)