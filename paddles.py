from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=0.5)
        self.goto(position, 0)

    def move_up(self):
        self.setheading(90)
        self.forward(10)
        self.setheading(0)

    def move_down(self):
        self.setheading(270)
        self.forward(10)
        self.setheading(0)