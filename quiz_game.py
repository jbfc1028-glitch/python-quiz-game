import json
from pathlib import Path
from quiz import Quiz
class QuizGame:
    def __init__(self, quizzes, best_score=0):
        self.quizzes = quizzes
        self.best_score = best_score

    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            return True

        return False

    def show_best_score(self):
        print(f"현재 최고 점수는 {self.best_score}점 / 100점입니다.")

    
    def save_state(self):
        data = {
            "best_score": self.best_score,
            "quizzes": []
        }

        for quiz in self.quizzes:
            data["quizzes"].append({
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer
            })

        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("게임 데이터가 저장되었습니다.")

        except (OSError, TypeError, ValueError) as error:
            print(f"게임 데이터 저장 중 오류가 발생했습니다: {error}")


    def load_state(self):
        if not Path("state.json").exists():
            print("저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
            return

        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            best_score = data["best_score"]
            saved_quizzes = []

            for item in data["quizzes"]:
                saved_quizzes.append(
                    Quiz(item["question"], item["choices"], item["answer"])
                )

            self.best_score = best_score
            self.quizzes[:] = saved_quizzes

            print("저장된 게임 데이터를 불러왔습니다.")

        except (OSError, ValueError, KeyError, TypeError):
            print("저장 파일에 문제가 있어 기본 퀴즈로 시작합니다.")
