#SITI RABIATUL ADAWIAH BINTI HUSSAIN

monthly_usage = float(input())
discount = 0

#Determine discount
if monthly_usage < 50 :
    discount = 0
elif monthly_usage <= 100 :
    discount = 0.05
elif monthly_usage > 100 :
    discount = 0.2

#Calculate total discount
discount *= monthly_usage

#Calculate total amount of the bill to be paid after discount
amount_of_bill = monthly_usage - discount

print(f"Amount of the bill : RM{amount_of_bill:.2f}")