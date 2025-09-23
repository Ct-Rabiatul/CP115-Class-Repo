applicant_age = int(input())
vision_test = input()
written_score = int(input())
driving_score = int(input())
medical_clearance = input()

requirements_met = 0

# TODO: Your code here
if vision_test == "Pass" :
    requirements_met += 1

if written_score >= 80 :
    requirements_met += 1

if driving_score >= 85 :
    requirements_met += 1

if medical_clearance == "Pass" :
    requirements_met += 1



if requirements_met == 4 and applicant_age >= 21 :
    license = "Class A (Commercial)"
elif requirements_met == 3 and applicant_age >= 18 :
    license = "Class B (Regular)"
elif requirements_met == 2 or requirements_met == 3 :
    license = "Restricted License"
elif requirements_met < 2 :
    license = "Application Denied"

license_class = license
print(license_class)