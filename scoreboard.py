# Create a new scoreboard class, inherits from turtle class like food, scoreboard is turtle (how to track and display the score)
import random
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.highscore = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250) # Top Center, which means we will have to make changes to snake & food movement i think.
        with open("data.txt", "r") as file:
            self.highscore = int(file.read())
        self.update_score()
                

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Courier", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("data.txt", "w") as file:
            file.write(str(self.highscore)) # save new highscore
            # Instructor Alt: file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Courier", 15, "normal"))

