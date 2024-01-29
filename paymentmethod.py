from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def display_payment_details(self):
        pass

class Refundable(ABC):
    @abstractmethod
    def process_refund(self, amount):
        pass

class CreditCard(PaymentMethod, Refundable):
    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder
        self.balance = 0

    def process_payment(self, amount):
        self.balance += amount
        print(f"Payment of ${amount} processed using credit card ending in {self.card_number}")

    def display_payment_details(self):
        print(f"Credit Card Details: Card Holder - {self.card_holder}, Card Number - {self.card_number}")

    def process_refund(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Refund of${amount} processed from credit card ending in {self.card_number}")
        else:
            print("Refund cannot be processed. Insufficient balance.")

