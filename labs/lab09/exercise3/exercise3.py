day_type = input()
show_time = int(input())
customer_type = input()
is_student = input()

base_price = 0
# TODO your code here
if day_type == "Weekend" and customer_type == "Adult" :
    base_price = 18
elif day_type == "Weekend" and customer_type == "Child" :
    base_price = 12
elif day_type == "Weekend" and customer_type == "Senior" :
    base_price = 15
elif day_type == "Weekday" and customer_type == "Adult" :
    base_price = 15
elif day_type == "Weekday" and customer_type == "Child" :
    base_price = 10
elif day_type == "Weekday" and customer_type == "Senior" :
    base_price = 12

final_price = base_price

if show_time > 18 :
    final_price += 3


if day_type == "Weekday" and is_student == "Yes" :
    final_price *= 0.9 #10% discount

print(base_price)
print(final_price)