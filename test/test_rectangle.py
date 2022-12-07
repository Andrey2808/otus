import pytest

from srv.rectangle import Rectangle
from srv.square import Square


def test_rectangle_name():
    rectangle = Rectangle(10, 5)
    assert rectangle.NAME == 'Rectangle'


rectangle_area = [
    (2, 1, 2),
    (2, 2, 4)
]


@pytest.mark.parametrize("side_1,side_2,area", rectangle_area)
def test_rectangle_area(side_1, side_2, area):
    rectangle = Rectangle(side_1, side_2)
    assert rectangle.area == area


rectangle_perimeter = [
    (2, 1, 6),
    (2, 2, 8)
]


@pytest.mark.parametrize("side_1,side_2,perimeter", rectangle_perimeter)
def test_rectangle_perimeter(side_1, side_2, perimeter):
    rectangle = Rectangle(side_1, side_2)
    assert rectangle.perimeter == perimeter


def test_rectangle_square():
    rectangle = Rectangle(10, 5)
    square = Square(5)
    assert rectangle.add_area(square) == 75
