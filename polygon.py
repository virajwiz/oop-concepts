class Polygon:
    def __init__(self, sides, color):
        self.sides = sides
        self.color = color

    def display_info(self):
        print(f"Polygon with {self.sides} sides, color: {self.color}")

    def calculate_area(self):
        print("Calculating area of a generic polygon")

class Rectangle(Polygon):
    def __init__(self, color, length, width):
        super().__init__(sides = 4, color = color)
        self.width = width
        self.length = length

    def display_info(self):
        super().display_info()
        print(f"length: {self.length}, width: {self.width}")

    def calculate_area(self):
        area = self.length*self.width
        print(f"Calculating area of rectangle: {area}")

class Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color, side, side)

    def calculate_area(self):
        area = self.length ** 2
        print(f"Calculating area of a square: {area}")
        