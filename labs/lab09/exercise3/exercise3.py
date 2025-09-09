day_type = input()
show_time = int(input())
customer_type = input()
is_student = input()

# TODO your code here
if day_type == "Weekends" and customer_type == "Adult" :
    base_price = 18
elif day_type == "Weekends" and customer_type == "Child" :
    base_price = 12
elif day_type == "Weekends" and customer_type == "Senior" :
    base_price = 15
elif day_type == "Weekdays" and customer_type == "Adult" :
    base_price = 15
elif day_type == "Weekdays" and customer_type == "Child" :
    base_price = 10
else :
    base_price = 12


print(base_price)
print(final_price)