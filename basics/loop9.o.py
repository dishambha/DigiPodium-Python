from turtle import*
bgcolor("light yellow")
pencolor("black")
speed(0)
penup()
backward(500)
left(90)  #moving from center to left corner
fd(300)
pendown() 
fillcolor("indian red")
begin_fill()
fd(20)  #left triangle
left(135)
fd(20)
left(90)
fd(20)
left(135)
fd(8)
end_fill()
right(90)
fd(1000) #bottom line
left(90)
fillcolor("indian red")
begin_fill()
fd(20)     #right triangle
right(135)
fd(20)
right(90)
fd(20)
right(135)
fd(20)
end_fill()
left(90)
fd(1000)   #upperline
fillcolor("white")
begin_fill()
left(90)
fd(11)
left(90)
fd(1000)  
left(90)
fd(11)
left(90)
fd(1000)
left(90)
fd(11)
end_fill()
left(90)
fd(25)
right(90)
fd(80)
right(90)
fd(50)
fillcolor("sienna")
begin_fill()
left(90)
for i in range(2):   #left flag
    forward(180)
    left(90)
    forward(250)
    left(90)
end_fill()
right(90)
backward(200)
penup()
right(90)
fd(80)
pendown()
backward(80)
left(90)
fd(200)
penup() #centre flag
backward(350)
right(90)
fd(50)
pendown()
fillcolor("orange")
right(90)#top secion
for i in range (2):
    begin_fill()
    fd(270)
    right(90)
    fd(60)
    right(90)
    end_fill()
penup()#mid section
left(90)
backward(120)
pendown()
fillcolor("white")
for i in range (2):
    begin_fill()
    fd(60)
    right(90)
    fd(270)
    right(90)
    end_fill()
fillcolor("green")#green part
begin_fill()
backward(60)
right(90)
fd(270)
left(90)
fd(60)
end_fill()
penup()
fd(30)  #ashok chakra
left(90)
fd(105)
pendown()
pencolor("blue")
x=15
while x<=180 :
    #speed(0)
    forward(30)
    left(15)
    forward(30)
    left(90)
    circle(30,15)
    left(90)
    x+=15   
right(90)
circle(30)
pencolor("black")
penup()
left(90)
right(90)
fd(120)
pendown()
right(90)
fd(30)
right(90)
fd(30)
left(90)
backward(115)
left(90)
fd(30)
right(90)
fd(265)
penup()  #right flag
right(90)
fd(50)
pendown()
fillcolor("silver")
for i in range(2):
    begin_fill()
    fd(180)
    left(90)
    fd(250)
    left(90)
    end_fill()
left(90)
fd(64.5)
left(90)
fd(50)
backward(50)
right(90)
fd(121)
left(90)
fd(50)
backward(50)
right(90)
fd(64.5)
pencolor("black")#podium
penup()
right(90)
fd(600)
right(90)
fd(30)
pendown()
fd(840)
fillcolor("dodger blue")
begin_fill()
right(90)
fd(30)
right(90)
fd(280)
right(90)
fd(30)
end_fill()
fillcolor("sky blue")
begin_fill()
left(180)
fd(80)
right(90)
fd(280)
right(90)
fd(80)
end_fill()
fillcolor("deep sky blue")
begin_fill()
left(180)
fd(50)
right(90)
fd(280)
right(90)
fd(50)
end_fill()
penup()
backward(300)
right(90)
fd(270*2)
pendown()
pensize(15)#medal
pencolor("red")
left(135)
fd(150)
left(90)
fd(150)
backward(150)
pencolor("gold")
right(180)
fd(7)
fillcolor("gold")
begin_fill()
circle(10)
end_fill()
hideturtle()
mainloop()