from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 11, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(x=0, y=270)
        self.write(f'Score: {self.score}', align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGN, font=FONT)
