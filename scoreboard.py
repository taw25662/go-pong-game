from turtle import Turtle
FONT = ("Arial", 60, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("white")

    def update_scoreboard(self):
        self.goto(0, 240)
        self.write(arg=f"{self.l_score} | {self.r_score}", align="center", move=False, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()