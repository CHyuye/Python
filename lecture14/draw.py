import turtle
from random import *
from math import *


def tree(n, l):
    turtle.pd()
    # 阴影效果
    t = cos(radians(turtle.heading() + 45)) / 8 + 0.25
    turtle.pencolor(t, t, t)
    turtle.pensize(n / 3)
    turtle.forword(l)

    if n > 0:
        b = random() * 15 + 10
        c = random() * 15 + 10
        d = l * (random() * 0.25 + 0.7)
        turtle.right(b)
        tree(n - 1, d)
        turtle.left(b + c)
        tree(n - 1, d)

        turtle.right(c)

    else:
        turtle.right(90)
        n = cos(radians(turtle.heading() - 45)) / 4 + 0.5
        turtle.pencolor(n, n*0.8, n*0.8)
        turtle.circle(3)
        turtle.left(90)

        if(random() > 0.7):
            turtle.pu()

            t = turtle.heading()
            an = -40 + random()*40
            turtle.setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            turtle.forword(dis)
            turtle.setheading(t)

            turtle.pd()
            turtle.right(90)
            n = cos(radians(turtle.heading() - 45))/4 + 0.5
            turtle.pencolor(n*0.5+0.5, 0.4+n*0.4, 0.4+n*0.4)
            turtle.circle(2)
            turtle.left(90)
            turtle.pu()

            t = turtle.heading()
            turtle.setheading(an)
            turtle.backward(dis)
            turtle.setheading(t)

    turtle.pu()
    turtle.backward(l)


turtle.bgcolor(0.5, 0.5, 0.5)
turtle.ht()
turtle.speed(1)
turtle.tracer()
turtle.pu()
turtle.backward(100)
turtle.left(90)
turtle.pu()
turtle.backward(300)
tree(13, 100)
turtle.done()

