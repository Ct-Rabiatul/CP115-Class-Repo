main_course = input()
drink = input()
dessert = input()
customer_age = int(input())

main_price = 0
drink_price = 0
dessert_price = 0

# TODO: Your code here
if main_course == "Chicken" :
    main_price = 10
elif main_course == "Beef" :
    main_price = 12
elif main_course == "Fish" :
    main_price = 11

if drink == "Soft Drink" :
    drink_price = 2
elif drink == "Coffee" :
    drink_price = 3

if dessert == "Ice Cream" :
    dessert_price = 4
elif dessert == "Cake" :
    dessert_price = 5

food_cost = main_price + drink_price + dessert_price

#Addittional Charges 

#Service charge 10%
final_bill = food_cost * 1.10

#Senior Citizen and Student Discount
if customer_age > 60 :
    final_bill *= 0.85
elif customer_age < 18 :
    final_bill *= 0.9

print(f"{final_bill:.2f}")