def check(string):
    """Проверяет, чтобы введенная строка состояла только из букв"""
    while not string.isalpha():
        print("Строка должна содержать только буквы!")
        string = input()
    return string


name = input("Введите имя: ")
name = check(name)
surname = input("Введите фамилию: ")
surname = check(surname)
# Соединение имени и фамилии в одну строку с разделением пробелом
ans = name + " " + surname
# Вывод полученной строки и ее длины
print("Строка:", ans, "Длина строки:", len(ans))
