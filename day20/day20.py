from turtle import Screen
from snakey import Snakey
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Snake Xenzia')
screen.bgcolor('black')
screen.tracer(0)

snakey = Snakey()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food, add to score, increase snakey and change food location
    if snakey.head.distance(food) < 10:
        food.refresh()
        snakey.extend()
        scoreboard.increase_score()

    # Detect collision with game wall
    if snakey.head.xcor() > 295 or snakey.head.xcor() < -305 or snakey.head.ycor() > 300 or snakey.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for square in snakey.squares:
        if square == snakey.head:
            pass

        elif snakey.head.distance(square) < 8:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
