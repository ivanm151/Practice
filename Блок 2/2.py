progs = ["Новости", "Прогноз погоды", "Кино", "Охота и рыбалка"]
for i in progs:
    print(i)
prog = input("Введите название передачи: ")
num = int(input("Введите порядковый номер передачи в списке: ")) - 1
progs.insert(num, prog)
print("Новый список:")
for i in progs:
    print(i)
