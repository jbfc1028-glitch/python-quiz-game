
from quiz import Quiz

def create_default_quizzes():
    quizzes = [
        Quiz(
            "대한민국의 수도는?",
            ["서울", "부산", "대전", "인천"],
            1
        ),
        Quiz(
            "일본의 수도는?",
            ["오사카", "교토", "도쿄", "후쿠오카"],
            3
        ),
        Quiz(
            "프랑스의 수도는?",
            ["마르세유", "파리", "리옹", "니스"],
            2
        ),
        Quiz(
            "호주의 수도는?",
            ["시드니", "멜버른", "브리즈번", "캔버라"],
            4
        ),
        Quiz(
            "캐나다의 수도는?",
            ["토론토", "밴쿠버", "오타와", "몬트리올"],
            3
        )
    ]

    return quizzes


if __name__ == "__main__":
    quizzes = create_default_quizzes()

    for quiz in quizzes:
        quiz.show_question()
        print("정답 번호:", quiz.answer)
        print()
