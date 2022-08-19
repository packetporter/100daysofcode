import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
speed_multiplier = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.new_car()
    cars.car_move()

    # Detect collision with the car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect player has successfully crossed
    if player.ycor() > 280:
        player.restart()
        scoreboard.level_up()
        cars.increase_speed()

screen.exitonclick()