def simple(number):
    for i in range(2, round(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


n = int(input("До какого числа проверять: "))
a = [i for i in range(n+1) if not simple(i)]
print(a)
