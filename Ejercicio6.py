#!/usr/bin/env python3
# -*- coding: utf-8 -*-def figura(l):
    Hini=heading()
    ini=position()
    seth(0)
    penup()
    goto(ini+(-40/2,-40/2))
    pendown()
    for i in range(l):
        forward(H) 
        left(360/l)
    penup()
    goto(ini)
    seth(Hini)
from turtle import *
import math
penup()
#numero de casillas
#hideturtle()
speed(10)
goto(-200,-200)
f=int(input('Número de filas del poligono '))
lon=100*f
c=lon
l=f+2
pendown()
for i in range(3):
    forward(lon)
    left(120)
    if i==1: Pos=position()
pensize(4)
penup()
r=40
H = 2*r*math.sin(math.pi/l)

for j in range(f):
    if j%2==0:seth(0)
    else:seth(180)
    for k in range(f-j-1):
        figura(l-j)
        if f-(j+1)!=0: 
            forward((c/f*(f-j))/(f-(j+1)))
            print((c/f*(f-j))/(f+(j+1)),j)
            #forward(((c/f*(f-j))/(f-(j+1))-3**(j+1)))
        if k==f-j-2: figura(l-j)
    if j!=f-1:
        if j%2==0:left(120)
        else:right(120)  
        forward(lon/(f-1))
    else: 
        if f%2==0:
            seth(0)
        else:
            seth(180)
        #forward(((c/f*(f-j))/(f-(j+2)))/2-30*(k+1))
        if j==f-1: 
            goto(Pos)
            figura(l-j)
     
