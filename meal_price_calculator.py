#inputs
child_price = float(input("What is the price of a child's meal? :"))
adult_price = float(input("What is the price of an adult's meal? :"))
child_count = int(input("How many children are eating? :"))
adult_count = int(input("How many adults are eating? :"))
sales_tax = int(input("What is the  percentage rate of sales tax? :"))
tip = float(input("How much money are you tipping? :"))

#calculating subtotal
subtotal = child_price * child_count + adult_price * adult_count

#add tax
sub_add_tax = subtotal * (sales_tax / 100 +1)

#add tip
sub_with_tip = sub_add_tax + tip
print(f"Your total is ${sub_with_tip:.2f}.")

payment = float(input("How much are you going to pay? :"))
change = payment - sub_with_tip

print(f"Here's your change! ${change:.2f}")
if tip > 0:
    print("Thanks for tipping! We really appreciate it.")
