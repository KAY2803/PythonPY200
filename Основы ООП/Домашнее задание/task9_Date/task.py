class Date:
    def __init__(self, day: int, month: int, year: int):
        self.__day = self.__check_day(day)
        self.__month = self.__check_month(month)
        self.__year = self.__check_year(year)

    @staticmethod
    def __check_day(day: int):
        if not isinstance(day, int):
            raise TypeError ('only integers')
        return day

    @staticmethod
    def __check_month(month: int):
        if not isinstance(month, int):
            raise TypeError('only integers')
        return month

    @staticmethod
    def __check_year(year: int):
        if not isinstance(year, int):
            raise TypeError('only integers')
        return year

    def __repr__(self):
        return f'{self.__day}, {self.__month}, {self.__year}'

    def __str__(self):
        if len(str(self.__day)) < 2 or len(str(self.__month)) < 2:
            return f'0{self.__day}/0{self.__month}/{self.__year}'
        else:
            return f'{self.__day}/{self.__month}/{self.__year}'

date1 = Date(1, 1, 2020)

print(date1)
print(repr(date1))