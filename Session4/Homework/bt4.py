#Implement quiz program 1:
quiz_1 = {
    "stimulus": "Answer the following algebra question:",
    "stem": "If x = 8, then what is the value of 4(x+3)?",
    "answers": [35, 36, 40, 44],
    "right_choice": "4",
}

print(quiz_1["stimulus"])
print(quiz_1["stem"])

position = 0
for i in quiz_1["answers"]:
    print(position + 1, quiz_1["answers"][position])
    position += 1

int_answer1 = input("Your choice: ")

if int_answer1 == quiz_1["right_choice"]:
    print("Bingo")
else:
    print(":(")

#Implement quiz program 2:
quiz_2 = {
    "stimulus": "Estimate this answer (exact calculation not needed)",
    "stem": "Jack scored these marks in 5 maths tests: 49, 81, 72, 66 and 52. What is the mean?",
    "choices": ["About 55", "About 65", "About 75", "About 85"],
    "answer": "2",
}

print(quiz_2["stimulus"])
print(quiz_2["stem"])

position = 0
for i in quiz_2["choices"]:
    print(position +1, quiz_2["choices"][position])

int_answer2 = input("Your choice: ")

if int_answer2 == quiz_2["answer"]:
    print("Bingo")
else:
    print(":(")

if int_answer1 == quiz_1["right_choice"] and int_answer2 == quiz_2["answer"]:
    print("You correctly answer 2 out of 2 questions.")
elif not int_answer1 == quiz_1["right_choice"] and not int_answer2 == quiz_2["answer"]:
    print("You correctly answer 0 out of 2 questions.")
else:
    print("You correctly answer 1 out of 2 questions.")