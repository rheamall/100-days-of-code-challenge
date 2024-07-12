from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i['text'], i['answer']))

quiz = QuizBrain(question_bank)
score = 0

while quiz.still_has_questions():
    ans = quiz.next_question()
    score = quiz.check_answer(score, question_bank, ans)

print(f'\nGame end. Your final score was {score}/{quiz.question_number}. Thanks for playing!')
