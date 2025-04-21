# Python Pizza
'''
Write a Pizza Delivery Program
'''
'''
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
print(f"Your final bill is: ${bill}.")
todo: work out how much they need to pay based on their size choice.
(선택한 사이즈에 따라 얼마를 지불해야 하는지 계산하세요)

todo: work out how much to add to their bill based on their pepperoni choice.
(선택한 페퍼로니에 따라 얼마를 추가해야 하는지 계산하세요)

todo: work out their final amount on whether if they want extra cheese.
(치즈 추가 여부에 대한 최종  금액을 계산하세요)

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Add pepperoni for small Pizza (Y or N): +$2
(작은 피자에 페퍼로니 추가)
Add pepperoni for medium or large Pizza (Y or N): +$3
(M, L size의 피자에 페퍼로니 추가)
Add extra cheese for any size pizza (Y or N): +$1
(모든 사이즈에 치즈 추가)
'''

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# bill = 0
# # print(f"Your final bill is: ${bill}.")
#
# small_pepperoni = 2
# another_size = 3
# cheese = 1
#
# '''
# 기본 = bill
# 하나추가 = price
# 다추가 = total_price
# '''
#
# if size == "S":
#     bill = 15
#     if pepperoni == "Y":
#         price = bill + small_pepperoni
#         print(f"Your final bill is: ${price}.")
#         if extra_cheese == "Y":
#             total_price = price + cheese
#             print(f"Your final bill is: ${total_price}.")
#         else:
#             print(f"Your final bill is: ${price}.")
#     if extra_cheese == "Y":
#         price = bill + cheese
#         print(f"Your final bill is: ${price}.")
#     if extra_cheese == "N":
#         print(f"Your final bill is: ${bill}.")
#     else:
#         print(f"Your final bill is: ${bill}.")
#
# if size == "M":
#     bill = 20
#     if pepperoni == "Y":
#         price = bill + another_size
#         print(f"Your final bill is: ${price}.")
#         if extra_cheese == "Y":
#             total_price = price + cheese
#             print(f"Your final bill is: ${total_price}.")
#         else:
#             print(f"Your final bill is: ${price}.")
#     if extra_cheese == "Y":
#         price = bill + cheese
#         print(f"Your final bill is: ${price}.")
#     if extra_cheese == "N":
#         print(f"Your final bill is: ${bill}.")
#     else:
#         print(f"Your final bill is: ${bill}.")
#
# if size == "L":
#     bill = 25
#     if pepperoni == "Y":
#         price = bill + another_size
#         print(f"Your final bill is: ${price}.")
#         if extra_cheese == "Y":
#             total_price = price + cheese
#             print(f"Your final bill is: ${total_price}.")
#         else:
#             print(f"Your final bill is: ${price}.")
#     if extra_cheese == "Y":
#         price = bill + cheese
#         print(f"Your final bill is: ${price}.")
#     if extra_cheese == "N":
#         print(f"Your final bill is: ${bill}.")
#     else:
#         print(f"Your final bill is: ${bill}.")
# //결과 중복 출력이됨 + 코드의 길이가 길어짐

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")