from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def increment_level(self):
        self.clear()
        self.level += 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def game_over(self):
        self.write("GAME OVER", align='center', font=FONT)