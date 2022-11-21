from w2d1_quiz_questions import Question

question_prompts = [
    "1. What brand of car is a Fielder?\n(a) Mazda \n(b) Ferrari \n(c) Toyota \n ---> Answer: ",
    "2. What brand of car is a Skyline?\n(a) Nissan \n(b) Ford \n(c) Maserati \n ---> Answer: ",
    "3. What brand of car is a Mondeo?\n(a) BMW \n(b) Volvo \n(c) Ford \n ---> Answer: ",
    "4. What brand of car is a C-180?\n(a) GM \n(b) Mercedes \n(c) Skoda \n ---> Answer: ",
    "5. What brand of car is a Vitara?\n(a) Alfa Romeo \n(b) Suzuki \n(c) Kia \n ---> Answer: "
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "b"),
]

#loop through questions and add score
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Your final score is: " + str(score) + " out of " + str(len(questions)))

run_test(questions)