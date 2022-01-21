class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False): ')
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('That\'s Right')
            self.score += 1
            print(f'Current Score: {self.score}/{self.question_number}')
        else:
            print('That\'s Wrong')
            print(f'Final Score: {self.score}/{self.question_number}')
        print(f'The correct answer is {correct_answer.lower()}\n')

    def print_total(self):
        print(f'Your final score is : {self.score}/{self.question_number}')
