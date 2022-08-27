from turtle import *

colors = ["red","blue","green"]
pensize(50)
for i in range (70,0,-1):
    pencolor(colors[i%3])
    forward(100)
    left(360/3)
    

mainloop()
