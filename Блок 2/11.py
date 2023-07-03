def check(string):
    """Проверяет, чтобы введенная строка была числом"""
    while not string.lstrip("-").isnumeric():
        print("Введите должна быть числом!")
        string = input()
    return int(string)


a, b = input(""), input("")
a, b = check(a), check(b)
print(round((a+b)*(b-a+1)/2))