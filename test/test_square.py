import pytest

from srv.square import Square


def test_square_name():
    square = Square(5)
    assert square.NAME == 'Square'


square_area = [
    (5, 25),
    (4, 16,),
    (10, 100)
]


@pytest.mark.parametrize("side,area", square_area)
def test_square_area(side, area):
    square = Square(side)
    assert square.area == area


square_perimeter = [
    (1, 4),
    (0, 0),
    (5, 20)
]


@pytest.mark.parametrize("side,perimeter", square_perimeter)
def test_square_perimeter(side, perimeter):
    square = Square(side)
    assert square.perimeter == perimeter


square = 200


def test_square_add_area():
    square_1 = Square(10)
    square_2 = Square(10)
    assert square_1.add_area(square_2) == 200
