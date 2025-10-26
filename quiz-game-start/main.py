from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for ques in question_data:
    # adding object of every entry in question data as an object in question bank
    question_bank.append(Question(ques["text"],ques["answer"]))
    


quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number} ")