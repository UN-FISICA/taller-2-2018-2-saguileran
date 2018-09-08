from turtle import *
import  math
#speed(1)
a,b=-1,1
def cuadrado(l,c):
    ini=position()
    penup();pensize(4)
    setpos(ini+(a*c/2,-b*c/2))
    pendown()
    for i in range(l):
        forward(c)
        left(360/l)
    penup()
    goto(ini)
    pendown()
    pensize(1)
    heading()
#hideturtle()
#cuadrado(4,10)
penup()
setpos(position()+(-100,-100))
for j in range(4):
   penup()
  # ini1=position()
   #setpos(ini1+(-200/2,-200/2))
  # pendown()
   forward(200)
   cuadrado(4,100)
   left(90)
   #setpos(ini1)
   if j%2==0:
     a=-a
   else:
     b=-b
