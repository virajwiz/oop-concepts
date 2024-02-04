class Animal:

    def __init__ (self, color, weight):
        self.__color = color
        self.__weight = weight

    def get_color(self):
        return self.__color

    def get_weight(self):
        return self.__weight

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
   
    
    def make_sound(self):
        #super().make_sound()
        print("Woof Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow Meow")
