from math import sum


def test(a, b):
    actual = sum(a, b)
    expected = a + b
    assert expected == actual


test(-5, 0)
test(-10, 21)
test(1000, 6781)
test(9000, 6781)
test(-10, -20)
test(-50, -101)
