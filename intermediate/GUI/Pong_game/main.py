from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((-350, 0))
l_paddle = Paddle((350, 0)) 

screen.listen()
screen.onkey(r_paddle.move_up, "w")
screen.onkey(r_paddle.move_down, "s")
screen.onkey(l_paddle.move_up, "Up")
screen.onkey(l_paddle.move_down, "Down")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    sleep(0.13)
    screen.update()
    r_paddle.move(), l_paddle.move()
    ball.move()
    ball.bounce()
    if ball.distance(r_paddle) < 60 and ball.xcor() < -320 \
    or ball.distance(l_paddle) < 60 and ball.xcor() > 320:
        ball.bounce(bounce_from_paddle=True)
    if r_paddle.ycor() > 240:
        r_paddle.setheading(270)
    elif r_paddle.ycor() < -240:
        r_paddle.setheading(90)
    if l_paddle.ycor() > 240:
        l_paddle.setheading(270)
    elif l_paddle.ycor() < -240:
        l_paddle.setheading(90)
    if ball.xcor() > 400:
        ball.refresh()
        scoreboard.increase_r_score()
    if ball.xcor() < -400:
        ball.refresh()
        scoreboard.increase_l_score()
    scoreboard.update_scoreboard()
