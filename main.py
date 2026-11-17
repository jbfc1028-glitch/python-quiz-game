
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
            print("퀴즈 풀기를 선택했습니다.")

        elif choice == 2:
            print("퀴즈 추가를 선택했습니다.")

        elif choice == 3:
            print("퀴즈 목록을 선택했습니다.")

        elif choice == 4:
            print("최고 점수 확인을 선택했습니다.")

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
