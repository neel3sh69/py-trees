import random
import turtle

turtle.speed('fastest')

# turning the turtle to face upwards
turtle.rt(-90)

# the acute angle between
# the base and branch of the Y

# when not random:
# angle = 30

turtle.width(6)


# function to plot a Y
def y(sz, level):
    angle = random.randint(10, 40)
    change = random.randint(0, 3)
    level = level - change

    if level > 15:
        turtle.width(25)
    elif level > 10:
        turtle.width(15)
    elif level > 5:
        turtle.width(10)
    else:
        turtle.width(6)

    if level > 0:
        turtle.colormode(255)

        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level

        if level > 14:
            turtle.pencolor('saddle brown')
        elif level > 9:
            turtle.pencolor('sienna')
        else:
            turtle.pencolor(0, 127 + (127 // level), 0)

        # drawing the base
        turtle.fd(sz)

        turtle.rt(angle)

        # recursive call for
        # the right subtree
        y(0.8 * sz, level - 1)

        if level > 14:
            turtle.pencolor('saddle brown')
        elif level > 9:
            turtle.pencolor('sienna')
        else:
            turtle.pencolor(0, 127 + (127 // level), 0)

        turtle.lt(2 * angle)

        # recursive call for
        # the left subtree
        y(0.8 * sz, level - 1)

        if level > 14:
            turtle.pencolor('saddle brown')
        elif level > 9:
            turtle.pencolor('sienna')
        else:
            turtle.pencolor(0, 127 + (127 // level), 0)

        turtle.rt(angle)
        turtle.fd(-sz)


def root(sz, level):
    angle = random.randint(10, 30)
    change = random.randint(0, 3)
    level = level - change

    if level > 15:
        turtle.width(25)
    elif level > 10:
        turtle.width(15)
    elif level > 5:
        turtle.width(10)
    else:
        turtle.width(6)

    if level > 0:
        turtle.colormode(255)

        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level

        if level > 14:
            turtle.pencolor('saddle brown')
        elif level > 9:
            turtle.pencolor(94, 44, 8)
        else:
            turtle.pencolor(61, 27, 2)

        # drawing the base
        turtle.bk(sz)

        turtle.lt(angle)

        # recursive call for
        # the right subtree
        root(0.8 * sz, level - 1)

        if level > 14:
            turtle.pencolor('saddle brown')
        elif level > 9:
            turtle.pencolor(94, 44, 8)
        else:
            turtle.pencolor(61, 27, 2)

        turtle.rt(2 * angle)

        # recursive call for
        # the left subtree
        root(0.8 * sz, level - 1)

        if level > 14:
            turtle.pencolor('saddle brown')
        elif level > 9:
            turtle.pencolor(94, 44, 8)
        else:
            turtle.pencolor(61, 27, 2)

        turtle.lt(angle)
        turtle.bk(-sz)
