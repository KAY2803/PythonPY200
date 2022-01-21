from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_

# реализовать класс DoubleLinkedNode

class DoubleLinkedNode(Node):
    """ Класс, который описывает двусвязный узел связного списка. """

    def __init__(self, value: Any, prev: Optional["Node"] = None, next_: Optional["Node"] = None):
        super().__init__(value=value, next_=next_)
        self.prev = prev

    def __repr__(self) -> str:
         return f"Node({self.prev}, Node({self.value}), Node({self.next}))"

    @property
    def prev_(self):
        return self.prev

    @prev_.setter
    def prev_(self, prev: Optional["Node"]):
        self.is_valid(prev)
        self.prev = prev


a = Node(2)
b = Node(3)
n = DoubleLinkedNode(1, a, b)
print(repr(n))


Node(2, Node(1), Node(3))