# Create a new scoreboard class, inherits from turtle class like food, scoreboard is turtle (how to track and display the score)

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250) # Top Center, which means we will have to make changes to snake & food movement i think.
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

