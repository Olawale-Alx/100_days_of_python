import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.7)
        self.color('red')
        self.speed('fastest')
        x_food = random.randint(-280, 250)
        y_food = random.randint(-270, 280)
        self.goto(x_food, y_food)
        self.refresh()

    def refresh(self):
        x_food = random.randint(-280, 250)
        y_food = random.randint(-270, 280)
        self.goto(x_food, y_food)
