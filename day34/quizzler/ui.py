from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        logo = PhotoImage(file='images/true.png')
        self.window.iconphoto(False, logo)
        self.window.minsize(height=600, width=380)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text=f'Score: 0', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=330, height=300, highlightthickness=0, bg='white')
        self.canvas.create_text(165, 150, text='Amazon Woman', font=('Arial', 20, 'italic'),
                                justify='center', fill=THEME_COLOR)
        self.canvas.grid(padx=20, pady=30, row=1, column=0, columnspan=2)

        correct_photo = PhotoImage(file='images/true.png')
        self.correct_button = Button(image=correct_photo, highlightthickness=0)
        self.correct_button.grid(row=2, column=0)

        wrong_photo = PhotoImage(file='images/false.png')
        self.wrong_button = Button(image=wrong_photo, highlightthickness=0)
        self.wrong_button.grid(row=2, column=1)

        self.window.mainloop()
