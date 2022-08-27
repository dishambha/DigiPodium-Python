from turtle import*

speed(1)
bgcolor("slate grey")
pensize(0.5)
pencolor("black")


fillcolor("light steel blue")
begin_fill()
penup()
forward(25)
pendown()

right(90)
forward(250)
left(90)
circle(150,180)
left(90)
forward(50)
end_fill()

fillcolor("slate grey")
begin_fill()
penup()
left(90)
forward(25)
pendown()
right(90)
forward(200)
left(90)
circle(100,180)
end_fill()
hideturtle()

mainloop()