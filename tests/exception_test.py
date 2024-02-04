from exceptions.calculate import Calculate


def test_divide():
    c = Calculate()
    result = c.divide(4, 2)
    assert result == 2

def test_divide_by_zero():
    c = Calculate()
    result = c.divide(4, 0)
    assert result is not None
    assert result == 0

def test_value_error():
    c = Calculate()
    result = c.divide(4, "2")
    assert result == 0