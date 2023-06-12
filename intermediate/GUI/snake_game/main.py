import time
from food import Food
from snake import Snake
from turtle import Screen
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

sanke_is_alive = True
while sanke_is_alive:
    screen.update()
    time.sleep(0.13)
    snake.move()
    
    if snake.head.distance(food) < 15:
        color_of_food = food.rgb
        food.refresh()
        snake.extend(color_of_food)
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
        or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        sanke_is_alive = False
        scoreboard.end_game()

    for segment in snake.segments:
        if segment != snake.head and snake.head.distance(segment) < 10:
            sanke_is_alive = False
            scoreboard.end_game()
         

screen.exitonclick()


