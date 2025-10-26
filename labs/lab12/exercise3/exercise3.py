age_input = input()

total_age = 0
age_count = 0

# TODO: Your code here
while age_input != "done" :
    total_age += int(age_input)
    age_count += 1
    age_input = input()

if age_count > 0:
    average_age = total_age / age_count
else:
    average_age = 0

print(age_count)
print(total_age)
print(f"{average_age:.2f}")
