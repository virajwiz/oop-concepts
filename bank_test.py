from bank import SavingsBankAccount

account = SavingsBankAccount("0123456","Viraj",2000)
print(account.display_balance())
print(account.deposit(1000))
print(account.display_balance())
print(account.deposit(500))
print(account.display_balance())

account.withdraw(500)
print(account.display_balance())

print(account.get_balance())
account.__account_holder = "Anand"
account.set_account_holder("Anand")
print (account.display_balance())