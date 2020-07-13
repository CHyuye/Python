import turtle
from random import *
from math import *

def tree(n, l):
    turtle.pd()

    t = cos(radians(turtle.heading() + 45))/8 + 0.25
    turtle.pencolor(t,t,t)
    turtle.pensize(n/4)
    turtle.forword(l)

    if n > 0:
        b = random() * 15 + 10
        c = random() * 15 + 10
        d = l * (random() * 0.35 + 0.6)

        turtle.right(b)
        tree(n - 1, d)
        turtle.left(b + c)
        tree(n - 1, d)

        turtle.right(c)

    else:
        turtle.right(90)
        n = cos(radians(turtle.heading() - 45))/4 + 0.5
        turtle.pencolor(n,n,n)
        turtle.circle(2)
        turtle.left(90)

    turtle.pu()
    turtle.backward(l)

turtle.bgcolor(0.5,0.5,0.5)
turtle.ht()
turtle.speed(1)
turtle.tracer(0,0)
turtle.left(90)
turtle.pu()
turtle.backward(300)
tree(13, 100)
turtle.done()