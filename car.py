class Car:
    color = "white"
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
 
    def start_engine(self):
        print(f"The {self.color} {self.model}'s enigine is started.")

    def drive(self):
        print(f"The {self.color} {self.model} is on the move.")

    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")
