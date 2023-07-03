import math
"""Для функции math.ceil"""


def check(string):
    """Проверяет, чтобы введенная строка была числом"""
    while not string.isnumeric():
        print("Введите должна быть числом!")
        string = input()
    return int(string)


n = ""
n = check(n)
print(math.ceil(n ** 0.5))
