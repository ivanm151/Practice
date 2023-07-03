def list_of_numbers():
    """Создание списка чисел"""
    empty_list = []
    length = int(input("Введите длину списка: "))
    for i in range(length):
        empty_list.append(int(input("Введите элемент списка: ")))
    return empty_list


list1 = list_of_numbers()
r = lambda x: sum(x) / len(x)
print("Среднее значение списка:", r(list1))
