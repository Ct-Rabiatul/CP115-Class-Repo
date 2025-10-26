target_points = int(input())
points = int(input())
total_points = 0

# TODO: Your code here
# Use input() inside the while loop to get points each round
while target_points != 100 :
    points = int(input())
    total_points += points
    rounds_played += 1

print(total_points)
print(rounds_played)