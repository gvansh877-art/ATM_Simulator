import time

print("PLEASE INSERT YOUR CARD")

time.sleep(5)

password= 4023

pin=int(input("ENTER YOUR ATM PIN"))

if pin==password:

    print("1.== Display Balance")
    print("2.== Withdraw Balance")
    print("3.Deposite Balance")
    print("4.Statement transaction record")
    print("5.Exit")

    balance = 9000 

while True:
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your balance is:", balance)

        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Withdraw successful")
                print("Remaining balance:", balance)
            else:
                print("Insufficient balance")

        elif choice == 3:
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("Deposit successful")
            print("Updated balance:", balance)

        elif choice == 4:
            print("Transaction record not available yet")

        elif choice == 5:
            print("Thank you! Have a good day !Exiting ATM...")
            break

        else:
            print("Invalid choice")

    except:
        print("Please enter numbers only")