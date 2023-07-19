def check(string):
    """Проверяет, чтобы введенная строка была числом"""
    while not string.lstrip("-").isnumeric():
        print("Введите число!")
        string = input()
    return string


a = str(11)
while len(a) != len(set(a)):
    a = input("Введите число, все цифры которого различны:\n")
    a = check(a)
m = list(a)
print("Порядковый номер максимальной цифры с начала списка:", m.index(max(m)) + 1, "С конца:", len(m) - m.index(max(m)))
