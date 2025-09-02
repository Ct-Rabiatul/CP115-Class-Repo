test = 5
grade1 = 78
grade2 = 85
grade3 = 92
grade4 = 67
grade5 = 88
full_mark = 100
full_mark_test = 500

total_point = grade1 + grade2 + grade3 + grade4 + grade5
average_score = total_point / full_mark_test
grade2 = (grade2 / full_mark_test) * 100
grade2 = (grade2 / full_mark_test) * 100
grade3 = (grade3 / full_mark_test) * 100
grade4 = (grade4 / full_mark_test) * 100
grade5 = (grade5 / full_mark_test) * 100

print(f"Score 1: {grade1} \nScore 2: {grade2} \nScore 3: {grade3} \nScore 4: {grade4} \nScore 5: {grade5}")
print(f"Total point : {total_point}")
print(f"Student average : {average_score}")
print(f"{grade1}% \n{grade2}% \n{grade3} \n{grade4}% \n{grade5}")
