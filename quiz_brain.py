

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list   # q_list <--- object from question_model
        self.user_points = 0


    def still_has_guestions(self):
        return self.question_number <  len(self.question_list)


    def next_question(self):

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            user_answer = input(f'Q.{self.question_number} {current_question.text } True / False)?: ')
            if user_answer == "True" or user_answer == "False":
                break

        self.check_answer(user_answer, current_question )



    def check_answer(self,user_answer, current_question ):

        if user_answer == current_question.answer:
            print(f'Your got it right')
            print(f'the correct answer was: {user_answer}')
            self.user_points += 1
            print(f'You courent score / questions is {self.user_points}/ {self.question_number} ')


        else:
            print(f'You wrong sore  / questions:  {self.user_points}/ {self.question_number} ')

        print('\n')






# Asking the questions
# Checking if the answer war correct
# Checking if we’re the end of the quiz
# Q.1: ……………… . (True / False)? :
# Class QuizBrain:
#
# question_number = 0
# question_list =
#
# Methods  : next_question()