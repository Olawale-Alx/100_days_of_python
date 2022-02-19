from turtle import Screen
from snakey import Snakey
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Snake Xenzia')
screen.bgcolor('black')
screen.tracer(0)

snakey = Snakey()
food = Food()

screen.listen()
screen.onkey(snakey.up, 'Up')
screen.onkey(snakey.down, 'Down')
screen.onkey(snakey.left, 'Left')
screen.onkey(snakey.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snakey.move()

    # Detect collision with food and change food location
    if snakey.head.distance(food) < 10:
        food.refresh()

screen.exitonclick()
