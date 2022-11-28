
def deposit();
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

deposit()