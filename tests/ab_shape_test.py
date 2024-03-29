from shapes.ab_shape import Circle, Rectangle, Shape

def print_area(shape):
    print(shape.area())


def test_polymorphism():
    circle = Circle("circle", 4)
    rectangle = Rectangle("rectangle", 4, 5)
    print(f"{circle.name} : Area : {circle.area()}, Perimeter : {circle.perimeter()}")
    print(f"{rectangle.name} : Area : {rectangle.area()}, Perimeter : {rectangle.perimeter()}")

    print_area(circle)
    print_area(rectangle)

    #shape = Shape("shape")