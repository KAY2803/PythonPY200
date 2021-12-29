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
        self.next = None
        self.set_next(next_)

    def is_valid(self, node: Any) -> None:
        """Метод, который проверяет корректность значения node"""
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def set_next(self, next_: Optional["Node"] = None) -> None:
        """Метод, который устанавливает значение next"""
        self.is_valid(next_)
        self.next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return f'{self.value}'


def linked_nodes(left_node: Node, right_node: Optional["Node"] = None) -> None:
    """
    Функция, которая связывает между собой два узла.

    :param left_node: Левый или предыдущий узел
    :param right_node: Правый или следующий узел
    """
    left_node.set_next(right_node)


if __name__ == "__main__":
    list_nodes = [Node(value) for value in range(5)]
    print(list_nodes)

    index = 0
    for _ in range(len(list_nodes)-1):
        if index == list_nodes[index]:
            linked_nodes(list_nodes[index], None)
        else:
            linked_nodes(list_nodes[index], list_nodes[index + 1])
            index += 1


    #реализуйте алгоритм, который свяжет между собой узлы в списке

    print(list_nodes)

