import turtle
from random import choice

toto = turtle.Turtle()
turtle.colormode(255)
screen = turtle.Screen()
toto.penup()
toto.hideturtle()
screen.screensize(10, 10)

color_list = [(144, 76, 50), (188, 165, 117), (248, 244, 246), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45)]

print(screen.screensize())
y_pos = 0

while y_pos < 500:
    toto.goto(-500, y_pos)
    toto.setheading(0)
    for step in range(10):
        color = choice(color_list)
        toto.dot(20, color)
        if step != 9:
            toto.forward(50)
        else:
            toto.setheading(90)
            toto.forward(50)
    y_pos += 50

screen.exitonclick()
