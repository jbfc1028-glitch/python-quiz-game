
from quiz_game import QuizGame
from quiz_data import create_default_quizzes


def add_quiz(quizzes):
    print("\n===== 퀴즈 추가 =====")

    question = input("문제를 입력하세요: ").strip()

    if not question:
        print("문제는 비워둘 수 없습니다.")
        return

    choices = []

    for i in range(4):
        choice = input(f"{i + 1}번 보기를 입력하세요: ").strip()

        if not choice:
            print("보기는 비워둘 수 없습니다.")
            return

        choices.append(choice)

    while True:
        try:
            answer = int(input("정답 번호 (1~4): ").strip())

            if 1 <= answer <= 4:
                break

            print("1~4 사이의 번호를 입력해주세요.")

        except ValueError:
            print("숫자를 입력해주세요.")

    new_quiz = Quiz(question, choices, answer)
    quizzes.append(new_quiz)

    print("퀴즈가 추가되었습니다!")

def show_quiz_list(quizzes):
    print("\n===== 퀴즈 목록 =====")

    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return

    for i, quiz in enumerate(quizzes, start=1):
        print(f"{i}. {quiz.question}")

    print(f"\n총 {len(quizzes)}개의 퀴즈가 등록되어 있습니다.")


def play_quiz(game):
    quizzes = game.quizzes
    score = 0

    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return

    for quiz in quizzes:
        print("\n--------------------")
        quiz.show_question()

        while True:
            try:
                answer = input("정답 번호 (1~4): ").strip()

                if answer == "":
                    print("정답 번호를 입력해주세요.")
                    continue

                answer = int(answer)

                if answer < 1 or answer > 4:
                    print("1~4 사이의 번호를 입력해주세요.")
                    continue

                break

            except ValueError:
                print("숫자를 입력해주세요.")

        if quiz.check_answer(answer):
            print("정답입니다!")
            score += 1
        else:
            print(f"오답입니다! 정답은 {quiz.answer}번입니다.")

    print("\n===== 퀴즈 결과 =====")
    print(f"총 {len(quizzes)}문제 중 {score}문제 정답!")

    final_score = round(score / len(quizzes) * 100) if quizzes else 0

    print(f"이번 점수: {final_score}점 / 100점")

    if game.update_best_score(final_score):
        print("새로운 최고 점수 달성!")

    game.show_best_score()


quizzes = create_default_quizzes()
game = QuizGame(quizzes)


while True:
    print("\n===== 나라별 수도 퀴즈 게임 =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 최고 점수 확인")
    print("5. 종료")

    try:
        choice = input("메뉴 번호를 선택하세요: ").strip()

        if choice == "":
            print("번호를 입력해주세요.")
            continue

        choice = int(choice)

        if choice == 1:
            play_quiz(game)

        elif choice == 2:
            add_quiz(quizzes)

        elif choice == 3:
            show_quiz_list(quizzes)

        elif choice == 4:
            game.show_best_score()

        elif choice == 5:
            print("게임을 종료합니다.")
            break

        else:
            print("1~5 사이의 번호를 입력해주세요.")

    except ValueError:
        print("숫자를 입력해주세요.")

    except (KeyboardInterrupt, EOFError):
        print("\n게임을 안전하게 종료합니다.")
        break
