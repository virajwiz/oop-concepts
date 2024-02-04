from shapes.drawable import Circle, Rectangle, Triangle

def test_abstract():
    circle = Circle()
    rectangle = Rectangle()
    triangle = Triangle()

    shapes = [circle, rectangle, triangle]

    for shape in shapes:
        shape.draw()