PIN = "4023"
balance = 10000
statement = []
print("===== Welcome to ATM =====")
for attempt in range(3):
    entered_pin = input("Enter your PIN: ")
    if entered_pin == PIN:
        print("Login Successful")
        break
    else:
        print("Incorrect PIN")
else:
    print("Too many incorrect attempts. Card Blocked.")
    exit()
def show_menu():
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Show Statement")
    print("5. Exit")
while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        print(f"\nYour Current Balance: ₹{balance}")
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            statement.append(f"Deposited: ₹{amount}")
            print("Amount Deposited Successfully")
        else:
            print("Invalid Amount")
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient Balance")
        elif amount <= 0:
            print("Invalid Amount")
        else:
            balance -= amount
            statement.append(f"Withdrawn: ₹{amount}")
            print("Please collect your cash")
    elif choice == "4":
        print("\n===== TRANSACTION STATEMENT =====")
        if len(statement) == 0:
            print("No transactions yet")
        else:
            for s in statement:
                print(s)
        print(f"Current Balance: ₹{balance}")
    elif choice == "5":
        print("Thank you for using the ATM")
        break
    else:
        print("Invalid choice, try again")