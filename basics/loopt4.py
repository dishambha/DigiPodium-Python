from turtle import *
speed(0)
bgcolor("black")
for i in range (6):
    pensize(5)
    pencolor("pink")
    penup()
    forward(150)
    pendown()
    circle(5)
    left(360/6)
    for i in range (6):
        pensize(3)
        pencolor("yellow")
        penup()
        forward(100)
        pendown()
        circle(10)
        left(360/6)
        for i in range (6):
            pensize(2)
            pencolor("orange")
            penup()
            forward(50)
            pendown()
            right(360/6)
            circle(20)
             
            

mainloop()