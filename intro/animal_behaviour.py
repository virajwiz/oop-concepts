class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Swimable:
    def swim(self):
        pass

class Flyable:
    def fly(self):
        pass

class Runnable:
    def run(self):
        pass

class Bird(Animal, Flyable):
    def __init__(self, name, age):
        super().__init__(name, age)

    def fly(self):
        print(f"{self.name} is flying.")

class Fish(Animal, Swimable):
    def __init__(self, name, age):
        super().__init__(name, age)

    def swim(self):
        print(f"{self.name} is swimming.")

class Mammal(Animal, Runnable):
    def __init__(self, name, age):
        super().__init__(name, age)

    def run(self):
        print(f"{self.name} is running.")