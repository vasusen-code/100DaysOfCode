class Quiz:
    def __init__(self, q_list: list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def ask_question(self):
        question = self.question_list[self.question_number]["question"]
        self.question_number += 1
        string = f"Q{self.question_number}. {question}\nTrue/False  : "
        answer = input(string).lower()
        return answer
    
    def check_questions_left(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, answer):
        if answer == self.question_list[self.question_number - 1]["answer"]:
            self.score += 1
            print("Correct answer.")
            print(f"Your current score is: {quiz.score}/{self.question_number}")
        else:
            print("Incorrect answer.")
            print(f"Your current score is: {quiz.score}/{self.question_number}")
        
question_bank = [
    {"question": "Delhi is capital of india", "answer": "true"},
    {"question": "mysore is capital of goa", "answer": "false"},
    {"question": "Narendra modi is PMOI", "answer": "true"},
    {"question": "HIV is retro virus", "answer": "true"},
    {"question": "Human heart is 3 chambered", "answer": "false"}]

quiz = Quiz(question_bank)
questions_left = True

def ask_question(quiz):
    def invalid_answer():
        answer = input("Invalid entry, try again\nTrue/False: ").lower()
        if answer != "true" and answer != "false":
            return invalid_answer()
        else:
            return answer
    answer = quiz.ask_question()
    if answer != "true" and answer != "false":
        answer = invalid_answer()
    return answer

while questions_left:
    answer = ask_question(quiz)
    quiz.check_answer(answer)
    print("\n")
    questions_left = quiz.check_questions_left()

print("Quiz over")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")
        
        
