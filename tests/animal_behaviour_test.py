from intro.animal_behaviour import Bird, Fish, Mammal


def test_animal_behavior():
    bird = Bird("crow", 2)
    fish = Fish("nemo", 1)
    mammal = Mammal("Zebra", 3)

    bird.fly()
    fish.swim()
    mammal.run()

    