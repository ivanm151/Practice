b = False
string = ""
while not b:
    string = input("Введите строку, состоящую из букв и пробелов: ")
    if all(x.isalpha() or x.isspace() for x in string):
        b = True
    else:
        print("Строка содержит недопустимые символы!")
        b = False
print(string.title())
