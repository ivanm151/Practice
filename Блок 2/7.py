def check(string):
    """Проверяет, чтобы введенная строка была числом"""
    while not string.lstrip("-").isnumeric():
        print("Введите должна быть числом!")
        string = input()
    return int(string)


a = -1
summa = 0
while int(a) < 0:
    a = input("Введите число: ")
    a = check(a)
    print(summa)
    summa += int(a)
