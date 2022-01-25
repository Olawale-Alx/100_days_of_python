from turtle import Turtle, Screen


jim = Turtle()
# jimmy_the_turtle.shape('turtle')
jim.color('red', 'beige')
jim.speed(1)

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
color = ['red', 'green', 'blue', 'black', 'orange', 'yellow', 'brown', 'beige', 'pink', ]


# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360/num_sides
#         jim.forward(60)
#         jim.right(angle)
#
#
# for shape_sides in range(3, 11):
#     jim.color(color[shape_sides - 3])
#     draw_shape(shape_sides)


print(jim.position())

screen = Screen()
screen.title('Turtle')
screen.exitonclick()
