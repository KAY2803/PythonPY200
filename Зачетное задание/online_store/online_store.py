from typing import Optional

from goods import Goods, Category, Basket
from user import User


class PasswordError(Exception):
    """Класс исключения, которое возникает, если Пользователь неверно ввел логин и/или пароль"""
    pass


class OnlineStore:

    def __init__(self, goods: Optional[Goods] = None):
        """Инициализируем онлайн магазин с одним параметром - товары.

        :param goods: товары

        """

        self.goods = goods
        self.__user = None
        self.identification = False
        self.catalogue = []

    def set_catalogue(self, category):
        self.catalogue.append(category)
        return self.catalogue

    def get_catalogue(self):
        for index, category in enumerate(self.catalogue, start=1):
            print(index, category)

    @property
    def user(self):
        """
        Возвращает значение пользователя класса User
        :return: self.user
        """
        return self.__user

    @user.setter
    def user(self, user: User):
        """Присваивает значение атрибуту user.
        Принимает аргумент user класса User.

        """

        if not isinstance(user, User):
            raise TypeError(f'Ожидается {User}, получено{type(user)}')
        self.__user = user

    def check_identification(self, name: str, password: str):
        """Метод идентификации Покупателя. При введении правильных логина и пароля
        Покупатель получает доступ к каталогу товаров.

        :param name: имя (логин)
        :param password: пароль
        :return: True, если параметры введены корректно
        """
        while True:
            name = input('Введите логин: ')
            password = input('Введите пароль: ')
            try:
                if name == self.__user.login and password == self.__user.password:
                    self.identification = True
                    print('Welcome our store! Have a good shoping!\n')
                    return self.identification
                else:
                    raise PasswordError
            except PasswordError:
                print('Логин и/или пароль введены неверно')

    def __repr__(self):
        return f'{self.catalogue}'

    def look_goods(self):
        """Смотрим и выбираем товаров. Метод возвращает корзину выбранных товаров."""
        while True:
            self.get_catalogue()
            category_to_look = int(input(f'Выберите категорию товаров для просмотра, указав номер категории: '))
            if category_to_look in range(1, len(self.catalogue)+1):
                choice = int(input(f'Выберите товар {self.catalogue[category_to_look-1].get_goods_in_category()}, '
                               f'указав номер товара '))
            else:
                continue
            for index, goods in enumerate(self.catalogue[category_to_look-1], start=1):
                if choice == index:
                    self.__user.basket.put_in_basket(goods)
                    print(f'в корзине {self.__user.basket}')
            finish = input(f'Продолжить покупки: нажмите Y для продолжения или N для перехода к оплате: ')
            if finish.lower() == 'n':
                return self.__user.basket

    def _buy_goods(self):
        """Покупаем товар. Метод возвращает массив купленных товаров."""
        self.look_goods()
        self.check_identification('name', 'password')
        if self.identification:
            if self.__user.basket:
                common_price = 0
                for goods in self.__user.basket:
                    common_price += goods.price
                sum_to_pay = float(input(f'К оплате {round(common_price, 2)}: '))
                if sum_to_pay >= common_price:
                    print(f'Спасибо за покупку! Вы приобрели: {self.__user.basket}')
                    return ''
                else:
                    self.__user.basket.clear()
                    print('Немного не хватает, ждем в другой раз')
                    return ''


if __name__ == '__main__':

    good_1 = Goods('carrot', 2.5, 87.2)
    good_2 = Goods('potato', 2.8, 88.4)
    good_3 = Goods('pasta', 4.3, 89.9)
    good_4 = Goods('coffee', 1.75, 95)
    # print(good_1, good_2, good_3, good_4)

    veg_category = Category('veg')
    veg_category.add_goods([good_1])
    veg_category.add_goods([good_2])
    gros_category = Category('gros')
    gros_category.add_goods([good_3, good_4])
    # print(veg_category, gros_category)

    shop = OnlineStore()
    shop.set_catalogue(veg_category)
    shop.set_catalogue(gros_category)
    # shop.get_catalogue()

    shop.user = User('Bob', '123')
    shop.user.basket = Basket()
    shop._buy_goods()




