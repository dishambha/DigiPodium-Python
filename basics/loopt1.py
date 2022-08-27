from turtle import *
speed('fastest')

#360/number of sides
sides = int(input("HOW MANY SIDES DO YOU WANT?"))
distance = int(input("HOW FAR DO YOU WANT TO GO?"))


for i in range(sides):
    forward(distance)
    left(360/sides)


mainloop()
