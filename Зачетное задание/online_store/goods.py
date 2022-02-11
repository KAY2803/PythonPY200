from dataclasses import dataclass


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

    # def __getitem__(self, item: int):
    #     return self[item]

    def __repr__(self):
        return f'{self.name}: {self.price}$'


class Category(Goods):
    """Класс, который описывает категории товаров. Атрибут класса catalogue содержит перечень всех категорий товаров.
    Предусмотрен классовый метод составления каталога товаров путем добавления категорий.

    """
    catalogue = []

    @classmethod
    def make_catalogue(cls, categories: ['Category', ...]):
        # добавить проверку типа
        # добавить проверку наличия категории, в случае наличия - ее расширение
        cls.catalogue.extend(categories)
        return f'{cls.catalogue}'

    # @classmethod
    # def __iter__(cls):
    #     return cls.catalogue

    def __init__(self, name_category: str, goods: [Goods, ...]):
        """Инициализируем категорию товаров.

        :param name_category: наименование категории товара
        :param goods: товары класса Goods, входящие в эту категорию
        """
        self.name = name_category
        self.category = goods # добавить проверку вх значения = list

    def add_goods(self, goods: [Goods, ...]):
        """Метод добавляет товар в категорию. Принимает в качестве аргумента товар класса Goods,
        возвращает обновленную категорию товаров.

        """

        self.category.append(goods)
        return self.category

    def __getitem__(self, item: int):
        return self.category[item]

    # def __contains__(self, item):
    #     return item in self

    def __repr__(self):
        return f'{self.name}: {self.category}'


@dataclass
class Basket:
    """Класс, который описывает перечень выбранных для покупки товаров"""
    basket: list

    def put_in_basket(self, goods):
        self.basket.append(goods)
        return self.basket

    def __getitem__(self, item: int):
        return self[item]

    def __repr__(self):
        return f'{self.basket}'


if __name__ == '__main__':
    good_1 = Goods('carrot', 2.5, 87.2)
    good_2 = Goods('potato', 2.8, 88.4)
    good_3 = Goods('pasta', 4.3, 89.9)
    good_4 = Goods('coffe', 1.75, 95)

    veg_category = Category('veg', [good_1])
    veg_category.add_goods(good_2)
    gros_category = Category('gros', [good_3, good_4])
    print(veg_category)

    Category.make_catalogue([veg_category])
    Category.make_catalogue([gros_category])
    print(Category.catalogue)

    basket = Basket([])
    basket.put_in_basket(good_2)
    print(basket)
