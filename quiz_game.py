
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
