import random
colors = ["белый", "желтый", "зеленый", "синий", "черный"]
b = False
num = random.randrange(5)
while not b:
    a = int(input("Введите цвет: 1-бел, 2-желт, 3-зел, 4-син, 5-черн\n"))
    if num == (a - 1):
        print("Цвет загадан:", colors[num] + ",", "Отлично!")
        b = True
    elif num > (a - 1):
        print("Ваш цвет:", colors[a - 1] + ",", "Нужный цвет темнее!")
    else:
        print("Ваш цвет:", colors[a - 1] + ",", "Нужный цвет светлее!")
