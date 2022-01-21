from typing import Optional

class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

        self.is_valid_date(self._day, self._month, self._year)

    # какой декоратор следует применить?
    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
            return True
        return False
            # записать условие проверки високосного года

    def get_max_day(self, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if self.is_leap_year:
            return Date.DAY_OF_MONTH[1][month - 1]
        return Date.DAY_OF_MONTH[0][month - 1]
        # вернуть количество дней указанного месяца

    def is_valid_date(self, day: int, month: int, year: int) -> None:
        """Проверяет, является ли дата корректной"""
        if not isinstance(day, int):
            raise TypeError
        if not isinstance(month, int):
            raise TypeError
        if not isinstance(year, int):
            raise TypeError
        if 1 > year:
            raise ValueError
        if 1 > month or month > 12:
            raise ValueError

        if 1 > day or day > self.get_max_day(month, year):
            raise ValueError
        # если указанный набор день, месяц и год неверны, то вызвать ошибку ValueError

    # записать getter и setter для дня
    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day: int):
        self._day = day

    # записать getter и setter для месяца
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month: int):
        self._month = month

    # записать getter и setter для года
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year: int):
        self._year = year

    def __repr__(self):
        return f'{self.__class__.__name__}({self.day},{self.month},{self.year})'


if __name__ == "__main__":
    date1 = Date(1, 12, 2021)
    print(date1)
    print(date1.is_leap_year(2021))
    print(date1.get_max_day(12, 2021))

    date2 = Date(20, 2, 1976)
    print(date2)
    print(date2.is_leap_year(1976))
    print(date2.get_max_day(2, 1976))

