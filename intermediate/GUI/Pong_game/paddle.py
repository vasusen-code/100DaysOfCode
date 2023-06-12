from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position:tuple):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(position)
        self.setheading(90)

    def move(self):
        self.forward(10)

    def move_up(self):
        self.setheading(90)
        self.goto((self.xcor(), self.ycor() + 20))

    def move_down(self):
        self.setheading(270)
        self.goto((self.xcor(), self.ycor() - 20))

