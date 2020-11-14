# 导入turtle库
import turtle
'''
绘图窗口的原点(0,0)在正中间，前方即右边
运动命令
forward(d)
backward(d)
right(d)
left(d)
goto(x,y) 移动到x,y的位置
speed(s) 壁画绘制的速度

笔画控制命令
up()  抬笔
down()
setheading(d) 改变海龟的朝向
pensize(d)
pencolor(color) 笔画颜色
reset()  恢复所有设置，重置turtle
clear()  清空窗口,不重置turtle
circle(r,e)  绘制圆形，r为半径，e为次数

begin_fill()
fillcolor(colorstr)
end_fill()

其他命令
done() 程序继续执行
undo() 撤销上一次动作
hideturtle() 隐藏海龟
screensize() 
'''
turtle.screensize(1000,10,"green")
turtle.speed(5)
turtle.forward(100)
turtle.right(45)
turtle.pencolor("red")
turtle.forward(100)
turtle.goto(100,-200)
turtle.up()
turtle.goto(-100,-200)
turtle.down()
turtle.pensize(10)
turtle.goto(-100,20)
turtle.setheading(50)
turtle.pensize(10)
#turtle.reset()
turtle.circle(50)
turtle.forward(100)

turtle.begin_fill()
turtle.fillcolor("blue")
turtle.circle(50,steps=5)
turtle.end_fill()
#turtle.undo()
turtle.hideturtle()
turtle.done()

