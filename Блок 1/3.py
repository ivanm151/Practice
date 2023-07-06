def check(string):
    """Проверяет, чтобы введенная строка была числом"""
    while not string.lstrip("-").isnumeric():
        print("Строка должна быть числом!")
        string = input()
    return int(string)


mas = []
print("Введите 3 числа:")
for i in range(3):
    a = input()
    a = check(a)
    mas.append(a)
# Сортировка списка чисел по убыванию
mas.sort(reverse=True)
print(mas, "Наибольшее число: ", mas[0])
