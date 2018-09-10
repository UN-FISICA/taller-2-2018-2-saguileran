from turtle import *
import  math
def cuadrado(l):
    ini=position()
    penup()
    goto(ini+(-100/2,-100/2))
    pendown()
    for i in range(4):
        forward(100)
        left(360/l)
    penup()
    goto(ini)
speed(10)
hideturtle()
pensize(4)
a,b=-1,1
penup()
goto(-200,-200)
for j in range(4):
	forward(400)
	left(90)
	seth(0)
	cuadrado(4)
	heading()
	left(90+90*j)
pendown()
