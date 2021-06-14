def tips(amount,bill,prompt):
    tip = 0
    if prompt == "Y":
        tip += amount * 0.2
        change = amount - (bill + tip)
    else:
        change = amount - bill
    print("The tip amount is: R",tip)
    return change

amount = int(input("Enter the money given by the customer: "))
bill = int(input("Enter bill amount: "))
prompt = input("Do you want to tip the waiter? (Y/N): ").upper()

print("The change is: R",tips(amount,bill,prompt))
