from math import pi

from srv.figure import Figure


class Circle(Figure):
    NAME = "Circle"

    def __init__(self, diameter):
        if type(diameter) not in [int, float]:
            raise ValueError("Некорректные данные")
        self.diameter = diameter

    @property
    def area(self):
        return pi * (self.diameter ** 2)

    @property
    def perimeter(self):
        return 2 * pi * self.diameter
