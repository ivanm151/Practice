def check(string):
    """Проверяет, чтобы введенная строка была числом"""
    while not string.lstrip("-").isnumeric():
        print("Строка должна быть числом!")
        string = input("Введите число: ")
    return int(string)


a, b, = "", ""
a, b = check(a), check(b)
print("Произведение чисел", a, "и", b, "равно", a * b)
