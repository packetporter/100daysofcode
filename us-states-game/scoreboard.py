from turtle import Turtle
import pandas
FONT = ('Arial', 10, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.score = 0
        self.data = pandas.read_csv("50_states.csv")
        self.state_list = self.data.state.to_list()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score}/50 states correct", align="center", font=FONT)

    def check_answer(self, user_guess):
        state = self.data[self.data.state == user_guess]
        if user_guess in self.state_list:
            state_x_cor = int(state.x)
            state_y_cor = int(state.y)
            self.goto(state_x_cor, state_y_cor)
            self.write(f"{user_guess}", align="center", font=FONT)
            self.score += 1