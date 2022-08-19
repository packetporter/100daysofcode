from turtle import Turtle, Screen
from random import choice,randrange


def moveit_moveit(steps, angle):
    toto.pencolor(randrange(255), randrange(255), randrange(255))
    toto.forward(steps)
    toto.setheading(angle)


toto = Turtle()
screen = Screen()

toto.shape("classic")
toto.speed(1)
screen.colormode(255)

toto.pensize(10)
while True:
    step_size = choice([20, -20])
    angle_choice = choice([0, 90, 180, 270])
    moveit_moveit(step_size, angle_choice)
