from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Goods:
    """Класс, который описывает товары.

        Атрибуты класса:
        name_goods: наименование товара
        price: цена товара
        rate: рейтинг товара

    """

    name: str
    price: int | float
    rate: int | float = None


class Category(Goods):
    """Класс, который описывает категории товаров."""

    def __init__(self, name_category: str, goods: Optional[Goods] = None):
        """Инициализируем категорию товаров.

        :param name_category: наименование категории товара
        :param goods: товары класса Goods, входящие в эту категорию
        """
        self.name = name_category
        self.category = goods

        if not isinstance(goods, Goods|None):
            raise TypeError(f'Ожидается класс {Goods}, получен {goods})')

    def add_goods(self, goods: [Goods, ...]):
        """Метод добавляет товар в категорию. Принимает в качестве аргумента товар класса Goods,
        возвращает обновленную категорию товаров.

        """
        if self.category is None:
            self.category = goods
        else:
            self.category.append(goods)
        return self.category

    def get_goods_in_category(self):
        for index, goods in enumerate(self.category, start=1):
            print(index, goods)
        return ''

    def __getitem__(self, item: int):
        return self.category[item]

    def __repr__(self):
        return f'{self.name}: {self.category}'


class Basket:
    """Класс, который описывает перечень выбранных для покупки товаров"""

    def __init__(self):
        self.basket = []

    def put_in_basket(self, goods):
        self.basket.append(goods)
        return self.basket

    def __iter__(self):
        self.ix = 0
        return self

    def __next__(self):
        if self.ix == len(self.basket):
            raise StopIteration
        item = self.basket[self.ix]
        self.ix += 1
        return item

    def __repr__(self):
        return f'{self.basket}'


if __name__ == '__main__':
    good_1 = Goods('carrot', 2.5, 87.2)
    good_2 = Goods('potato', 2.8, 88.4)
    good_3 = Goods('pasta', 4.3, 89.9)
    good_4 = Goods('coffee', 1.75, 95)

    veg_category = Category('veg')
    veg_category.add_goods([good_1])
    veg_category.add_goods([good_2])
    gros_category = Category('gros')
    gros_category.add_goods([good_3, good_4])
    print(veg_category.get_goods_in_category())

