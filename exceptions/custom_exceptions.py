class CustomError(Exception):
    def __init__(self, message = "A custom error occured"):
        self.message = message
        super().__init__(self.message)


class InsufficientFundsError(Exception):
    def __init__(self, amount_balance, amount_requested):
        self.amount_balance = amount_balance
        self.amount_requested = amount_requested
        super().__init__(f"Insufficient funds. Current balance:{amount_balance}, Amount requested:{amount_requested}")
        