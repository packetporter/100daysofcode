from turtle import Turtle

DISTANCE = 20
UP = 90
DOWN = 270
X_POS = 350
y_POS = 0


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_pos, 0)

    def go_up(self):
        new_pos = self.ycor() + 20
        self.goto(self.xcor(), new_pos)

    def go_down(self):
        new_pos = self.ycor() - 20
        self.goto(self.xcor(), new_pos)
