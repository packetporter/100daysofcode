from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for quiz in question_data:
    question = Question(quiz["question"], quiz["correct_answer"])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"You've completed the quiz \nYour final score is: {quiz_brain.score}/{len(question_bank)}")