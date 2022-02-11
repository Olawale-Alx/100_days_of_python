from turtle import Turtle, Screen

screen = Screen()
screen.listen()
turtles = Turtle()
turtles.shape('square')


def up():
    turtles.setheading(90)
    turtles.forward(50)


def down():
    turtles.setheading(270)
    turtles.forward(50)


def left():
    turtles.setheading(180)
    turtles.forward(50)


def right():
    turtles.setheading(0)
    turtles.forward(50)


screen.onkey(right, 'Right')
screen.onkey(left, 'Left')
screen.onkey(up, 'Up')
screen.onkey(down, 'Down')

screen.exitonclick()
