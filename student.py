class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)
        print(f"{self.name} is enrolled in {course}.")
        