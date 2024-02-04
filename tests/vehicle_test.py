from auto.vehicle import Car,Motorcycle


def test_inheritance():
    car = Car("Camry", "Toyota", 4)
    motorcycle = Motorcycle("Speedster", "Harley Davidson", False)
    assert car.model == "Camry"
    car.display_info()
    motorcycle.display_info()
