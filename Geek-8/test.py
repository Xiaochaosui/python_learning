import turtle


def square(len,c,n):
    turtle.color(c)
    turtle.begin_fill()
    for i in range(0,n):
        turtle.forward(len)
        turtle.right(360/n)
    turtle.end_fill()


square(100,"yellow",8)

turtle.done()