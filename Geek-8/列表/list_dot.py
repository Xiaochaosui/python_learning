from turtle import *
import random

dot_x = []
dot_y = []
speed(10)
for i in range(0,10):
       penup()
       x = random.randint(-200,200)
       y = random.randint(-200,200)
       dot_x.append(x)
       dot_y.append(y)
       goto(x,y)
       dot(10,"blue")
for i in range(0,10):
       penup()
       goto(dot_x[i],dot_y[i])
       dot(5,"green")
