from question_model import Question
from data import question_data
# list of question objects
question_bank = []
for i in question_data:
    question = Question(i["text"], i["answer"])
    question_bank.append(question)
