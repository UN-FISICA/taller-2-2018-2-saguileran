import turtle, math
#turtle.forward(100)
def cuadrado(l,c):
    ini=turtle.position()
    turtle.setpos(ini+(-c/2,c/2))
    for i in range(4):
        turtle.forward(c)
        turtle.right(90)
    turtle.setpos(ini)
for j in range(4):
   ini1=turtle.position()
   turtle.setpos(ini1+(-100/2,100/2))
   turtle.forward(100)
   cuadrado(4,50)
   turtle.right(90)
   turtle.goto(ini1)
