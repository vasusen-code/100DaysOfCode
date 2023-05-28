import turtle, random

def random_color():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    return (red, blue, green)

t = turtle.Turtle()
t.speed("fastest")
turtle.colormode(255)
t.pensize(2)

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + 10)

draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()
