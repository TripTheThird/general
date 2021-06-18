import math

items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

calc = math.ceil(items / items_per_box)

print(f"You will need {calc} boxes.")