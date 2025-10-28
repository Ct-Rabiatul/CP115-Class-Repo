grade = float(input())
valid_count = 0
total_grade = 0
# TODO: Your code here
while grade > 0:
    if grade < 0 and grade > 100:
        continue
    valid_count += 1
    total_grade += grade
    grade = float(input())
if valid_count == 0 :
    average = 0
else:
    average = total_grade / valid_count

print(valid_count)
print(f"{average:.2f}")
