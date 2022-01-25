from turtle import Turtle, Screen
# import turtle as t
import random

jim = Turtle()
# # jimmy_the_turtle.shape('turtle')
# jim.color('red', 'beige')
# jim.speed(1)

# jimmy_the_turtle.forward(70)
# jimmy_the_turtle.right(90)
# jimmy_the_turtle.forward(70)
# jimmy_the_turtle.home()
# jimmy_the_turtle.penup()
# jimmy_the_turtle.resizemode('user')
# jimmy_the_turtle.turtlesize(2, 2, 5)
# lexi = jimmy_the_turtle.clone()
# jimmy_the_turtle.circle(90, 180)
# jimmy_the_turtle.dot(50, 'purple')
# jimmy_the_turtle.onclick(1.5, 1, True)
# jimmy_the_turtle.undo()
# jimmy_the_turtle.stamp()
# jimmy_the_turtle.fd(180)
# for _ in range(4):
#     jim.forward(100)
#     jim.right(90)
# for _ in range(15):
#     jim.forward(10)
#     jim.penup()
#     jim.forward(10)
#     jim.pendown()
# for _ in range(3):
#     jim.forward(60)
#     jim.right(120)
# for _ in range(4):
#     jim.forward(60)
#     jim.right(90)
# for _ in range(5):
#     jim.forward(60)
#     jim.right(72)
# for _ in range(6):
#     jim.forward(60)
#     jim.right(60)
# for _ in range(7):
#     jim.forward(60)
#     jim.right(51.42)
# for _ in range(8):
#     jim.forward(60)
#     jim.right(45)
# for _ in range(9):
#     jim.forward(60)
#     jim.right(40)
# for _ in range(10):
#     jim.forward(60)
#     jim.right(36)
screen = Screen()
# screen.bgcolor('green yellow')
screen.title('Turtle')
# t.colormode(255)
color = ['red', 'green', 'blue', 'black', 'orange', 'yellow', 'brown', 'beige', 'pink',
         'Medium Blue', 'silver', 'steel blue', 'dark khaki', 'magenta', 'crimson', 'white',
         'sandy brown', 'moccasin', 'green', 'green yellow', 'lawn green', ]
# positioning = [0, 90, 180, 270]

# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360/num_sides
#         jim.forward(60)
#         jim.right(angle)
#
#


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_list = (r, g, b)
    return color_list


# jim.speed(9)
# jim.resizemode('user')
jim.hideturtle()
# jim.pensize(15)
#
# for _ in range(300):
#     jim.color(random_color())
#     jim.forward(30)
#     jim.setheading(random.choice(positioning))
screen.bgcolor('black')
jim.pensize(9)
jim.speed(9)
for _ in range(36):
    jim.color(random.choice(color))
    jim.circle(160)
    jim.left(10)


print(jim.position())


screen.exitonclick()
