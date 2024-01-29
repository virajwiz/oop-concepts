from my_shape import Circle, Rectangle

circle = Circle("circle1", 3, "Black")
rectangle = Rectangle("rectangle1", 4, 2, "Blue")

print(f"{circle.name} : Area : {circle.area()}, Perimeter : {circle.perimeter()}, Color : {circle.color}")
print(f"{rectangle.name} : Area : {rectangle.area()}, Perimeter : {rectangle.perimeter()}, Color : {rectangle.color}")

def print_area(shape):
    print(shape.area())

def print_perimeter(shape):
    print(shape.perimeter())

print_area(circle)
print_area(rectangle)

print_perimeter(circle)
print_perimeter(rectangle)
