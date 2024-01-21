from student import Student

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

print(student1.name, student1.age)
print(student2.name, student2.age)

student1.enroll_course("Mathematics")
student2.enroll_course("Computer Science")

student1.enroll_course("Physics")
print(student1.courses)
print(student2.courses)