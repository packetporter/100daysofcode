import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return r, b, g


def draw_spirograph(deviation):
    deviation_constant = deviation
    while deviation <= 360:
        toto.color(random_color())
        toto.circle(200)
        toto.right(deviation_constant)
        deviation += deviation_constant


t.colormode(255)
toto = t.Turtle()
screen = t.Screen()
toto.pensize(2)
toto.speed(0)

draw_spirograph(2)







screen.exitonclick()