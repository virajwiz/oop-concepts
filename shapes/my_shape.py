from abc import ABC, abstractmethod

class Printable:
    def print_info(self):
        pass

class Shape(ABC):

    def __init__(self, name):
        self.name = name

        @abstractmethod
        def area(self):
            pass

        @abstractmethod
        def perimeter(self):
            pass

        @abstractmethod
        def color(self):
            pass

class Circle(Shape, Printable):
    def __init__(self, name, radius, color):
        super().__init__(name)
        self.radius = radius
        self.color = color

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def color(self):
        return self.color

    def print_info(self):
        print("Circle")

class Rectangle(Shape, Printable):
    def __init__(self, name, length, width, color):
        super().__init__(name)
        self.length = length
        self.width = width
        self.color = color

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def color(self):
        return self.color

    def print_info(self):
        print("Rectangle")
