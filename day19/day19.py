from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=900, height=400)

user_bet = screen.textinput(title='Place Bet', prompt='Which turtle will win the race. Enter a '
                                                      'color:').lower()
y_position = [-70, -30, 10, 50, 90, 130]
player_colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']
is_race_on = False
all_turtles = []

for turtle_start in range(0, 6):
    new_turtle = Turtle('turtle')
    new_turtle.shapesize(1.5)
    new_turtle.penup()
    new_turtle.color(player_colors[turtle_start])
    new_turtle.setposition(x=-435, y=y_position[turtle_start])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:

        if turtle.xcor() > 425:
            is_race_on = False
            winner = turtle.pencolor()

            if winner == user_bet:
                print(user_bet)
                print(f'You have won! The winner is color {winner}')

            else:
                print(user_bet)
                print(f'You have lost! The winner is color {winner}')

        race_distance = random.randint(0, 10)
        turtle.forward(race_distance)

screen.exitonclick()
