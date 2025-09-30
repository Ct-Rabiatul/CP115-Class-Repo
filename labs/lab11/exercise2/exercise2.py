num_days = int(input())
danger_threshold = float(input())
danger_days = 0
# TODO: Your code here
# Use input() inside the loop to get each day's temperature
for num_days in range (1, num_days) :
    temp = float(input())

    if temp > danger_threshold:
        danger_days += 1

    temp += temp
    average_temp = temp / num_days


print(danger_days)
print(f"{average_temp:.1f}")