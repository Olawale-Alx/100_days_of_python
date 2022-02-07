from turtle import Turtle, Screen

fim = Turtle()
screen = Screen()


def forward():
    fim.forward(50)


def backward():
    fim.backward(50)


def left():
    fim_heading = fim.heading() + 10
    fim.setheading(fim_heading)


def right():
    fim_heading = fim.heading() - 10
    fim.setheading(fim_heading)


def clear():
    fim.clear()
    fim.penup()
    fim.hideturtle()
    fim.home()
    fim.showturtle()


screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='a', fun=right)
screen.onkey(key='d', fun=left)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
