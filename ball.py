from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ball_move_speed = 0.1
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(0, 0)

    def move_right(self):
        self.setheading(35)

    def move_left(self):
        self.setheading(220)

    def bounce_right(self):
        self.setheading(180 - int(self.heading()))
        self.ball_move_speed *= 0.7

    def bounce_left(self):
        self.setheading(180 - int(self.heading()))
        self.ball_move_speed *= 0.7

    def bounce_up(self):
        self.setheading(360 - int(self.heading()))

    def bounce_down(self):
        self.setheading(360 - int(self.heading()))