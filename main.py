import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

timmy = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(timmy.move, "Up")

increment = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.create_car()
    car.move()
    if timmy.ycor() > 280:
        timmy.finish_line()
        car.increase_speed()
        scoreboard.increment_level()

    for moving_car in car.cars:
        if timmy.distance(moving_car) < 20:
            scoreboard.game_over()
            game_is_on = False

    increment += 1

    screen.update()

screen.exitonclick()
