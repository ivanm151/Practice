import itertools

"""Для использования itertools.combinations()"""


def list_of_numbers():
    """Создание списка чисел"""

    empty_list = []
    global length
    for k in range(length):
        empty_list.append(int(input("Введите элемент списка: ")))
    return empty_list


combinations, answer, check = [], [], []
length = int(input("Введите длину списка: "))
lst = list_of_numbers()
n = int(input("Введите число: "))
counter = 1
while counter <= length:
    for x in list(itertools.combinations(lst, counter)):
        combinations.append(x)
    counter += 1
i = 0
while i < len(combinations):
    if sum(combinations[i]) == n:
        if set(combinations[i]) in check:
            i += 1
        else:
            check.append(set(combinations[i]))
            answer.append(combinations[i])
            i += 1
    else:
        i += 1
print("Заданное число:", n, "Список комбинаций:", *answer)
