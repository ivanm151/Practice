def simple(number):
    """Проверяет, является ли число простым"""
    for i in range(2, round(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


m = int(input("С какого числа проверять: "))
n = int(input("До какого числа проверять: "))
print(*[i for i in range(m, n + 1) if simple(i)], sep=', ')
# Создание и распаковка списка перестановок заданного списка
