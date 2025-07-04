from shapes.polygon import Rectangle, Square


def test_inheritance():
    rectangle1 = Rectangle("blue", 5, 4)
    square1 = Square("Red", 4)

    rectangle1.display_info()
    rectangle1.calculate_area()
    rectangle1.calculate_perimeter()

    square1.display_info()
    square1.calculate_area()
    square1.calculate_perimeter()