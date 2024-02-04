from intro.calculator import Calculator


def test_method_override():
    my_calculator = Calculator()
    result1 = my_calculator.add(2, 3)
    print(result1)

    result2 = my_calculator.add(2, 3, 5)
    print(result2)
