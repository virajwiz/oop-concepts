from intro.ooperson import Person, Student

def test_inheritance():
    person1 = Person("Viraj", 19)
    student1 = Student("Anand", 47, 101)
    person1.display_info()
    student1.display_info()
    student1.study()
