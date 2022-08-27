from turtle import *
speed('fastest')

#360/number of sides
sides = 6
distance =120
fillcolor("yellow")
begin_fill()

for i in range(sides):
    forward(distance)
    left(360/sides)
end_fill()


mainloop()
