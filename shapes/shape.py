class Shape:
    def __init__(self, color):
        self.color = color

    def display_info(self):
        print(f"color:{self.color}")

    def calculate_area(self):
        print("Calculating area for a generic shape.")

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def display_info(self):
        super().display_info()
        print(f"length:{self.length}, width:{self.width}")

    def calculate_area(self):
        area = self.length * self.width
        print(f"Calculating area of the rectangle:{area}")

    def caluclate_area_overloaded(self, side):
        area = side ** 2
        print(f"Calculating area of a sqaure(overloaded method):{area}")
