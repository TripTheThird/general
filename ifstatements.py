first_num = float(input("What is the first number? :"))
second_num = float(input("What is the second number? :"))

if first_num > second_num:
    print("The first number is greater.")
elif first_num <= second_num:
    print("The first number is not greater.")
else:
    print("ERROR")

if first_num == second_num:
    print("The numbers are equal.")
elif first_num != second_num:
    print("The numbers are not equal.")
else:
    print("ERROR")

if first_num < second_num:
    print("The second number is greater.")
elif first_num >= second_num:
    print("The second number is not greater.")
else:
    print("ERROR")

animal = input("What is your favorite animal? :")

if animal.lower() == "monkey":
    print("That's my favorite animal too!")
else:
    print("Your animal is more lame than mine, loser.")
    