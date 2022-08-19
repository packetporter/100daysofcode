from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=800, height=700)
user_choice = screen.textinput(title="Make your bet", prompt="Which turtle are you betting on? Enter it's color: ")

colors = ["red", "orange", "green", "yellow", "blue", "purple"]
turtle_list = []
y_pos = 250
race_on = False
for num in range(len(colors)):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[num])
    t.goto(-350, y_pos)
    y_pos -= 100
    turtle_list.append(t)

if user_choice:
    race_on = True

while race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 380:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You have won!. The {winning_color} turtle is the winner.")
            else:
                print(f"You have lost!. The {winning_color} turtle is the winner.")
        rand_step = randint(0, 10)
        turtle.forward(rand_step)










screen.exitonclick()