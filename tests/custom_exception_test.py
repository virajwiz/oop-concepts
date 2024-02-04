from exceptions.custom_exceptions import CustomError, InsufficientFundsError

def withdraw(amount_balance, amount_requested):
    if amount_balance < amount_requested:
        raise InsufficientFundsError(amount_balance, amount_requested)


try:
    withdraw(100, 200)
except InsufficientFundsError as e:
    print(f"Error: {e}")
except CustomError as e:
    print(f"caught a custom exception:{e}")
except Exception as e:
    print(f"An unexpected error occured:{e}")
finally:
    print("Execution completed")