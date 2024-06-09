from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard



screen = Screen()
screen.bgcolor("black")
screen.setup(width = 600, height = 600)
screen.title("My Snake game🐍")
screen.listen()
# it stops update the screen
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkeypress(snake.move_fast, "space")


game_is_on = True
while game_is_on:
    # when screen.update is called then it updates the screen only
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) < 15:
        if food.food_color == "white":
            scoreboard.increase_score(1)
        elif food.food_color == "yellow":
            scoreboard.increase_score(2)
        elif food.food_color == "red1":
            scoreboard.increase_score(3)
        food.refresh()
        snake.extend()
    
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        snake.reset_snake()
        scoreboard.reset()

    for segment in snake.segments[1: len(snake.segments)]:
        if snake.head.distance(segment) < 10:
            snake.reset_snake()
            scoreboard.reset()



screen.exitonclick()