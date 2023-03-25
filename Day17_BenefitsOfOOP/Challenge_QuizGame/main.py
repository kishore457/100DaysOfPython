from quiz_brain import QuizBrain
from question_model import Question
from data import question_data
# list of question objects
#1 start
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)
#1 end
# 2 start
quiz = QuizBrain(question_bank)
# 2 end
#3 start

while quiz.still_has_questions():
    # 2 start
    quiz.next_question()
    # 2 end

#3 end

print("You've completed the quiz")
print(f"Your final score was : {quiz.score} / {quiz.question_number}")
