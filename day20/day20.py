from turtle import Screen
from snakey import Snakey
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Snake Xenzia')
screen.bgcolor('black')
screen.tracer(0)

snakey = Snakey()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snakey.move()

screen.exitonclick()
