import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x_food = random.randint(-280, 250)
        y_food = random.randint(-270, 280)
        self.goto(x_food, y_food)
