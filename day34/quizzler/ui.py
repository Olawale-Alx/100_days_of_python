from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        logo = PhotoImage(file='images/true.png')
        self.window.iconphoto(False, logo)
        self.window.minsize(height=600, width=380)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text=f'Score: 0', fg='white', bg=THEME_COLOR, font=('Arial', 12, 'bold'),
                           justify='right')
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=330, height=300, highlightthickness=0, bg='white')
        self.question_text = self.canvas.create_text(165, 150, text='', font=('Arial', 16, 'italic'),
                                                     justify='center', fill=THEME_COLOR, width=310)
        self.canvas.grid(padx=20, pady=30, row=1, column=0, columnspan=2)

        correct_photo = PhotoImage(file='images/true.png')
        self.correct_button = Button(image=correct_photo, highlightthickness=0, cursor='hand2',
                                     command=self.right_answer)
        self.correct_button.grid(row=2, column=0)

        wrong_photo = PhotoImage(file='images/false.png')
        self.wrong_button = Button(image=wrong_photo, highlightthickness=0, cursor='hand2',
                                   command=self.wrong_answer)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')

        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
            self.score.config(text=f'Score: {self.quiz.score}/{self.quiz.question_number}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz.')
            self.correct_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def right_answer(self):
        is_right = self.quiz.check_answer('True')
        self.give_player_feedback(is_right)

    def wrong_answer(self):
        is_wrong = self.quiz.check_answer('False')
        self.give_player_feedback(is_wrong)

    def give_player_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg='green')
            self.canvas.itemconfig(self.question_text, fill='white')
        else:
            self.canvas.config(bg='red')
            self.canvas.itemconfig(self.question_text, fill='white')

        self.window.after(2000, self.get_next_question)
