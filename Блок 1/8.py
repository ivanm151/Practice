def check_name(string):
    """Проверяет, чтобы введенная строка состояла только из букв"""
    while not string.isalpha():
        print("Строка должна содержать только буквы!")
        string = input("Введите имя: ")
    return string


def check_age(string):
    """Проверяет, чтобы введенная строка была числом"""
    while not string.isnumeric():
        print("Строка должна быть числом!")
        string = input("Введите возраст: ")
    return int(string)


name, age = "", ""
name = check_name(name)
age = check_age(age)
print("Привет,", name + "! Тебе уже", age, "лет.")
