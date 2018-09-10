#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 18:27:05 2018

@author: sebas
"""

def figura(l):
    Hini=heading()
    ini=position()
    seth(0)
    penup()
    goto(ini+(-40/2,-40/2))
    pendown()
    for i in range(l):
        forward(40) 
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
r=5
H = 2*r*math.sin(math.pi/l)
for j in range(f):
    if j%2==0:seth(0)
    else:seth(180)
    for k in range(f-j-1):
        figura(int(H-j+2))
        if f-(j+1)!=0: 
            if j==f-2:
                forward((c/f*(f-j))/(f-(j+1))-(j)*(c/10))
            else:
                forward((c/f*(f-j))/(f-(j+1))-(j)*(c/20))
            #print((c/f*(f-j))/(f+(j+1)),j)
            #forward(((c/f*(f-j))/(f-(j+1))-3**(j+1)))
        if k==f-j-2: figura(int(H-j+2))
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
            figura(int(H-j+2))
