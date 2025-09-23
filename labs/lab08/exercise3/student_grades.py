test = 5
score1 = 78
score2 = 85
score3 = 92
score4 = 67
score5 = 88
full_mark = 100
full_mark_test = 500

total_point = score1 + score2 + score3 + score4 + score5
average_score = total_point / full_mark_test
grade1 = (score1 / full_mark_test) * 100
grade2 = (score2 / full_mark_test) * 100
grade3 = (score3 / full_mark_test) * 100
grade4 = (score4 / full_mark_test) * 100
grade5 = (score5 / full_mark_test) * 100

print(f"Score 1: {score1} \nScore 2: {score2} \nScore 3: {score3} \nScore 4: {score4} \nScore 5: {score5}")
print(f"Total point : {total_point}")
print(f"Student average : {average_score}")
print(f"Percentage Each Test: \n{grade1}% \n{grade2}% \n{grade3}% \n{grade4}% \n{grade5:.2f}%")
