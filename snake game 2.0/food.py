from turtle import Turtle
import random

FOOD_COLOR  = ["white","white", "white", "white", "white", "white", "white", "yellow", "yellow", "red1"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.food_color = ""
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def random_food_color(self):
        return random.choice(FOOD_COLOR)

    def refresh(self):
        self.food_color = self.random_food_color()
        self.color(self.food_color)
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)