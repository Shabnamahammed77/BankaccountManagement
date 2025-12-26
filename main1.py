from bank import Bank

bank = Bank()

while True:
    print("\n--- Bank Management System ---")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        bank.create_account()
    elif choice == "2":
        bank.deposit()
    elif choice == "3":
        bank.withdraw()
    elif choice == "4":
        bank.check_balance()
    elif choice == "5":
        bank.view_accounts()
    elif choice == "6":
        print("Thank you for using the bank system 🏦")
        break
    else:
        print("❌ Invalid choice")
