from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_list =[]
for q in question_data:
    question_list.append(Question(q['question'],q['correct_answer']))

quiz = QuizBrain(question_list)
while quiz.still_has_questions():
    quiz.next_question()