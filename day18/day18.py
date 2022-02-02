import turtle
from turtle import Turtle, Screen
import random


number_of_dots = int(input('Enter the number of dots you want to draw: '))

turtle.colormode(255)
color_list = [[175, 19, 44], [116, 178, 201], [180, 74, 41], [206, 161, 101], [30, 119, 161],
              [21, 136, 82], [182, 45, 64], [219, 62, 96], [21, 34, 67], [186, 179, 24],
              [73, 171, 100], [215, 134, 156], [237, 231, 4], [127, 182, 129], [40, 44, 114],
              [215, 75, 55], [19, 165, 209], [9, 53, 33], [11, 96, 54], [163, 24, 20],
              [233, 166, 181], [152, 208, 219], [160, 210, 182], [233, 174, 165], [90, 23, 59],
              [7, 84, 110], [90, 23, 19], [115, 121, 145], [177, 187, 214], [255, 6, 27]]

tim = Turtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed(9)
tim.hideturtle()
screen = Screen()
screen.bgcolor('black')
# number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(30)

    if dot_count % 15 == 0:
        tim.setheading(90)
        tim.forward(30)
        tim.setheading(180)
        tim.forward(450)
        tim.setheading(0)

screen.exitonclick()
