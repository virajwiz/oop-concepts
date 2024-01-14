from person import Person

person1 = Person("Viraj",19)
person2 = Person("Amitabh",18)

print(person1.name)
print(person2.age)

person1.greet()
person2.celebrate_birthday()

person1.age = 26
print(person1.age)

person2.celebrate_birthday()
print(person2.age)

print(person1.species)
print(person2.species)