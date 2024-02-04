from shop.shopping import Product, Customer, Electronics, Clothing, Book


def test_class_models():
    product1 = Product(1, "Laptop", 1200, 10, "work office", "black")
    product2 = Product(2, "Smartphone", 800, 15, "mobile", "white")

    customer1 = Customer(101, "John", "john@gmail.com")
    customer1.add_to_cart(product1, 2)
    customer1.add_to_cart(product2, 1)

    print(f"{customer1.name}, {customer1.cart}")
    customer1.place_order()
    print(f"{product1.name}: stock quantity after order:{product1.stock_quantity}.")

    customer1.add_to_cart(product1, 5)
    customer1.delete()

    print(f"{customer1.name}, {customer1.cart}")
    customer1.add_to_cart(product1, 1)
    print(f"{customer1.name}, {customer1.cart}")




    electronics_product = Electronics(1,"Laptop", 1200, 10, "work office", "black", "xyz elec")
    clothing_product = Clothing(2, "Tshirt", 25, 50, "sports", "red", "large")
    book_product = Book(3, "Python Programming", 40, 20,"technology", "yellow", "Guido van Rossum")

    print(f"{electronics_product.name},{electronics_product.brand}")
    print(f"{clothing_product.name}, {clothing_product.size}")
    print(f"{book_product.name}, {book_product.author}")