MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

def deposit():
    while True:
        amount = input("How much would you like to deposit? £")
        if amount.isdigit(): # checks if the input is a valid number
            amount = int(amount) # Turns the last line into int
            if amount > 0: # the minimum amount to add is 1
                break
            else:
                print("Deposit amount must be greater than 0.")
        else: 
             print("Please enter a number.")
    
    return amount

def get_number_of_lines():
    while True:
        lines= input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: #checks if lines is equal or greater than 1 and less than or equal to the max lines
                break
            else:
                print("Enter a valid number of lines")
        else: 
             print("Please enter a number.")
    
    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? £")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()

main()