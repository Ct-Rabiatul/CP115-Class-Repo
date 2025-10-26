age = int(input("Enter you age: "))
ticket_price = float(input("Enter your ticket price: RM "))
discount = 0
category = ""

#Checking whether age and ticket are positive values or not.
while age < 0 or ticket_price < 0 :
    print("Error : Age and ticket price must be non-negative values.")
    age = int(input("Enter you age: "))
    ticket_price = float(input("Enter your ticket price: RM "))

if age <= 12 :
    discount = 0.5
    category = "Children"
elif age >= 13 and age <= 17 :
    discount = 0.25
    category = "Teenagers"
elif age >= 18 :
    discount = 0
    category = "Adults"

#Calculate ticket price after discount
final_price = ticket_price - (ticket_price * discount)

#To change discount in float to integer (0.50 to 50)
discount_percentage = discount * 100

print(f"Category : {category}")
print(f"Discount : {discount_percentage:.1f}%")
print(f"The Discounted Price : RM {final_price:.2f}")