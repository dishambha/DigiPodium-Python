A = {1,2,3,4,5}
B = {4,5,6,7,8}
#set union
print(A|B)

print(A.union(B))

print(B.union(A))


#intersection
print(A & B)

print(A.intersection(B))

#difference
#it gives the unique values or the first set written in difference function
print(A-B)

print(B.difference(A))
#symetric difference 
#removes the common values of both the sets

print(A ^ B)

print(A.symmetric_difference(B))