# For loop approach
total = 0
for i in range(1, 6):
    total += i
print(f"For loop total: {total}")\

# While loop approach
total = 0
current = 1
while current <= 5:
    total += current
    current += 1  # Manual update
print(f"While loop total: {total}")