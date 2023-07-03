def list_of_numbers():
    """Создание списка чисел"""
    empty_list = []
    length = int(input("Введите длину списка: "))
    for i in range(length):
        empty_list.append(int(input("Введите элемент списка: ")))
    return empty_list


a = [i ** 2 for i in list_of_numbers()]
print(a)
