# 팁 계산하기

print("Welcome to the tip calculator!")

total_price = float(input("What was the total bill? $"))
tip_percent = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_rate = tip_percent / 100
total_with_tip = total_price * (1 + tip_rate)
amount_per_person = total_with_tip / people

final_amount = round(amount_per_person, 2)
print(f"Each person should pay: ${final_amount:.2f}")


'''
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_rate = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount:.2f}")
'''