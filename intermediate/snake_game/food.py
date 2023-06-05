import turtle
from random import randint

class Food(turtle.Turtle):

    turtle.colormode(255)

    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()
        self.rgb = (255, 255, 255)

    def refresh(self):
        """ Generates food at random position of random color """

        red = randint(10, 255)
        green = randint(10, 255)
        blue = randint(10, 255)
        rgb = (red, green, blue)
        self.rgb = rgb
        self.color(rgb)

        xcor = randint(-280, 280)
        ycor = randint(-280, 280)
        self.goto(x=xcor, y=ycor)
        
