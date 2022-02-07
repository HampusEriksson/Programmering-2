import random


class Question:

    def __init__(self, question, correct_answer, *wrong_answers):
        self.question = question
        self.correct_answer = correct_answer
        self.wrong_answers = wrong_answers
        self.answers = [correct_answer] + list(wrong_answers)
        random.shuffle(self.answers)

questions = [
    Question("What color is a banana?", "yellow", "blue", "red", "purple"),
    Question("When was the kalmar union formed?", "1743", "1942", "1875", "2bc"),
    Question("What's the top speed of the paragram falcon?", "Nånting galen jag har ingen aning", "200km/h", "300mph", "20m/s")
]

score = 0

for q in questions:
    print(q.question)
    print(*q.answers)
    ans = input("What is your answer?")
    if ans == q.correct_answer:
        score += 1

print(score)