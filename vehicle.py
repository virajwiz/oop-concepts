class Vehicle:
    def __init__(self, model, brand):
        self.__model = model
        self.__brand = brand

    @property
    def model(self):
        return self.__model

    @property
    def brand(self):
        return self.__brand

    def display_info(self):
        print(f"{self.brand} {self.model}")

class Car(Vehicle):
    def __init__(self, model, brand, num_doors):
        super().__init__(model, brand)
        self.__num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"{self.__num_doors} doors.")

class Motorcycle(Vehicle):
    def __init__(self, model, brand, has_sidecar):
        super().__init__(model, brand)
        self.__has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        if self.__has_sidecar:
            print("Has sidecar.")

        else:
            print("Does not have sidecar.")

            