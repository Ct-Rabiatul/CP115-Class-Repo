age = int(input())
accident_count = int(input())
base_premium = 0
penalty = 0
discount_amount = 0
# Your code here
if age < 25 :
    base_premium = 2400
elif age >= 25 and age <= 50 :
    base_premium = 1800
elif age > 50 :
    base_premium = 2000

if accident_count == 0 :
    penalty = 0
    discount_amount = 0.9
elif accident_count == 1 or accident_count == 2 :
    penalty = 300
    discount_amount = 0
elif accident_count >= 3 :
    penalty = 600
    discount_amount = 0

final_premium = (base_premium * discount_amount) + penalty


print(base_premium)
print(final_premium)
print(discount_amount)