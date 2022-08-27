from turtle import *

pensize (100)
speed(0)
bgcolor("black")

pencolor("orange")
forward (200)
penup()
right(90)
forward(100)
left(90)
pendown()
pencolor("white")
backward(200)
penup()
right(90)
forward(100)
right(90)
pendown()
pencolor("green")
backward(200)
penup()
forward(50)
right(90)
forward(100)
pendown()
pensize(1.5)
pencolor("blue")
circle(50)
left(90)
x=0
speed(0)
while x<=720 :
    #speed(0)
    forward(50)
    left(x)
    forward(50)
    left(90)
    circle(50,15)
    left(90)
    
    
    x+=15

right(90)
circle(50)
hideturtle()

mainloop()