# Интернет магазин.
# Этап 1.
# Создать класс Товар, имеющий переменные имя, цена, рейтинг.
# Создать класс Категория, имеющий переменные имя и массив товаров. Создать несколько объектов класса Категория.
# Создать класс Basket, содержащий массив купленных товаров.
# Создать класс User, содержащий логин, пароль и объект класса Basket. Создать объект класса User.
# Этап 2.
# Аутентификация пользователя. Пользователь вводит логин и пароль с клавиатуры.
# Просмотр списка каталогов товаров.
# Просмотр списка товаров определенного каталога.
# Выбор товара в корзину.
# Покупка товаров, находящихся в корзине.
# Создаем перечисление содержащее значения для перечисленных операций. Можете добавить свои операции или
# изменить что-то на свой вкус.
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, TypedDict


class PasswordError(Exception):
    pass

class GoodsError(Exception):
    pass


class Goods(TypedDict):

    name_goods: str
    price: float
    rate: Optional[float]

    # def __str__(self):
    #     return f'{self.name_goods}: {self.price}$'
    #
    # def __getitem__(self, item):
    #     for item in self:
    #         return self[item]


class Categories:

    catalogue = {}

    def __new__(cls, args):
        cls.catalogue[args] = None
        print(cls.catalogue)
        return super().__new__(cls)

    def __init__(self, name: str):
        self.name_category = name
        self.category = {self.name_category: list[Goods, ...]}

    def __str__(self):
        return f'{self.name_category}: {self.category}'

    def __getitem__(self, item):
        for item in self:
            return self[item]

    def system_goods(self, goods: [Goods, ...]):
        self.category = {self.name_category: goods}
        Categories.catalogue.update(self.category)
        return Categories.catalogue

    def get_list_of_goods(self):
        return self.category


class Basket:

    def __init__(self, basket: list):
        self.basket = basket

    def __str__(self):
        return f'{self.basket}'

    def __getitem__(self, goods: Goods):
        for goods in self:
            return goods

    def input_basket(self, goods):
        for good in goods:
            self.basket.append(good)
        return self.basket


class User:

    def __init__(self, login: str, password: str):
        self._login = login
        self._password = password
        self.identification = None
        self.check_identification('name', 'password')

        # self.basket = Basket([])
        # self.choisen_goods = None

    def __str__(self):
        return f'Пользователь: {self._login}'

    def check_identification(self, name: str, password: str):
        name = input('Введите логин: ')
        password = input('Введите пароль: ')
        try:
            if name == self._login and password == self._password:
                self.identification = True
                print('Welcome our store! Have a good shoping!\n')
                return self.identification
        except PasswordError:
            print('Логин и/или пароль введены неверно')

    def look_goods(self):
        if self.identification:
            category_to_look = input(f'Выберите категорию товаров для просмотра из {Categories.catalogue.keys()}: ')
            print(f'В этой категории Вы можете выбрать следующие товары: {Categories.catalogue[category_to_look]}')
        return ''

    # def choose_goods(self, goods: [Goods, ...]):
    #     if goods:
    #         self.basket.input_basket(goods)
    #     return f'В Вашей корзине: {self.basket}'

    # def purchase_goods(self, basket: Basket):
    #     # common_price = 0
    #     for goods in basket:
    #         print(goods)


good_1: Goods = {'name_goods': 'carrot', 'price': 0.20, 'rate': 85.15}
good_2: Goods = {'name_goods': 'bread', 'price': 0.30, 'rate': 93.9}
good_3: Goods = {'name_goods': 'tooth_paste', 'price': 1.20, 'rate': 80.03}
good_4: Goods = {'name_goods': 'shampoo', 'price': 3.1, 'rate': 72.08}
good_5: Goods = {'name_goods': 'pasta', 'price': 2.41, 'rate': 56.93}
good_6: Goods = {'name_goods': 'coffee', 'price': 1.5, 'rate': 93.1}
# print(good_1, good_2, good_3, good_4, good_5, good_6)

grocery = Categories('grocery')
grocery.system_goods([good_5, good_6])
cosmetics = Categories('cosmetics')
cosmetics.system_goods([good_3, good_4])
vegetables = Categories('vegetables')
vegetables.system_goods([good_1, good_2])
print(Categories.catalogue['grocery'])

user_1 = User('Bob', '!al__231!')
print(user_1.look_goods())
# print(user_1.choose_goods([good_4, good_6]))
# print(user_1.purchase_goods(user_1.choose_goods([good_4, good_6])))


