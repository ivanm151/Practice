def isfloat():
    """Проверяет, чтобы введенное число было вещественным"""
    b = False
    while not b:
        number = input("Введите число: ")
        try:
            float(number)
            b = True
        except ValueError:
            print("Срока должна быть вещественным числом")
            b = False
    return number


a = isfloat()
# Округление до двух знаков после запятой
print(round(float(a), 2))
