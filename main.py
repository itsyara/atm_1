#creation of a ATM machine
#create function main menu


balance = 1000
choice = ""

def main_menu():
    print("Hello, welcome to our bank.")
    print("Please choose from the following options:")
    print("1. See Balance")
    print("2. Withdraw")
    print("3. Exit")
    

def see_balance():
    print(f"Your balance is {balance}")
    print("Would you like to select another service?")
    print("1. Main Menu")
    print("2. Exit")
    

def withdraw_cash():
    print("How much would you like to withdraw?")
    
while True:
    main_menu()
    choice = input()
    if choice == "1":
        see_balance()
        choice = input()
        if choice == "1":
            continue
        elif choice == "2":
            break
        else:
            print("invalid input")
    elif choice == "2":
        withdraw_cash()
        choice = int(input())
        if choice < balance:
            print(f"you have withdrawn {choice} , your new balance is {balance - choice}")
            balance = balance - choice
            print("would you like to continue?")
            if choice == "1":
              continue
        elif choice == "2":
            break
        else:
            print("invalid input")
    elif choice == "3":
        break
    else:
        print("Invaid input")
        continue

