import math

choose = input("Determine group size or number of groups? GS/NG: ")

if choose.lower() == "gs":

    students = int(input("How many students are in the class? :"))
    groups = int(input("How many groups do you want?: "))

    print(f"You will have {math.floor(students / groups)} students in every group")
    print(f"You will have {students % groups} students without a group")

elif choose.lower() == "ng":

    students = int(input("How many students are in the class? :"))
    group_size = int(input("What is the group size? :"))
    num_groups = students / group_size
    full_groups = students // group_size
    leftover_students = students % group_size
    print(f"There are {num_groups} groups")
    print(f"There are {full_groups} full groups")
    print(f"There are {leftover_students} students left over.")

else:

    print("Invalid command, try again.")