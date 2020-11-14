import turtle
startx = -300
starty = 0
def run(angele,lenth):
    turtle.seth(angele)
    turtle.fd(lenth)
def change(x,y):
    turtle.penup()
    turtle.goto(startx+x,starty+y)
    turtle.pendown()
def init():
    turtle.pensize(10)
    turtle.pencolor("purple")

if __name__ == '__main__':
    #turtle.screensize(1000, 1000)
    turtle.title("我的名字")
   # turtle.setup(800,400,200,200)
    init()
    #turtle.speed(10)
    # 肖
    change(0, 120)  # 将画笔放在坐标E（0， 150）
    run(-90, 120)  # 从E
    change(-90,90)
    run(-45,120)
    change(90,90)
    run(-135,120)

    change(-70,0)
    run(-90,160)
    change(-70, 0)
    run(0, 140)
    change(70,0)
    run(-90,160)
    run(135,30)
    change(-50, -50)
    run(0, 100)
    change(-50, -100)
    run(0, 100)
    # 朝
    startx = 0
    starty = 0
    change(-150,90)
    run(0,100)
    change(-100,120)
    run(-90,80)

    change(-140,40)
    run(-90,80)
    change(-140,40)
    run(0,80)
    run(-90,80)
    change(-140,0)
    run(0,80)
    change(-140,-40)
    run(0,80)

    change(-150, -90)
    run(0, 100)
    change(-100,-40)
    run(-90,120)

    change(-10,80)
    run(-90,240)

    change(-10, 80)
    run(0,80)
    run(-90,240)
    run(135,30)

    change(-10, 0)
    run(0, 80)
    change(-10, -40)
    run(0, 80)

    # 穗
    startx = 220
    starty = 0
    change(-30,120)
    run(-135,70)

    change(-100,20)
    run(0,100)

    change(-50,90)
    run(-90,160+20+80)
    change(-50,20)
    run(-135,70)
    change(-50, 20)
    run(-45, 60)

    change(20,80)
    run(0,80)
    change(10,40)
    run(-90,80)
    change(10,40)
    run(0,100)
    run(-90,80)
    change(10,0)
    run(0,100)
    change(10,-40)
    run(0,100)
    change(60,105)
    run(-90,105+95)
    change(10,-95)
    run(0,100)
    change(100,-85)
    run(-45,20)
    change(20,-120)
    run(-135,20)
    change(40,-110)
    run(-90,50)
    run(0,95)
    run(135,30)
    change(60,-115)
    run(-45,20)
    change(135,-130)
    run(-45,10)
    turtle.done()
