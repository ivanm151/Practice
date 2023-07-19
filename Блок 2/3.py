def check(string):
    """Проверяет, чтобы введенная строка была числом"""
    while not string.isnumeric():
        print("Введите должна быть числом!")
        string = input()
    return string


num = ""
num = check(num)
sum = 0
for i in range(len(num)):
    sum += int(num[i]) ** len(num)
if sum == int(num):
    print("Является числом Армстронга")
else:
    print("Не является числом Армстронга")
