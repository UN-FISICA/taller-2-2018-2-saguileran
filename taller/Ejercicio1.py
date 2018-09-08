from turtle import *
import  math
#turtle.forward(100)
def cuadrado(l,c):
    ini=position()
    penup();pensize(4)
    setpos(ini+(-c/2,-c/2))
    pendown()
    for i in range(l):
        forward(c)
        left(360/l)
    penup()
    setpos(ini)
    pendown()
hideturtle()
#cuadrado(4,100)
for j in range(4):
  # penup()
   ini1=position()
   setpos(ini1+(-500/2,-500/2))
  # pendown()
   forward(100)
  # cuadrado(4,100)
   left(90)
   #setpos(ini1)
   break
