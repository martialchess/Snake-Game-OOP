from turtle import Screen, Turtle
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

border = Turtle()
border.hideturtle()
border.speed("fastest")
border.color("white")
border.pensize(10)

# Go to top-left corner
border.penup()
border.goto(-280, 280)
border.pendown()

# Draw square border
for _ in range(4):
    border.forward(560)
    border.right(90)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
 
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        # updated_score
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if (
        snake.head.xcor() >= 280
        or snake.head.xcor() <= -280
        or snake.head.ycor() >= 280
        or snake.head.ycor() <= -280
        ):
        print(f"Game Over! Hit the wall 🚧 Final Score: {scoreboard.score}")
        game_is_on = False

    # Detect collision with tail

    for segment in snake.segments[1:]: # skip the head at index 0
        if snake.head.distance(segment) < 15:
            print(f"Game Over! Ran into yourself 🌀 Final Score: {scoreboard.score}")
            game_is_on = False




screen.exitonclick()