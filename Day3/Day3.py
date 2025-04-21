# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height > 120:
#     print(f"You can ride the rollercoaster!")
#
# else:
#     print(f"Sorry, you are too young to ride the rollercoaster")


# Even Number 10 % 3
# 나머지를 깔끔하게 0으로 만드는 방법

# number_to_check = int(input("What is the number your to check? "))
# if number_to_check % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


## 중첩 if, elif
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height > 120:
#     print(f"You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("Please Pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
#
# else:
#     print(f"Sorry, you are too young to ride the rollercoaster")


## 단일 if문 사용
# print("놀이공원에 어서오세요")
# height, age = map(int, input("키와 나이가 어떻게 되시나요(cm)? ").split())
# price = 0
# photo_price = 5000
# if age >= 20:
#     price = 200000
#     print(f"성인은 무조건 {price}원입니다. (촬영비용 포함)")
#
# if age < 20:
#     price = 30000
#     print(f"청소년 요금입니다. 가격은 {price}원입니다.")
#
#     if height < 150:
#         print(f"키{height}는 150cm 미만이라 롤러코스터는 탑승 불가능합니다.")
#         if height < 148:
#             print(f"이번만 입장 시켜드릴게요")
#     if height < 100:
#         print(f"키{height}는 100cm 미만이라 범퍼카 이하만 탑승 가능합니다.")
#
#     want_photo = input("놀이기구별 사진 촬영을 원하시나요? Y or n")
#     if want_photo == "y":
#         total = price + photo_price
#         print(f"입장권 + 촬영비용 총 {total}원입니다.")
#     else:
#         total = price
#
# if age <= 9:
#     price = 23000
#     print(f"어린이 요금입니다. 가격은 {price}원입니다.")
#
#     if height < 150:
#         print(f"키{height}는 150cm 미만이라 롤러코스터는 탑승 불가능합니다.")
#         if height < 148:
#             print(f"이번만 입장 시켜드릴게요")
#     if height < 100:
#         print(f"키{height}는 100cm 미만이라 범퍼카 이하만 탑승 가능합니다.")
#
#     want_photo = input("놀이기구별 사진 촬영을 원하시나요? Y or n")
#     if want_photo == "y":
#         total = price + photo_price
#         print(f"입장권 + 촬영비용 총 {total}원입니다.")
#     else:
#         total = price
#
# else:
#     print("아동 무료입장 입니다")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print(f"You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please Pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    # elif age >= 45 and age <= 55:
    #     print("Everything is going to be ok. Have a free ride on us!")
    elif 45 <= age <= 55:   # 위 방법으로 해도 101줄로 해도 무방함
        print("Everything is going to be ok. Have a free ride on us!")

    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("Do you want photo? Y or N: ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is: {bill}")

else:
    print(f"Sorry, you are too young to ride the rollercoaster")