# product class
# product id, name, price, stock
# customer class
# method add to cart, place order

class Product:
    def __init__(self, product_id, name, price, stock_quantity, style_name, color):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock_quantity = stock_quantity
        self.__style_name = style_name
        self.__color = color

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock_quantity(self):
        return self.__stock_quantity

    @property
    def style_name(self):
        return self.__style_name

    @property
    def color(self):
        return self.__color

    def reduce_stock_quantity(self, quantity):
        if quantity <= self.__stock_quantity:
            self.__stock_quantity -= quantity
            return True
        else:
            print(f"Insufficient stock for {self.name}.")
            return False
    
    def __str__(self) -> str:
        return self.name

class Electronics(Product):
    def __init__(self, product_id, name, price, stock_quantity, style_name, color, brand):
        super().__init__(product_id, name, price, stock_quantity, style_name, color)
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand

class Clothing(Product):
    def __init__(self, product_id, name, price, stock_quantity, style_name, color, size):
        super().__init__(product_id, name, price, stock_quantity, style_name, color)
        self.__size = size

    @property
    def size(self):
        return self.__size


class Book(Product):
    def __init__(self, product_id, name, price, stock_quantity, style_name, color, author):
        super().__init__(product_id, name, price, stock_quantity, style_name, color)
        self.__author = author

    @property
    def author(self):
        return self.__author

class Customer:
    def __init__(self, customer_id, name, email):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__cart = []

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def cart(self):
        return self.__cart

    def add_to_cart(self, product, quantity):
        if product.reduce_stock_quantity(quantity):
            self.__cart.append({"product":product,"quantity":quantity})
            print(f"{quantity} {product.name} added to the cart.")

    def place_order(self):
        if not self.__cart:
            print("Cart is empty, add products before placing an order.")
            return 
        total_price = 0
        for item in self.__cart:
            total_price += item["product"].price * item["quantity"]

        print(f"Order place by {self.name}, total amount: {total_price}.")
        self.__cart = []

    def delete(self):
        self.__cart = []

