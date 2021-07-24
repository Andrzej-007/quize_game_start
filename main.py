
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for i in question_data:
    q = i['question']
    a = i['correct_answer']
    question_bank.append(Question(q, a))

# print(f'question_bank : {question_bank}')
# print(question_bank[0].text)
# print(f'how much questions : {len(question_bank)}')

user_quiz = QuizBrain(question_bank)

while user_quiz.still_has_guestions():
    user_quiz.next_question()


print(f'your final scoue  {user_quiz.user_points} out of questions {user_quiz.question_number}')

# https://opentdb.com/api_config.php