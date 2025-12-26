
def deposit():
    while True:
        amount = input("What would you like to deposit? $ : ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter an amount greater than zero.")
        else:
            print("Invalid input. Please enter a numeric value.")
    return amount