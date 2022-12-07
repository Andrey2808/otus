import pytest as pytest

from srv.circle import Circle
from srv.square import Square


def test_circle_name():
    circle = Circle(10)
    assert circle.NAME == "Circle"


circle_area = [
    (0, 0),
    (1, 3.141592653589793),
    (5, 78.53981633974483)
]


@pytest.mark.parametrize("diameter,area", circle_area)
def test_circle_area(diameter, area):
    circle = Circle(diameter)
    assert circle.area == area


circle_perimeter = [
    (0, 0),
    (1, 6.283185307179586),
    (5, 31.41592653589793)
]


@pytest.mark.parametrize("diameter,perimeter", circle_perimeter)
def test_circle_area(diameter, perimeter):
    circle = Circle(diameter)
    assert circle.perimeter == perimeter


square_area = 178.53981633974485


def test_circle_add_area():
    circle = Circle(5)
    square = Square(10)
    assert circle.add_area(square) == square_area
