import turtle
import random

import tree

turtle.speed('fastest')


def normalSpiral():
    turtle.bgcolor('white')
    turtle.colormode(255)
    x = 0
    turtle.speed(0)
    for x in range(360):
        r, b, g = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        turtle.pencolor(r, g, b)
        turtle.fd(x + 50)
        turtle.rt(91)
    turtle.exitonclick()


def hexagonSpiral():
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    t = turtle.Pen()
    turtle.bgcolor('black')
    for x in range(360):
        t.pencolor(colors[x % 6])
        t.width(x // 100 + 1)
        t.forward(x)
        t.left(59)

    turtle.exitonclick()


hexagonSpiral()
# turtle.back(100)
# tree.y(100, 24)
# tree.root(56, 18)
# turtle.exitonclick()
