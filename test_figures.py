from figure_calculations import *

result_triangle = Triangle(2, 3, 4, 5)


def test_is_triangle_possible():
    assert result_triangle.is_triangle_possible(3, 4, 5)


def test_is_triangle_area_correct():
    assert result_triangle.area() == 3


def test_is_triangle_perimeter_correct():
    assert result_triangle.perimeter() == 12


result_rectangle = Rectangle(3, 4)


def test_is_rectangle_possible():
    assert result_rectangle.is_rectangle_possible(3, 4)


def test_is_rectangle_area_correct():
    assert result_rectangle.area() == 12


def test_is_rectangle_perimeter_correct():
    assert result_rectangle.perimeter() == 14


result_wheel = Wheel(3)


def test_is_wheel_possible():
    assert result_wheel.is_wheel_possible(3)


def test_is_wheel_area_correct():
    assert result_wheel.area() == 28.27


def test_is_wheel_perimeter_correct():
    assert result_wheel.perimeter() == 18.85
