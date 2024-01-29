from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Drawable):
    def draw(self):
        print("Drawing a circle.")

class Rectangle(Drawable):
    def draw(self):
        print("Drawing a rectangle.")

class Triangle(Drawable):
    def draw(self):
        print("Drawing a Triangle.")

        