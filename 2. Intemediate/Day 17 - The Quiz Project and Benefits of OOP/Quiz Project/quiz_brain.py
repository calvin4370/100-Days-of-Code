import random

class QuizBrain:
    def __init__(self, starting_questions):
        self.remaining_questions = starting_questions
        
        self.question_number = 0
        self.score = 0

        random.shuffle(self.remaining_questions)

    def print_question_and_get_answer(self):
        self.question_number += 1
        current_question = self.remaining_questions.pop()
        user_answer = input(f"\nQ{self.question_number}: {current_question.text} (True/False)? ")

        if user_answer.lower() == current_question.answer.lower():
            self.score += 1
            print(f"Correct! Current Score: {self.score}/{self.question_number}")
            return True
        else:
            print(f"Wrong! Current Score: {self.score}/{self.question_number}")
            return False
        
    def end_quiz(self):
        print(f"\nEnd of Quiz. Your score: ({self.score}/{self.question_number})")
