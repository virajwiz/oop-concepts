from shapes.shape import Shape, Rectangle


def test_inheritance_with_overloaded():
    rectangle1 = Rectangle("red", 5, 4)
    rectangle1.display_info()
    rectangle1.calculate_area()
    rectangle1.caluclate_area_overloaded(4)
