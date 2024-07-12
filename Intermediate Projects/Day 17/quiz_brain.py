class QuizBrain:
    def __init__(self, qs_list):
        self.question_number = 0
        self.questions_list = qs_list

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        ans = input(f'\nQ.{self.question_number+1}: {self.questions_list[self.question_number].question} True/False? ').title()
        self.question_number += 1
        return ans

    def check_answer(self, score, question_bank, ans):
        if ans == 'True' or ans == 'False':
            if ans == question_bank[self.question_number - 1].answer:
                score += 1
                print(f'You got it right! Your current score is {score}/{self.question_number}')
            else:
                print(
                    f'Ah, the correct answer was actually {question_bank[self.question_number - 1].answer}. Your current '
                    f'score is {score}/{self.question_number}')
        else:
            print('Invalid input. You lose this point.')
            print(f'Your current score is {score}/{self.question_number}')
        return score