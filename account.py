class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def display(self):
        print(f"{self.acc_no}\t{self.name}\t₹{self.balance}")
