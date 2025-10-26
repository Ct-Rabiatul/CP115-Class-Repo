sale_amount = int(input("Enter sale amount (0 to stop): "))
num_of_transaction = 0
total_sale = 0
average = 0

while sale_amount != 0 :
    num_of_transaction += 1
    total_sale += sale_amount
    sale_amount = int(input("Enter sale amount (0 to stop): "))

if num_of_transaction > 0 :
    average = total_sale / num_of_transaction
else:
    average = 0

print(f"Total sales : RM {total_sale:.1f}")
print(f"Number of transactions : {num_of_transaction}")
print(f"Average sale : RM {average}")