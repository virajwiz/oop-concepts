from paymentmethod import CreditCard, Refundable, PaymentMethod


credit_card = CreditCard("1234-5678-9012-3456", "John Doe")

credit_card.display_payment_details()
credit_card.process_payment(100)
credit_card.process_refund(50)
credit_card.display_payment_details()