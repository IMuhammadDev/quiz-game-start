from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
number_of_que = 1

for item in question_data:
    question_object = Question(item["text"], item["answer"])
    question_bank.append(question_object)

quiz = QuizBrain(question_list=question_bank)

while quiz.still_has_question():
    quiz.next_question()
print(f"You have completed the quiz !")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
