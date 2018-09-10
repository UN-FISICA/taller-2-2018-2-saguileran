from turtle import *
import  math
def figura(l):
    ini=position()
    penup()
    goto(ini+(-25/2,-25/2))
    pendown()
    for i in range(l):
        forward(25)
        left(360/l)
    penup()
    goto(ini)
hideturtle()
pensize(4)
a,b,l=-1,1,int(input('Enter number of sides: '))
L=int(input('Enter number of sides big: '))
penup()
goto(-200,-200)
for j in range(L):
	forward(100)
	left(90)
	seth(0)
	figura(l)
	seth(0)
	left((360/L)+(360/L)*j)
pendown()


