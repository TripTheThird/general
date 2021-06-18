import math
from datetime import datetime
current_date = datetime.now().date()
width = (float(input("Enter the width of the tire in mm (ex 205): ")))
aspect_ratio = (float(input("Enter the width of the tired (ex 60): ")))
diameter = (float(input("Enter the diameter of the wheel in inches (ex 15): ")))


#formula
approximate_volume = math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000

with open("volumes.txt.", "at") as volumes:
    print(f"Date: {current_date} | Width, Aspect Ratio, Diameter: {width}, {aspect_ratio}, {diameter} | Volume: Volume of tire: {approximate_volume:.2f}", file=volumes)

#print statement
print(f"Date: {current_date} | Width, Aspect Ratio, Diameter: {width}, {aspect_ratio}, {diameter} | Volume: Volume of tire: {approximate_volume:.2f}")

potential_buy = input("Would you like to buy these tires? (Y/N): ")

if potential_buy.lower() == "y" or "yes":
    phone = input("What is your phone number? (xxx-xxx-xxxx): ")
    with open("volumes.txt.", "at") as volumes:
        print(f"Phone number of client: {phone}", file=volumes)