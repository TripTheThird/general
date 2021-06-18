#inputs
print("Rate the following 1-10.")

loan_size = int(input("\nHow large is the loan? :"))
c_history = int(input("How good is your credit history? :"))
income = int(input("How high is your income? :"))
d_payment = int(input("How large is your down payment? :"))

#rules
loan = False

if loan_size >= 5:
    if c_history >= 7 and income >= 7:
        loan = True
    elif c_history >= 7 or income >= 7:
        if d_payment >= 5:
            loan = True
    else:
        loan = False
else: 
    if c_history < 4:
        loan = False
    else:
        if income >= 7 or d_payment >= 7:
            loan = True
        elif income >= 4 and d_payment >= 4:
            loan = True
        else:
            loan = False

if loan == True:
    print("Loan approved.")
else:
    print("Loan denied.")