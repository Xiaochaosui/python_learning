import turtle


def zsh(length):
    for i in range(0,3):
        turtle.forward(length)
        turtle.right(120)



def sb(l):
    turtle.speed(l)


sb(0)

zsh(10)
zsh(50)
zsh(400)




turtle.done()


