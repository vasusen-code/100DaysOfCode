from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.goto((-100, 200))
        self.write(self.r_score, align="center", font=("Courier", 60, "bold"))
        self.goto((100, 200))
        self.write(self.l_score, align="center", font=("Courier", 60, "bold"))

    def increase_l_score(self):
        self.l_score += 1

    def increase_r_score(self):
        self.r_score += 1

    def update_scoreboard(self):
        self.clear()
        self.goto((-100, 200))
        self.write(self.r_score, align="center", font=("Courier", 60, "bold"))
        self.goto((100, 200))
        self.write(self.l_score, align="center", font=("Courier", 60, "bold"))


