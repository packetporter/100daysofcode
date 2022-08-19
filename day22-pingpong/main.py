import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Ping Pong Game")

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

update_delay = 0.1

while True:
    screen.update()
    time.sleep(update_delay)
    ball.move()

# Detect collision with the upper and lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
# Detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        update_delay -= 0.01
# Detect when the right paddle misses the ball
    if ball.xcor() > 380:
        scoreboard.l_point()
        update_delay = 0.1
        ball.restart()

# Detect when the left paddle misses the ball
    if ball.xcor() < -380:
        scoreboard.r_point()
        update_delay = 0.1
        ball.restart()
screen.exitonclick()
