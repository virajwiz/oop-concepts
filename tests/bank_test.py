from banking.bank import SavingsBankAccount, Transaction
from exceptions.custom_exceptions import InsufficientFundsError, InvalidTransactionError, InvalidValueError


def test_control_structures():
    account = SavingsBankAccount("0123456","Viraj",2000)
    assert account is not None
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

def test_exceptions():
    account = SavingsBankAccount("123", "viraj", 1000)
    try:
        Transaction.deposit(account, 500)
        Transaction.withdraw(account, 200)
        Transaction.check_balance(account)
        
        Transaction.withdraw(account, 10000)
    except (InsufficientFundsError, InvalidTransactionError, InvalidValueError) as e:
        print(f"Error:{e}")


    

