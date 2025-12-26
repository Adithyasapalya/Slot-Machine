
MAX_LINES = 3

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

def get_no_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? : ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter an lines greater than zero.")
        else:
            print("Invalid input. Please enter a numeric value.")
    return lines


def main():
    balance = deposit()