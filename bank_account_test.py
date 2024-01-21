from bank_account import BankAccount
my_account = BankAccount("Viraj",1000)
account2 = BankAccount("Bob", 10000)

print(my_account.account_holder, my_account.balance)
print(account2.account_holder, account2.balance)

print(BankAccount.interest_rate)
print(my_account.calculate_interest())
print(account2.calculate_interest())

#my_account.deposit(500)