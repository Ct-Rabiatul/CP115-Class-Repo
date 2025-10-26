score_input = input()

passing_count = 0
failing_count = 0

# TODO: Your code here
while score_input != "end" :
    score = int(score_input)
    if score >= 60 :
        passing_count += 1
    else:
        failing_count += 1
    score_input = input()

if passing_count > 0 :
    pass_rate = (passing_count / (passing_count + failing_count)) * 100
else:
    pass_rate = 0



print(passing_count)
print(failing_count)
print(f"{pass_rate:.2f}")
