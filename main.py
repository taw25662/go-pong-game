from turtle import Screen
from ball import Ball
from paddles import Paddle
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

left_paddle = Paddle(-280)
right_paddle = Paddle(270)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)

game_is_on = True
counter = 0
ball.move_right()
scoreboard.update_scoreboard()
while game_is_on:
    screen.update()
    time.sleep(ball.ball_move_speed)
    ball.forward(8)
    if ball.xcor() <= -290:
        counter += 1
        right_paddle.goto(270,0)
        left_paddle.goto(-280,0)
        ball.goto(0,0)
        if counter % 2 == 0:
            ball.move_right()
            ball.ball_move_speed = 0.1
        if counter % 2 != 0:
            ball.ball_move_speed = 0.1
            ball.move_left()
        scoreboard.r_point()
    if ball.xcor() >= 290:
        counter += 1
        right_paddle.goto(270, 0)
        left_paddle.goto(-280, 0)
        ball.goto(0, 0)
        if counter % 2 == 0:
            ball.move_right()
            ball.ball_move_speed = 0.1
        elif counter % 2 != 0:
            ball.move_left()
            ball.ball_move_speed = 0.1
        scoreboard.l_point()
    if ball.ycor() >= 290:
        ball.bounce_down()
    if ball.ycor() <= -280:
        ball.bounce_up()
    if ball.distance(left_paddle) <= 40 and ball.xcor() <= -265:
        ball.bounce_right()
    if ball.distance(right_paddle) <= 40 and ball.xcor() >= 260:
        ball.bounce_left()

screen.update()

screen.exitonclick()
