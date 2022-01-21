import math


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure):
    """ Производный класс. Прямоугольник. """

    # определить конструктор и перегрузить метод area
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def area(self):
        super().area()
        return self.a * self.b

class Circle(Figure):
    """ Производный класс. Круг. """
    def __init__(self, r: int):
       self.r = r

    def area(self, P = 3.14):
        Figure.area(self)
        return self.r ** 2 * P
    # определить конструктор и перегрузить метод area


if __name__ == "__main__":
    fig = Figure()
    fig.area()

    rect = Rectangle(5, 10)
    print(rect.area())

    circle = Circle(5)
    print(circle.area())
