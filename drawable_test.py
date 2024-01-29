from drawable import Circle, Rectangle, Triangle

circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

shapes = [circle, rectangle, triangle]

for shape in shapes:
    shape.draw()