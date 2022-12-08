import pytest

from srv.square import Square
from srv.triangle import Triangle


def test_circle_name():
    triangle = Triangle(4, 5, 6)
    assert triangle.NAME == "Triangle"


triangle_area = [
    (4, 5, 6, 9.921567416492215),
    (7, 8, 9, 26.832815729997478),
    (10, 11, 12, 51.521233486786784)
]


@pytest.mark.parametrize("side_1,side_2,side_3,area", triangle_area)
def test_circle_area(side_1, side_2, side_3, area):
    triangle = Triangle(side_1, side_2, side_3)
    assert triangle.area == area


triangle_perimeter = [
    (4, 5, 6, 15),
    (7, 8, 9, 24),
    (10, 11, 12, 33)
]


@pytest.mark.parametrize("side_1,side_2,side_3,perimeter", triangle_perimeter)
def test_circle_area(side_1, side_2, side_3, perimeter):
    triangle = Triangle(side_1, side_2, side_3)
    assert triangle.perimeter == perimeter


triangle_area = 187.74964387392123


def test_triangle_add_area():
    triangle = Triangle(12, 15, 17)
    square = Square(10)
    assert triangle.add_area(square) == triangle_area
