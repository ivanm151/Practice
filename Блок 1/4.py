def check(string):
    """Проверяет, чтобы введенная строка была числом"""
    while not string.isnumeric():
        print("Строка должна быть числом!")
        string = input()
    return int(string)


a = 0
while a < 10 or a > 20:
    a = input("Введите число: ")
    a = check(a)
    if a < 10:
        print("Число меньше требуемого диапазона")
    if a > 20:
        print("Число больше требуемого диапазона")
print("Спасибо")
