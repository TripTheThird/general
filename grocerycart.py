#introductory things

print("Welcome to the Shopping Cart Program!")
in_cart = []
item_price = []
action = -1
while action != "6":
    print("Please select one of the following")
    print("1. Add item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Compute total")
    print("5. Check Out")
    print("6. Quit")
    
    #repeating input
    action = input("Please enter an action: ")
    
    #adds item and price to list
    if action == "1":
        add_cart = input("What item do you want to add? ")
        in_cart.append(add_cart)
        price_of_item = float(input("How much does this item cost? $"))
        item_price.append(price_of_item)
        print(f"{add_cart} has been added to the cart.")
  
    #shows you list of items
    elif action == "2":
        for i in range(len(in_cart)):
            cart = in_cart[i]
            price = item_price[i]

            print(f"{cart} - ${price:.2f}")

    #gives you list of items and option for removal
    elif action == "3":
        for i in range(len(in_cart)):
            cart = in_cart[i]
            price = item_price[i]

            print(f"[{i + 1}] {cart} - ${price:.2f}")
        remove = int(input("Which item do you want to remove? "))
        in_cart.pop(remove - 1)
        item_price.pop(remove - 1)
    
    #gives you sum of cart
    elif action == "4":
        total = sum(item_price)
        print(f"Your total is ${total:.2f}")

    elif action == "5":
        payment = -1
        total = 0
        while payment < total:
            total = sum(item_price)
            print(f"Your total is ${total:.2f}")
            payment = float(input("How much are you paying? $"))
            if payment < total:
                print("You need to pay equal or more than the total.")
            else:
                print("Here's your change!")
                print(f"${payment - total:.2f}")
            
    #closes program
    elif action == "6":
        print("Thank you, have a nice day.")
   
    #backup error message
    else:
        print("Oops, try again.")

        


