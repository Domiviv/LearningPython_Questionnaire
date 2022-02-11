# List of questions
questions = ["What is the capital of Belgium? ",
             "What is the capital of France? ",
             "What is the capital of Germany? ",
             "What is the capital of England? "]
# Associated good answers
answers = ["C",
           "A",
           "A",
           "D"]
# Associated options
options = [["A. Mons", "B. Bruges", "C. Brussels", "D. Liege"],
           ["A. Paris", "B. Bordeaux", "C. Lille", "D. Marseille"],
           ["A. Berlin", "B. Munich", "C. Hamburg", "D. Cologne"],
           ["A. Liverpool", "B. Manchester", "C. Oxford", "D. London"]]

score = 0
u_answers = []
for i in range(0, len(questions)):  # Loop for the length of the questions list
    print(f"\n{i+1}. {questions[i]}")
    for j in range(0, len(options[i])):  # Loop for the length of the options[i] list
        print("\t", options[i][j])
    u_answers.append(input("\nAnswer: "))
    u_answers[i] = u_answers[i].upper()
    if u_answers[i] == answers[i]:  # Compares user answer with good answers list
        print("Correct!")
        score += 1
    else:
        print("Wrong answer!")

print("\n---------- Review ----------")
print("Here are your answers:", u_answers, "\n")  # Display user's answers

for i in range(0, len(questions)):  # Loop for the length of the questions list
    print(f"Question {i+1}: {u_answers[i]}")
    if u_answers[i] != answers[i]:  # Compares user answer with good answers list
        print(f"The good answer was: {answers[i]}")

print(f"\nHere's your score: {score}/{len(questions)}")  # Displays the score


