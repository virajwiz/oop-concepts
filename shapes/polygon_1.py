class Polygon_1:
    def __init__(self, sides):
        self.sides = sides
       
    def display_info(self):
        print(f"Polygon with {self.sides}")

    class Rectangle(Polygon_1):
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def calculate_area(self):
            area = self.width*self.length
            print(f"area is: {area}")

        def calculate_perimeter(self):
            perimeter = 2*(self.length + self.width)
            print(f"perimeter is: {perimeter}")

        def report_dimensions(self):
            print(f"length is: {self.length} and widht is: {self.width}")

    class Square(Polygon_1):
        def __init__(self, sides):
            self.sides = sides

        def calculate_area(self):
            area = self.sides*self.sides
            print(f"")

