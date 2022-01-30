""""Класс Матрица. Имеет следующие переменные:
- двумерный массив вещественных чисел;
- количество строк и столбцов в матрице.
Класс имеет следующие методы:
- сложение с другой матрицей;
- умножение на число;
- вывод на печать;
- умножение матриц
"""


import random
from typing import Any, Optional


class Matrix:

    def __init__(self, lines=2, column=2):
        """Инициализирует экземпляр класса Matrix.

        :param lines: количество строк матрицы
        :param column: количество столбцов матрицы
        Значения матрицы задаются рандомно
        """
        self._matrix = []
        self.lines = lines
        self.column = column

        for _ in range(lines):
            col = []
            for i in range(column):
                col.append(random.randint(0, 10))
            self._matrix.append(col)

    def __add__(self, other):
        """Метод сложения матриц. Возвращает первоначальную матрицу с новыми значениями"""
        if not isinstance(other, Matrix):
            raise TypeError
        if self.lines != other.lines or self.column != other.column:
             raise ValueError('Количество строк и столбцов матриц должно совпадать')
        i = 0
        for l in range(self.lines):
            for c in range(self.column):
                self._matrix[l][c] += other[l][c]
        return self._matrix

    def __mul__(self, other: float):
        """Умножает матрицу на число или матрицу

        :param other: множитель
        :return: возвращает первоначальную матрицу с новыми значениями
        """
        if not isinstance(other, (int, float, Matrix)):
            raise TypeError('Значение должно быть int или float')
        #Умножение матрицы на число
        if isinstance(other, (int, float)):
            for l in range(self.lines):
                for c in range(self.column):
                    self._matrix[l][c] *= other
            return self._matrix
        #Умножение матрицы на матрицу
        else:
            if self.column != other.lines:
                raise ValueError('Количество столбцов в первой матрице должно совпадать с кол-вом строком второй')
            n = []
            new_matrix = []
            for l in range(self.lines):
                a = 0
                b = 0
                for i, x in enumerate(self._matrix[l]):
                    a += x * other[i][0]
                    b += x * other[i][1]
                n.append(a)
                n.append(b)
                new_matrix.append(n)
                n = []
            self._matrix = new_matrix
            return self._matrix

    def __repr__(self):
        return f'{self._matrix}'

    def __getitem__(self, item):
        return self._matrix[item]

    def print_matrix(self):
        """Выводит матрицу на печать в столбик"""
        for line in range(self.lines):
            print(self._matrix[line])


matrix_1 = Matrix()
matrix_2 = Matrix()

print(matrix_1.print_matrix())
print('****')
print(matrix_2.print_matrix())
print('****')
# matrix_1+matrix_2
# print(matrix_1.print_matrix())
# print('****')
# matrix_2 * 2
# print(matrix_2.print_matrix())
matrix_1 * matrix_2
print(matrix_1.print_matrix())


