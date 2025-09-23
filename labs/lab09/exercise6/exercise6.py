position = input()
overtime_hours = int(input())
is_weekend = input()

base_hourly = 0
# TODO: Your code here
if position == "Manager" :
    base_hourly = 30
elif position == "Supervisor" :
    base_hourly = 20
elif position == "Staff" :
    base_hourly = 15
elif position == "Intern" :
    base_hourly = 8


#Overtime Rules
if overtime_hours <= 8 :
    overtime_pay = 1.5 * overtime_hours * base_hourly
elif overtime_hours > 8 :
    overtime_pay = ((overtime_hours - 8) * 2.0 * base_hourly) + (8 * 1.5 * base_hourly)
bonus = 0
if is_weekend == "Yes" :
    bonus = overtime_hours * 5

overtime_pay += bonus

print(overtime_pay)