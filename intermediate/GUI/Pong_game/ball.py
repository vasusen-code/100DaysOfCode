from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.penup()
        self.x_move = -15
        self.y_move = 15
        
    def move(self):
        self.goto((self.xcor() + self.x_move, self.ycor() + self.y_move))

    def bounce(self, bounce_from_paddle=False):
        if bounce_from_paddle:
            self.x_move *= -1
            return
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1

    def refresh(self):
        self.goto((0, 0))
        self.x_move *= -1
        self.y_move *= -1
