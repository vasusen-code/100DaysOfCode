import turtle, random

def random_color():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    return (red, blue, green)

t = turtle.Turtle()
t.speed("fastest")
turtle.colormode(255)
t.pensize(5)

def random_path():
    for _ in range(300):
        t.color(random_color())
        t.forward(random.randint(0, 70))
        t.setheading(random.choice([0, 90, 180, 270]))

random_path()

screen = turtle.Screen()
screen.exitonclick()
