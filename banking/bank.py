class SavingsBankAccount:
    def __init__(self, account_number, account_holder, balanace = 0):
        self.account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balanace



    def get_balance(self):
        return self.__balance

    def set_account_holder(self, holder):
        self.__account_holder = holder

    def display_balance(self):
        return f"Account Holder:{self.__account_holder}\n Account Number:{self.account_number}\n Balance:{self.__balance}"

    def deposit(self, amount):
        if amount>0:
            self.__balance+=amount
            return f"Deposit successful. New balance:${self.__balance}"
        else:
            return "Invalid deposit amount. Please enter a positive amount"

        
    def withdraw(self, amount):
        if 0<amount<=self.__balance:
            self.__balance -= amount
            return f"Withdraw successful. New balance:${self.__balance}"
        else:
            return "Invalid withdrwal amount or insufficient fund. "
