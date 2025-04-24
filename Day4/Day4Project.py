import random

rock_art = ("""
        _______
      ---' ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
        """)

scissors_art = ("""
        _______
      ---' ____)____
                ______)
             __________)
            (____)
     ---.__(___)
""")

paper_art = ("""
          _____
      ---' ____)____
                ______)
                _______)
             _______)
    ---.__________)
""")

ascii_arts = [rock_art, scissors_art, paper_art]
game = ["rock", "scissors", "paper"]

print("Welcome to the Rock, Paper, Scissors Game!\n만약 당신이 한번이라도 진다면 점수는 다 사라집니다.")

point = 0

for _ in range(100):
    user = input("What do you choose? Type 0 for rock, 1 for scissors, 2 for paper\n")

    if user not in ["0", "1", "2"]:
        print("잘못된 입력입니다. 0, 1, 2 중에서 선택하세요.")
        continue

    # 인덱스 값으로 변환
    user_idx = int(user)
    computer_idx = random.randint(0, 2)

    # 사용자, 컴퓨터의 가위바위보 결과물 출력
    print(f"\nYou chose:\n{ascii_arts[user_idx]}")  # ascii_arts에서 user_idx = 인덱스 값
    print(f"Computer chose:\n{ascii_arts[computer_idx]}")   # ascii_arts에서 computer_idx = 인덱스 값

    # 인덱싱 값이 같을시
    if user_idx == computer_idx:
        print("무승부!\n")
        continue
    if (user_idx - computer_idx) % 3 == 1:
        point += 1
        print(f"You Win!\n+1 POINT\n당신의 점수: {point} POINT!")
        answer = input("한판 더 하시겠습니까? (Y/N): ")
        # 한번 더 할지 사용자에게 물어봄 Y가 아닐시 게임 종료
        if answer.upper() != "Y":
            print(f"게임 종료!\n최종 점수: {point} POINT!")
            break
        else:
            continue
    else:
        point = 0
        print(f"You Lose....\n{point} POINT...\nbye..")
        print("게임이 종료됩니다.")
        break
