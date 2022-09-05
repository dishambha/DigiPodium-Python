from turtle import*

speed(1)
right(90)
for i in range(6):
    if i<2:
        forward(60)
        left(90)
        fd(270)
        left(90)
        fd(60)
    if i==3:
        left(90)
        fd(120)    
    if i<4 :
        fd(270)
        left(90)
        fd(60)
        left(90)
        fd(270)
    if i==4:
        fd(120)  
        left(90)
    if i<6:
        forward(60)
        left(90)
        fd(270)
        left(90)
mainloop()