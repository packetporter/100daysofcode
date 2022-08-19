from turtle import Turtle, Screen
from random import randrange


def draw_shape(num_sides):
    toto.pencolor(randrange(255), randrange(255), randrange(255))
    for _ in range(num_sides):
        toto.forward(100)
        toto.right(360/num_sides)


toto = Turtle()
toto.shape("classic")
toto.pensize(3)
screen = Screen()
screen.colormode(255)

sides = 3
while sides <= 10:
    draw_shape(sides)
    sides += 1







screen.exitonclick()
































