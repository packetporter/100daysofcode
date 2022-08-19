from turtle import Turtle, Screen


def move_forward():
    toto.forward(10)


def move_backward():
    toto.backward(10)


def counter_clockwise():
    toto.left(10)


def clockwise():
    toto.right(10)


def cleanup_screen():
    screen.clearscreen()


toto = Turtle()
screen = Screen()
screen.listen()

screen.onkey(fun=move_forward, key="W")
screen.onkey(fun=move_backward,key="S")
screen.onkey(fun=counter_clockwise, key="A")
screen.onkey(fun=clockwise, key="D")
screen.onkey(fun=cleanup_screen, key="C")











screen.exitonclick()