#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABC, abstractmethod
import math


class Figure(ABC):
    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass


class Rectangle(Figure):
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

    def area(self):
        return self.side_1 * self.side_2

    def perimeter(self):
        return self.side_1 * 2 + self.side_2 * 2

    def is_rectangle_possible(self, side_1, side_2):
        return (side_1 * side_2) > 0


class Square(Rectangle):
    def __init__(self, side_1):
        super().__init__(side_1, side_1)


class Triangle(Figure):
    def __init__(self, height, side_1, side_2, side_3):
        self.height = height
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def area(self):
        return self.side_1 * self.height * 0.5

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def is_triangle_possible(self, side_1, side_2, side_3):
        return (
            side_1 < side_2 + side_3
            and side_2 < side_1 + side_3
            and side_3 < side_1 + side_2
        )


class Wheel(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    def is_wheel_possible(self, radius):
        return (2 * (math.pi) * radius) > 0
