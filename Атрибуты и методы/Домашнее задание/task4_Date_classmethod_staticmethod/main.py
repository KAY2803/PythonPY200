class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year: int):
        """Проверяет, является ли год високосным"""
        if year % 4 == 0:
            return f'{year} - високосный год'
        else:
            return f'{year} - обычный год'
        #

    @staticmethod
    def get_max_day(month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if year % 4 == 0:
            return Date.DAY_OF_MONTH[1][month-1]
        else:
            return Date.DAY_OF_MONTH[0][month-1]
        #

    def is_valid_date(self, day: int, month: int, year: int):
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

    def __repr__(self):
        return f'{self.__class__.__name__}({self.day},{self.month},{self.year})'

        #


if __name__ == "__main__":
    date1 = Date(1, 12, 2021)
    print(date1)
    print(date1.is_leap_year(2021))
    print(date1.get_max_day(12, 2021))

    date2 = Date(20, 2, 1976)
    print(date2)
    print(date2.is_leap_year(1976))
    print(date2.get_max_day(2, 1976))
    pass
