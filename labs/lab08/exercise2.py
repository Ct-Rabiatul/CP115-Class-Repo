group_member = 6
dish1 = 25
dish2 = 12
dish3 = 8
service_tax = 1.10
delivery_fee = 5

total_dish = (25 * 3) + (12 * 2) + (8 * 4)
total = (total_dish * service_tax) +  delivery_fee
amount_each_person = total // 6

print(f"(The amount each person : {amount_each_person})")