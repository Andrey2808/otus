from srv.figure import Figure


class Rectangle(Figure):
    NAME = "Rectangle"

    def __init__(self, side_1, side_2):
        for item in [side_1, side_2]:
            if type(item) not in [int, float]:
                raise ValueError("Некорректные данные")
        self.side_1 = side_1
        self.side_2 = side_2

    @property
    def area(self):
        return self.side_1 * self.side_2

    @property
    def perimeter(self):
        return 2 * (self.side_1 + self.side_2)