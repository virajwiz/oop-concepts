from exceptions.custom_exceptions import InsufficientFundsError, InvalidTransactionError, InvalidValueError


class SavingsBankAccount:
    def __init__(self, account_number, account_holder, balanace = 0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balanace



    def get_balance(self):
        return self.balance

    def set_account_holder(self, holder):
        self.account_holder = holder

    def display_balance(self):
        return f"Account Holder:{self.account_holder}\n Account Number:{self.account_number}\n Balance:{self.balance}"

    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            return f"Deposit successful. New balance:${self.balance}"
        else:
            return "Invalid deposit amount. Please enter a positive amount"

        
    def withdraw(self, amount):
        if 0<amount<=self.balance:
            self.balance -= amount
            return f"Withdraw successful. New balance:${self.balance}"
        else:
            return "Invalid withdrwal amount or insufficient fund. "

class Transaction:
    @staticmethod
    def deposit(account, amount):
        if account is None:
            raise InvalidValueError("account cannot be none")
        if amount <= 0:
            raise InvalidTransactionError("Invalid deposit amount")
        account.balance += amount
        print(f"Deposited {amount}. New balance: {account.balance}")

    @staticmethod
    def withdraw(account, amount):
        if account is None:
            raise InvalidValueError("account cannot be none")
        if amount <= 0:
            raise InvalidTransactionError("Invalid withdraw amount.")

        if amount > account.balance:
            raise InsufficientFundsError(account.balance, amount)

        account.balance -= amount
        print(f"Withdrew: {amount}, New balance: {account.balance}")

    @staticmethod
    def check_balance(account):
        print(f"account balacnce for {account.account_holder}: {account.balance}")