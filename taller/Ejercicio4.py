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
hideturtle()
speed(10)
goto(-200,-200)
l,f,lon=int(input('Número de lados del poligono ')),int(input('Número de filas del poligono ')),400.
#for i in range(3):
#    forward(lon)
#    left(120)
pensize(4)
for j in range(f):
    if j%2==0:seth(0)
    else:seth(180)
    for k in range(f-j-1):
        figura(l)
        if f-(j+1)!=0: forward((100*(f-j))/(f-(j+1)))
        if k==f-j-2: figura(l)
    #forward(100*(f-j))
    if j!=f-1:
        if j%2==0:left(120)
        else:right(120)  
        forward(lon/4)
    else: 
        if f%2==0:
            seth(0)
        else:
            seth(180)
        forward(((100*(f-j))/(f-(j+2)))/2)
        figura(l)
