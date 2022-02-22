from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snakey:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for square in POSITION:
            self.add_segment(square)

    def add_segment(self, square):
        # Creates a new segment
        new_square = Turtle(shape='square')
        new_square.penup()
        new_square.color('white')
        new_square.goto(square)
        self.squares.append(new_square)

    def extend(self):
        # Adds a new segment to snakey
        self.add_segment(self.squares[-1].position())

    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.squares[0].forward(MOVE_DISTANCE)

    def right(self):
        if self.squares[0].heading() != LEFT:
            self.squares[0].setheading(RIGHT)

    def up(self):
        if self.squares[0].heading() != DOWN:
            self.squares[0].setheading(UP)

    def left(self):
        if self.squares[0].heading() != RIGHT:
            self.squares[0].setheading(LEFT)

    def down(self):
        if self.squares[0].heading() != UP:
            self.squares[0].setheading(DOWN)
