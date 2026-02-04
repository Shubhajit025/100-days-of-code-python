from data import question_data
from question_model import Question
from  quiz_brain import QuizBrain

question_bank = []
# Done by me 👇
# print(len(question_data))
# for char in range(0, 12):
#     question_bank.append(question_data[char]["text"])
#     question_bank.append(question_data[char]["answer"])
# print(question_bank) # We can separate using `sep="\n"` and unlisting by using * sign before list holding var.
# Done by me 👆

# Made this after watching class 👇
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
