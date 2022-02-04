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

from typing import Optional, TypedDict


class PasswordError(Exception):
    """Класс исключения, которое возникает, если Пользователь неверно ввел логин и/или пароль"""
    pass


class Goods(TypedDict):
    """"Класс, который описывает товары.

    Атрибуты класса:
    name_goods: наименование товара
    price: цена товара
    rate: рейтинг товара

    """

    name_goods: str
    price: float
    rate: Optional[float]

    def __str__(self):
        return f'{self.name_goods}: {self.price}$, rate: {self.rate}'


class Categories:
    """Класс, который описывает категории товаров. Атрибут catalogue содержит перечень всех категорий товаров."""

    catalogue = {}

    def __new__(cls, args):
        cls.catalogue[args] = None
        return super().__new__(cls)

    def __init__(self, name: str):
        """Инициализируем категорию товаров.

        :param name: наименование категории
        """
        self.name_category = name
        self.category = {self.name_category: list[Goods, ...]}

    def __str__(self):
        return f'{self.name_category}: {self.category}'

    def __getitem__(self, item):
        for item in self:
            return self[item]

    def system_goods(self, goods: [Goods, ...]):
        """Метод добавляет товар в категорию. Принимает в качестве аргумента товар класса Goods,
        возвращает обновленный каталог товаров.

        """
        self.category = {self.name_category: goods}
        Categories.catalogue.update(self.category)
        return Categories.catalogue


class Basket:
    """Класс, который описывает перечень купленных товаров"""

    def __init__(self, basket: list):
        self.basket = basket

    def __str__(self):
        return f'{self.basket}'

    def __getitem__(self, goods: Goods):
        return goods


class User:
    """Класс, который описывает Покупателя, который может просматривать каталог и категории товаров,
    выбрать товар для покупки, оплатить товар.

    Переменные экземпляра класса:
    login: логин
    password: пароль

    """

    def __init__(self, login: str, password: str):
        """Инициализируем Покупателя.

        :param login: логин
        :param password: пароль

        """
        self._login = login
        self._password = password
        self.identification = False
        self._check_identification('name', 'password')
        self.goods = []
        self.basket = Basket([])

    def __str__(self):
        return f'Пользователь: {self._login}'

    def _check_identification(self, name: str, password: str):
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
                if name == self._login and password == self._password:
                    self.identification = True
                    print('Welcome our store! Have a good shoping!\n')
                    return self.identification
                break
            except PasswordError:
                print('Логин и/или пароль введены неверно')
                continue

    def _look_goods(self):
        """Смотрим и выбираем товаров. Метод возвращает массив выбранных товаров."""
        if self.identification:
            while True:
                category_to_look = input(f'Выберите категорию товаров для просмотра из {Categories.catalogue.keys()}: ')
                if category_to_look in Categories.catalogue.keys():
                    choice = input(f'Выберите товар: {Categories.catalogue[category_to_look]} ')
                else:
                    continue
                for goods in Categories.catalogue[category_to_look]:
                    if choice == goods.get('name_goods'):
                        self.goods.append(goods)
                finish = input(f'Продолжить покупки: нажмите Y для продолжения или N для перехода к оплате: ')
                if finish.lower() == 'n':
                    break
        return self.goods

    def _buy_goods(self):
        """Покупаем товар. Возвращает массив купленных товаров."""
        self._look_goods()
        if self.goods:
            self.basket = self.goods
        if self.basket:
            common_price = 0
            for goods in self.basket:
                common_price += goods.get('price')
            sum_to_pay = float(input(f'К оплате {round(common_price, 2)}: '))
            if sum_to_pay >= common_price:
                print(f'Спасибо за покупку! Вы приобрели: {self.basket}')
            else:
                self.basket.clear()
                print('Немного не хватает, ждем в другой раз')
        return self.basket


good_1: Goods = {'name_goods': 'carrot', 'price': 0.20, 'rate': 85.15}
good_2: Goods = {'name_goods': 'potato', 'price': 0.30, 'rate': 93.9}
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
# print(Categories.catalogue)

user_1 = User('Bob', '123')
# print(user_1._look_goods())
print(user_1._buy_goods())


