from obliczanie_figur import *


def test_is_triangle_possible():
    result = Triangle(1, 1, 2, 3)
    assert result.is_triangle_possible(3, 4, 5)


def test_is_rectangle_possible():
    result = Rectangle(3, 3)
    assert result.is_rectangle_possible(3, 3)


def test_is_wheel_possible():
    result = Wheel(1)
    assert result.is_wheel_possible(1)
