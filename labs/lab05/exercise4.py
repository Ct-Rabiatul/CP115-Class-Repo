item_name = input("Enter item name: ")
item_price = float(input("Enter price of item: "))

quantity = 3
tax_rate = 0.06

subtotal = item_price * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount

print("Subtotal: " + float(subtotal))
print("Tax Amount: " + float(tax_amount))
print("Total Cost: " + float(total_cost)) 

