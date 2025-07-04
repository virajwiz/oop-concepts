class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

        print("Enter the length: ")
        length = int(input())

        print("Enter the width: ")
        width = int(input())

    def display_area(self):
        area = (self.length*self.width)
        print(f"area is : {area}")

    def display_perimeter(self):
        perimeter =  2*(self.length + self.width)
        print(f"perimeter is : {perimeter}")

    def report_dimensions(self):
        print(f"length = {self.length} width = {self.width}")

        

    

