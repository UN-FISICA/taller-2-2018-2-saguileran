import turtle, math
#turtle.forward(100)
def cuadrado(l,c):
    turtle.setpos(turtle.position()+(-c/2,c/2))
    for i in range(4):
        turtle.forward(c)
        turtle.right(90)
cuadrado(3,100)
