def check(string):
    """Проверяет, чтобы введенная строка состояла только из букв"""
    while not string.isalpha():
        print("Строка должна содержать только буквы!")
        string = input()
    return string


name = input("Введите имя: ")
name = check(name)
print(len(name))
