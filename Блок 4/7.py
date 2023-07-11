import itertools
"""Для использования itertools.permutations()"""


def list_of():
    """Создание списка"""
    empty_list = []
    length = int(input("Введите длину списка: "))
    for i in range(length):
        empty_list.append(input("Введите элемент списка: "))
    return empty_list


print(*itertools.permutations(list_of()), sep=', ')
# Создание и распаковка списка перестановок заданного списка, перестановки разделены запятыми
