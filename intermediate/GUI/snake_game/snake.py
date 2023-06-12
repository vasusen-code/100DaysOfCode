import turtle

MOVING_DISTANCE = 20
up, down, right, left = 90, 270, 0, 180
starting_positions = starting_positions = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    turtle.colormode(255)

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position, (255, 255, 255))

    def add_segment(self, position, color):
        """add a new segment to your snake"""
        new_segment = turtle.Turtle("square")
        new_segment.color(color)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)   
    
    def move(self):
        """moves the snake forward"""
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.segments[0].forward(MOVING_DISTANCE)

    def extend(self, color):
        self.add_segment(self.segments[-1].position(), color)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
        
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

