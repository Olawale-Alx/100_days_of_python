from turtle import Turtle
from gameart import game_art

ALIGN = 'center'
FONT = ('Courier', 11, 'normal')
game_art = game_art


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

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f'{game_art}', align=ALIGN, font=('Courier', 10, 'normal'))
        print('\n')
        self.write(f'Total Score: {self.score}', align=ALIGN, font=FONT)
