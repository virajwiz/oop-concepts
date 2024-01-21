from animal import Animal, Dog, Cat

generic_animal = Animal("white",10)
my_dog = Dog("black",20)
generic_animal.make_sound()
my_dog.make_sound()

print(my_dog.get_color())

my_cat = Cat("brown", 15)
my_cat.make_sound()
print(my_cat.get_color())

my_dog.set_speed(200)
print(my_dog.get_speed())

my_cat.set_speed(100)
print(my_cat.get_speed())


