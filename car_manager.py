import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 20


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in range(len(self.cars)):
            self.cars[car].forward(STARTING_MOVE_DISTANCE)

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            timmy = Turtle()
            timmy.shape('square')
            timmy.color(COLORS[random.randint(0, len(COLORS)-1)])
            timmy.shapesize(stretch_wid=1, stretch_len=2)
            timmy.penup()
            timmy.goto(280, random.randint(-250, 250))
            timmy.right(180)
            self.cars.append(timmy)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
