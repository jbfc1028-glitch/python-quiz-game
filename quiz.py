
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show_question(self):
        print(self.question)

        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def check_answer(self, user_answer):
        return self.answer == user_answer

if __name__ == "__main__":
    quiz = Quiz(
        "대한민국의 수도는?",
        ["서울", "부산", "대전", "인천"],
        1
    )

    quiz.show_question()
    print("정답 확인:", quiz.check_answer(1))