from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data_file:
            self.high_score = int(data_file.read())
        self.penup()
        self.color("white")
        self.ht()
        self.setposition(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data_file:
                data_file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()




    # def game_over(self):
    #     self.setposition(0,0)
    #     self.write("GAME OVER.", align=ALIGNMENT, font=FONT)

