import random
a = 0
b = 0
c = 0
while b < 3:
    i = input("Выберите сторону: 0-орел, 1-решка\n")
    match int(i):
        case 1:
            print("Решка")
        case 0:
            print("Орел")
        case _:
            print("Game over")
            exit()
    n = random.randrange(2)
    if int(i) == n:
        a += 1
        b = 0
        print("Выигрыш")
    else:
        b += 1
        c += 1
        print("Проигрыш")
    print("Выигрышей:", a, "Проигрышей:", c, "Поражений подряд:", b)
