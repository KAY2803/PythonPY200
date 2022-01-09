from typing import Iterable, Optional, Any

from node import Node

if __name__ == "__main__":

    if __name__ == "__main__":
        class LinkedList:
            def __init__(self, data: Iterable = None):
                """Конструктор связного списка"""
                self.len = 0
                self.head: Optional[Node] = None

                if data is not None:
                    for value in data:
                        self.append(value)

            def append(self, value: Any):
                """ Добавление элемента в конец связного списка. """
                append_node = Node(value)

                if self.head is None:
                    self.head = append_node
                else:
                    last_index = self.len - 1
                    last_node = self.step_by_step_on_nodes(last_index)

                    self.linked_nodes(last_node, append_node)

                self.len += 1

            @staticmethod
            def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
                """
                Функция, которая связывает между собой два узла.

                :param left_node: Левый или предыдущий узел
                :param right_node: Правый или следующий узел
                """
                left_node.set_next(right_node)

            def step_by_step_on_nodes(self, index: int) -> Node:
                """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """

                if not isinstance(index, int):
                    raise TypeError()
                if not 0 <= index < self.len:
                    raise IndexError()

                current_node = self.head
                for _ in range(index):
                    current_node = current_node.next

                return current_node

            def count(self, value: Any) -> int:
                """ Функция выполняет перемещение по узлам и возвращает количество найденных значений. """
                count = 0
                for element in self:
                    if element == value:
                        count += 1
                return count

            def to_list(self) -> list:
                return [linked_list_value for linked_list_value in self]

            def __getitem__(self, index: int) -> Any:
                """ Метод возвращает значение узла по указанному индексу. """
                node = self.step_by_step_on_nodes(index)
                return node.value

            def __repr__(self) -> str:
                return f"{self.__class__.__name__}({self.to_list()})"


        list_ = [1, 2, 2, 'a', 'v', 2, 'f', 90]
        linked_list = LinkedList(list_)
        print(linked_list.count(2))
