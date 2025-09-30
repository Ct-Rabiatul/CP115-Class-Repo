position = input()
overtime_hours = int(input())
is_weekend = input()
hourly_rate = 0
# Your code here
if position == "Manager" :
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25
elif position == "Staff":
    hourly_rate = 18

overtime_pay = 0
if is_weekend == "Yes":
    overtime_pay = (1.5 * hourly_rate * overtime_hours) + (overtime_hours * 5)
else:
    overtime_pay = 1.5 * hourly_rate * overtime_hours

total_pay = overtime_pay


print(hourly_rate)
print(overtime_pay)
print(total_pay)