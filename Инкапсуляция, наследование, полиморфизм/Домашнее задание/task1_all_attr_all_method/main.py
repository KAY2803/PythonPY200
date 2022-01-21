if __name__ == "__main__":

    class Parent:
        "Класс, который описывает родителей"

        def __init__(self, gender: str, age: int, name: str):
            """
            Создаем новый экземляр одного из родителей:
            :param gender: пол
            :param age: возраст
            :param name: имя
            """
            self.name = name
            self._age = age
            self.__gender = gender


