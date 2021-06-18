f_name = input("What is your first name?: ")
l_name = input("What is your last name?: ")
choice = input("Normal, or James Bond version? N/JB: ")


output1 = f"Your name is {f_name} {l_name}"
output2 = f"Your name is {l_name}, {f_name} {l_name}"
if choice.lower() == "n":
    print(output1)
elif choice.lower() == "jb": 
    print(output2)
else:
    print("Invalid Command")
