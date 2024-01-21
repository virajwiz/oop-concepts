class BankAccount:
    interest_rate = 0.02

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} successfull. New balance: ${self.balance}")

    def calculate_interest(self):
        interest_amount = self.balance * BankAccount.interest_rate
        return interest_amount 