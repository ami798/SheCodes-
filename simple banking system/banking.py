# Initialize the balance
balance = 0

while True:
    # Display menu options
    print("\nBanking System Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    # user's choice
    choice = input("Please select an option (1-4): ").strip()

    # Halt the loop if the input is 4
    if choice == "4":
        print("Exiting the banking system. Have a great day!")
        break
    
    # Check Balance
    elif choice == "1":
        print(f"Your current balance is: ${balance}")
    
    # Deposit
    elif choice == "2":
        amount = float(input("Enter the amount to deposit: ").strip())
        if amount > 0:
            balance += amount
            print(f"${amount} has been deposited. Your new balance is: ${balance}")
        else:
            print("Deposit amount must be positive.")
    
    # Withdraw
    elif choice == "3":
        amount = float(input("Enter the amount to withdraw: ").strip())
        if amount > 0:
            if amount <= balance:
                balance -= amount
                print(f"${amount} has been withdrawn. Your new balance is: ${balance}")
            else:
                print("Insufficient balance for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")
    
    # Invalid Choice
    else:
        print("Invalid choice. Please select a valid option (1-4).")
