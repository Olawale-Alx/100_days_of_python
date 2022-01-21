from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
# This converts the questions and answers in the array to texts that
# can be used in OOP
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
