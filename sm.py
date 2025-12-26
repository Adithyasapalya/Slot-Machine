
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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
                print("Enter valid number of lines.")
        else:
            print("Invalid input. Please enter a numeric value.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $ : ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Invalid input. Please enter a numeric value.")
    return amount


def main():
    balance = deposit()
    lines = get_no_of_lines() 
    bet = get_bet()
    print(balance, lines, bet)

main()