r = lambda x: True if x % 2 == 0 else False
if r(int(input("Введите число: "))):
    print("Четное")
else:
    print("Нечетное")
