from dataclasses import dataclass
from goods import Basket


@dataclass()
class User:
    """
    Класс, который описывает Покупателя, который может просматривать каталог и категории товаров,
    выбрать товар для покупки, оплатить товар.

    Переменные экземпляра класса:
    login: логин
    password: пароль
    basket: корзина выбранных товаров

    """

    login: str
    password: str
    basket: Basket([]) = None


if __name__ == '__main__':
    user_1 = User('Bob', '123')
    print(user_1.password)
