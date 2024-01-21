class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def display_info(self):
        print (f"Name:{self.name}, Age:{self.age}")

class Student(Person):
    def __init__(self,name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")
        