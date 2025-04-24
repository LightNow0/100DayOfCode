# Randomisation(랜덤 모듈)
import random
# import my_module  모듈 사용 방법떄 사용

# 정수
# random_integer = random.randint(1, 10)
# print(random_integer)

# print(my_module.my_favourite_number)  모듈 사용 방법떄 사용

# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

# Heads or Tails 램덤으로 출력하는 연습
# 개인적으로 사용자가 입력한 내용과 random모듈로 생성하는 것과 동일했을때 성공하는 게임? 궁금해서 해봄...
# a = "Heads"
# b = "Tails"
#
# user = input("Heads or Tails")
#
# random_H_or_T = random.choice([a, b])
# if random_H_or_T == user:
#     print(f"computer choise {random_H_or_T} You Win!")
# else:
#     print(f"computer choise {random_H_or_T} You Lose!")

# 강의 속 정답
# random_H_or_T = random.randint(0, 1)
# if random_H_or_T == 0:
#     print("Heads")
# else:
#     print("Tails")

#단일 변수
# state1 = "서울"
# state2 = "인천"
# state3 = "수원"

# state_of_korea = ["서울", "인천", "수원", "대전", "부산"]


# seoul = ["대림", "논현", "신촌"]
# deajeon = ["관저", "갈마", "봉명"]
# busan = ["범일", "부암", "개금"]
#
# korea = [seoul, deajeon, busan, 1, 10, 300, True, False]
# # print(korea[0][2])
# # korea[3] = 12345
# korea.append(0)
# print(korea)

# friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
# print(len(friends))
# random.choice로 이름을 랜덤으로 출력하는 방법
# print(random.choice(friends))

# randint로 법위 설정후 이름 랜덤으로 출력하는 방법
# print(friends[random.randint(0, 4)])  // 1번
# random_index = random.randint(0, 4)   // 2번
# print(friends[random_index])

fruits = ["apple", "banana", "orange", "strawberry", "grape"]
vegetables = ["carrot", "cabbage", "cucumber", "tomato", "spinach"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)