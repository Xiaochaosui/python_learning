from turtle import *
import random
#white
def zq(c):
    color(c)
    begin_fill()
    for i in range(0,4):
        fd(50)
        rt(90)
    end_fill()

def col():
    n = random.randint(1,5)
    if n==1:
        return "green"
    elif n==2:
        return "red"
    elif n==3:
        return "yellow"
    elif n==4:
        return "black"
    elif n==5:
        return "purple"


for i in range(0,4):
    zq(col())
    rt(90)

