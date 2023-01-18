from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-270, y=250)
        self.write(f"Level: {self.score}", font=FONT)

    def level_up(self):
        self.score += 1
        self.update_scoreboard()
