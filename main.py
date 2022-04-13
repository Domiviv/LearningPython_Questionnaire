class Question:
    def __init__(self, label, answer, option):
        self.label = label
        self.answer = answer
        self.option = option

    def ask(self):
        print(self.label)
        for i in range(len(self.option)):
            print("\t", self.option[i])

        print()
        result = False
        response = Question.ask_response(1, len(self.option))
        if self.option[response-1].lower() == self.answer.lower():
            print("Correct!")
            result = True
        else:
            print("Wrong answer!")

        return result

    def ask_response(min, max):
        response_str = input(f"\nAnswer (between {min} & {max}): ")
        try:
            response = int(response_str)
            if min <= response <= max:
                return response

            print(f"Please enter a number between {min} & {max})")
        except:
            print("Only numbers are allowed")
        return Question.ask_response(min, max)

class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def exec(self):
        print("\n---------- Review ----------")
        score = 0
        for question in self.questions:  # Loop for the length of the questions list
            if question.ask():  # Compares user answer with good answers list
                score += 1

        print(f"\nHere's your score: {score}/{len(self.questions)}")
        return score


Questionnaire(
    (
        Question("What is the capital of Belgium? ", "Brussels", ("Mons", "Bruges", "Brussels", "Liege")),
        Question("What is the capital of France? ", "Paris", ("Paris", "Bordeaux", "Lille", "Marseille")),
        Question("What is the capital of Germany? ", "Berlin", ("Berlin", "Munich", "Hamburg", "Cologne")),
        Question("What is the capital of England? ", "London", ("Liverpool", "Manchester", "Oxford", "London"))
    )
).exec()
