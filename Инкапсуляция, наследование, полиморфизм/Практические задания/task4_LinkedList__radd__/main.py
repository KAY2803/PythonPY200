from typing import Any, Iterable, Optional

from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):  # O(n)
        """Конструктор связного списка"""
        self.len = 0    # O(1)
        self.head: Optional[Node] = None    # O(1)
        self.tail = self.head   # O(1)

        # if data is not None:
        #     for value in data:  # O(n)
        #         self.append(value)  # O(1)

        if not self and data is not None:
            self = data     # O(1)

        if self and data is not None:
            for value in data:     # O(n)
                self.append(value)  # O(1)

    def append(self, value: Any):   # O(1)
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)   # O(1)

        if self.head is None:
            self.head = self.tail = append_node # O(1)
        else:
            self.linked_nodes(self.tail, append_node)   # O(1)
            self.tail = append_node     # O(1)

        self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:    # O(n)
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):  # O(1)
            raise TypeError()

        if not 0 <= index < self.len:   # O(1)
            raise IndexError()

        current_node = self.head    # O(1)
        for _ in range(index):  # O(n)
            current_node = current_node.next    # O(1)

        return current_node

    @staticmethod   # O(1)
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node # O(1)

    def __getitem__(self, index: int) -> Any:   # O(n)
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)    # O(n)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:  # O(n)
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)    # O(n)
        node.value = value

    def to_list(self) -> list:  # O(n)
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def insert(self, index: int, value: Any) -> None:   # O(n)
        #реализовать алгоритм вставки элемента
        if not isinstance(index, int):     # O(1)
            raise TypeError()
        if not 0 <= index:  # O(1)
            raise IndexError()

        new_node = Node(value)  # O(1)

        if index == 0:
            new_node.next = self.head   # O(1)
            self.head = new_node    # O(1)
            self.len += 1
        elif index > self.len:
            self.append(value)  # O(1)
        else:
            prev_node = self.step_by_step_on_nodes(index-1) # O(n)
            next_node = prev_node.next  # O(1)
            self.linked_nodes(prev_node, new_node)  # O(1)
            self.linked_nodes(new_node, next_node)  # O(1)
            self.len += 1

    def __add__(self, other: ["LinkedList", list]) -> "LinkedList":     # O(n)
        if not isinstance(other, (LinkedList, list)):   # O(1)
            raise TypeError

        for item in other:  # O(n)
            self.append(item)   # O(1)

        return self

    # определить метод сложения, когда LinkedList находится справа от оператора сложения
    def __radd__(self, other: list):
        return LinkedList(other + self.to_list())   # O(n)

if __name__ == "__main__":
    ll = LinkedList()
    print(ll)

    ll = ll + [1, 2, 3]
    print(ll)

    ll = [4, 5, 6] + ll
    print(ll)


