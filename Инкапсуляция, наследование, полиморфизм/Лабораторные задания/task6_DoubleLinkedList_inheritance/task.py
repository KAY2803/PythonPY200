from typing import Any, Iterable, Optional

from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def _step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предшествующий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self._step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self._step_by_step_on_nodes(index)
        node.value = value

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"


# Реализовать класс DoubleLinkedList

class DoubleLinkedList(LinkedList):
    def __init__(self, data: Iterable = None):
        super().__init__(data=data)
        self.left: Node

    def append(self, value: Any):
        """ Добавление элемента в конец двусвязного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = self.left = append_node
        elif self.len == 1:
            self.linked_nodes(self.head, append_node)
            self.tail = append_node
        else:
            self.linked_nodes(self.left, self.tail, append_node)
            self.left = self.tail
            self.tail = append_node
        self.len += 1

    @staticmethod
    def linked_nodes(prev_node: Node, center_node: Optional[Node] = None, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой три узла.

        :param prev_node: Узел, предшествующий центральному узлу
        :param center_node: Центральный узел
        :param right_node: Правый или следующий узел
        """
        prev_node.next = center_node
        center_node.next = right_node


list_ = [1, 2, 3]
ll = DoubleLinkedList(list_)
ll.append(7)
print(repr(ll))
