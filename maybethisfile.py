num_product = int(input("How many products did you sell? :"))
product_price = float(input("What is the price of the product? :"))

commission_percent = float(input("What is your commission? :"))

commission_percent = commission_percent / 100
total_sale = num_product * product_price

commission_amount = total_sale * commission_percent

print(f"The total sales amount is ${total_sale:.2f}")
print(f"You made : ${commission_amount:.2f}")

if total_sale > 500:
    print("You received a bonus!")

print("Thank you for using this wonderful program...")