n = int(input("Введите количетво очков (0, 1 или 3): "))
match n:
    case 0:
        print("Проигрыш")
        exit()
    case 1:
        print("Ничья")
        exit()
    case 3:
        print("Выигрыш")
        exit()
    case _:
        print("Количетво очков может быть равно только 0, 1 или 3")
