from auto.car import Car

def test_methods():
    car1 = Car("blue","polo",2010, "VW")
    # print(car1.color)
    # print(car1.model)
    # print(car1.year)
    # print(car1.make) 

    print(f"My car is {car1.year} {car1.color} {car1.make} {car1.model}")

    car1.start_engine()
    car1.drive()
    car1.stop()

    car2 = Car("black", "honda", 2023, "city")
    car2.start_engine()
    car2.drive()