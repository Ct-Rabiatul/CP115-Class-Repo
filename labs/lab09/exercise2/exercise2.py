employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here
if  tax_status == "Single" and base_salary >= 5000 :
    tax_rate = 0.22
elif tax_status == "Single" and base_salary <= 5000 :
    tax_rate = 0.18
elif tax_status == "Married" and base_salary >= 6000 :
    tax_rate = 0.20
elif tax_status == "Married" and base_salary >= 6000 :
    tax_rate = 0.15
elif tax_status == "Head" and base_salary >= 5500 :
    tax_rate = 0.25
else :
    tax_rate = 0.19

#Overtime pay
overtime_pay = overtime_hours * 35

total_salary = base_salary + overtime_pay

#Tax Deductions
tax_amount = total_salary * tax_rate

#After Tax Deductions
after_tax = total_salary - tax_amount

#Additional Deductions
epf = after_tax * 0.11
socso = after_tax * 0.005

total_deduction = tax_amount + epf + socso

net_salary = total_salary - total_deduction

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")