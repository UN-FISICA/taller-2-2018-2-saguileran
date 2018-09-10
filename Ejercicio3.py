from turtle import *
import  math
def figura(l):
    ini=position()
    penup()
    goto(ini+(-50/2,-50/2))
    pendown()
    for i in range(l):
        forward(50)
        left(360/l)
    penup()
    goto(ini)
hideturtle()
pensize(4)
a,b,l=-1,1,int(input('Número de lados del poligono: '))
L=int(input('Número de lados del poligono de alineación: '))
penup()
speed(10)
goto(-100,-100)
for j in range(L):
	forward(200)
	left(90)
	seth(0)
	figura(l)
	seth(0)
	left((360/L)+(360/L)*j)
pendown()


