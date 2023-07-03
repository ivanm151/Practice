import random
colors = ["белый", "желтый", "зеленый", "синий", "черный"]
b = False
num = random.randrange(5)
while not b:
    a = int(input("Введите цвет: 1-белый, 2-желтый, 3-зеленый, 4-синий, 5-черный\n"))
    if num == (a-1):
        print("Цвет загадан:", colors[num]+",", "Ваш цвет:", colors[a - 1]+",", "Отлично!")
        b = True
    elif num > (a-1):
        print("Ваш цвет:", colors[a - 1]+",", "Нужный цвет темнее! Попробуйте еще!")
    else:
        print("Ваш цвет:", colors[a - 1]+",", "Нужный цвет светлее! Попробуйте еще!")

