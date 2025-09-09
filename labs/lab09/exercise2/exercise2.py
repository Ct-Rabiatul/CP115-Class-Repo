employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here
if  tax_status == "single" :
    if base_salary >= 5000 :
        tax_rate = 0.22
    else :
        tax_rate = 0.18
elif tax_status == "married" :
    if base_salary >= 6000 :
        tax_rate = 0.20
    else :
        tax_rate = 0.15
else :
    tax_status == "head"
    if base_salary >= 5500 :
        tax_rate = 0.25
    else :
        tax_rate = 0.19

#Tax Deductions
tax_amount = base_salary * tax_rate

#After Tax Deductions
after_tax = base_salary + tax_amount

#Additional Deductions
epf = base_salary * 0.11 * 0.005

total_deduction = tax_amount + epf

net_salary = base_salary - total_deduction

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")