quiz = {
    "stimulus": "Answer the following algebra question:",
    "stem": "If x = 8, then what is the value of 4(x+3)?",
    "answers": [35, 36, 40, 44],
    "right_choice": "4",
}

print(quiz["stimulus"])
print(quiz["stem"])

position = 0
for i in quiz["answers"]:
    print(position + 1, quiz["answers"][position])
    position += 1

int_answer = input("Your choice: ")

if int_answer == quiz["right_choice"]:
    print("Bingo")
else:
    print(":(")


