class Glass:
    """Класс, который описывает стаканы"""

    def __init__(self, material: str):
        """
        Инициализируем новый стакан с одним атрибутом
        :param material: материал, из которого сделан стакан
        """
        self.__material = material

    def get_material(self):
        """Метод, который возвращает материал, из которого сделан стакан"""
        return self.__material


if __name__ == "__main__":
    glass1 = Glass('стекло')
    print(glass1.get_material())
