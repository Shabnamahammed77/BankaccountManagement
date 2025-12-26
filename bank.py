import pickle
import os
from account import BankAccount

FILE_NAME = "bankdata.pick"

class Bank:

    def load_accounts(self):
        accounts = []
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "rb") as file:
                try:
                    while True:
                        accounts.append(pickle.load(file))
                except EOFError:
                    pass
        return accounts

    def save_accounts(self, accounts):
        with open(FILE_NAME, "wb") as file:
            for acc in accounts:
                pickle.dump(acc, file)

    def create_account(self):
        accounts = self.load_accounts()
        acc_no = int(input("Enter Account Number: "))

        for acc in accounts:
            if acc.acc_no == acc_no:
                print("⚠️ Account already exists!")
                return

        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Initial Balance: "))
        accounts.append(BankAccount(acc_no, name, balance))
        self.save_accounts(accounts)

        print("✅ Account created successfully")

    def deposit(self):
        accounts = self.load_accounts()
        acc_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Deposit Amount: "))

        for acc in accounts:
            if acc.acc_no == acc_no:
                acc.balance += amount
                self.save_accounts(accounts)
                print("✅ Amount deposited")
                return

        print("❌ Account not found")

    def withdraw(self):
        accounts = self.load_accounts()
        acc_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Withdrawal Amount: "))

        for acc in accounts:
            if acc.acc_no == acc_no:
                if acc.balance >= amount:
                    acc.balance -= amount
                    self.save_accounts(accounts)
                    print("✅ Withdrawal successful")
                else:
                    print("❌ Insufficient balance")
                return

        print("❌ Account not found")

    def check_balance(self):
        accounts = self.load_accounts()
        acc_no = int(input("Enter Account Number: "))

        for acc in accounts:
            if acc.acc_no == acc_no:
                print(f"💰 Current Balance: ₹{acc.balance}")
                return

        print("❌ Account not found")

    def view_accounts(self):
        accounts = self.load_accounts()
        print("\nACC NO\tNAME\tBALANCE")
        print("-" * 30)
        for acc in accounts:
            acc.display()
