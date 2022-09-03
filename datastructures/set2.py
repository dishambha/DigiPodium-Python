my_set = {1,3}
#add a single value
my_set.add(2)
print(my_set)
#to add multiple value , do not take the repeated value
my_set.update ([2,3,4])
print(my_set)

my_set.update([4,5],[1,6,8])
print(my_set)

#it can give error
my_set.remove(6)
print(my_set)

#it never gives error 
my_set.discard(1)
print(my_set)
#remove and discard are same 
my_set.pop()
print(my_set)
print(my_set.pop())

my_set.clear()
print(my_set)