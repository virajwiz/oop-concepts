class Car:
    color = "white"
    def __init__(self, color, model, year, make):
        self.color = color
        self.model = model
        self.year = year
        self.make = make
        self.is_running = False
 
    def start_engine(self):
        if not self.is_running:
            print(f"The {self.color} {self.model} {self.make}'s enigine is started.")
            self.is_running = True
        else:
            print("The engine is already running.")

    def drive(self):
        if self.is_running:
            print(f"The {self.color} {self.model} {self.make} is on the move.")
        else:
            print("Start the engine first.")

    def stop(self):
        if self.is_running:
            print(f"The {self.color} {self.model} {self.make}'s engine has stopped.")
            self.is_running = False
        else:
            print("The engine is already off.")
