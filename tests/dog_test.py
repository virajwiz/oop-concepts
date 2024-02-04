from intro.dog import Dog

def test_variable():
    dog1 = Dog("Buddy",3)
    dog2 = Dog("Max",5)

    print(dog1.name)
    dog1.bark()

    print(dog2.name)
    dog2.dog_years()

    Dog.species = "Canis lupus"

    dog3 = Dog("Tiger", 3)
    dog3.age = 4
    print(dog2.species)
    print(dog3.age)
