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

        self.goods = Category.catalogue
        self.__user = None
        self.identification = False
        #self.check_identification('name', 'password')

    def __repr__(self):
        return f'{self.goods}'

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




    # self.basket = Basket([])



    #
    # def _look_goods(self):
    #     """Смотрим и выбираем товаров. Метод возвращает массив выбранных товаров."""
    #     if self.identification:
    #         while True:
    #             category_to_look = input(f'Выберите категорию товаров для просмотра из {Categories.catalogue.keys()}: ')
    #             if category_to_look in Categories.catalogue.keys():
    #                 choice = input(f'Выберите товар: {Categories.catalogue[category_to_look]} ')
    #             else:
    #                 continue
    #             for goods in Categories.catalogue[category_to_look]:
    #                 if choice == goods.get('name_goods'):
    #                     self.goods.append(goods)
    #             finish = input(f'Продолжить покупки: нажмите Y для продолжения или N для перехода к оплате: ')
    #             if finish.lower() == 'n':
    #                 break
    #     return self.goods
    #
    # def _buy_goods(self):
    #     """Покупаем товар. Метод возвращает массив купленных товаров."""
    #     self._look_goods()
    #     if self.goods:
    #         self.basket._append_goods(self.goods)
    #     if self.basket:
    #         common_price = 0
    #         for goods in self.basket:
    #             common_price += goods.get('price')
    #         sum_to_pay = float(input(f'К оплате {round(common_price, 2)}: '))
    #         if sum_to_pay >= common_price:
    #             return f'Спасибо за покупку! Вы приобрели: {self.basket}'
    #         else:
    #             self.basket.clear()
    #             return 'Немного не хватает, ждем в другой раз'


if __name__ == '__main__':

    good_1 = Goods('carrot', 2.5, 87.2)
    good_2 = Goods('potato', 2.8, 88.4)
    good_3 = Goods('pasta', 4.3, 89.9)
    good_4 = Goods('coffe', 1.75, 95)
    #print(good_1, good_2, good_3, good_4)

    veg_category = Category('veg', [good_1])
    veg_category.add_goods(good_2)
    gros_category = Category('gros', [good_3, good_4])
    #print(veg_category)
    #print(gros_category)

    Category.make_catalogue([veg_category])
    Category.make_catalogue([gros_category])
    #print(Category.catalogue)

    basket = Basket([])
    basket.put_in_basket(good_2)
    #print(basket)

    shop = OnlineStore()
    shop.user = User('Bob', '123')
    print(shop.user)



