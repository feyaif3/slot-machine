import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "🍎": 5,
    "🍌": 4,
    "🍐": 3,
    "🍑": 2,
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count): # underscore is annoymous value.
            all_symbols.append(symbol)
            
    columns = [] # column list
    for _ in range(cols): #generate column for every column we have
        column = []
        current_symbols = all_symbols [:] #current symbols is equal to a copy of all symbols available
        for _ in range (rows):
            value = random.choice(current_symbols) #picking a random choice of the current values
            current_symbols.remove(value) #removing the chosen value from the symbols list 
            column.append(value) #adding the picked value in the column list 
            
        columns.append(column)
        
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for column in columns:
    
            
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
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"Your balance is too low to bet, please deposit more. Your current balance is: £{balance} ")
        else:
            break
        
    print(f"You are betting ${bet} on {lines}. Total bet is equal to: ${total_bet}")

main()