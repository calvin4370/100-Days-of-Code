from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dict in question_data["results"]:
    question = Question(dict["question"], dict["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

for i in range(5):
    quiz.print_question_and_get_answer()

quiz.end_quiz()