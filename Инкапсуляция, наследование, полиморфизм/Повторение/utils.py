# функции по проверка типов

from typing import Any


def check_type(value: Any, types: Any):
    if not isinstance(value, types):
        raise TypeError(f'Ожидается {types}, получено {type(value)}')


def check_types(values: Any, types_: Any):
    if not isinstance(values, tuple):
        values = (values,)

    for elem in values:
        check_type(elem, types_)
