import csv


def check(string):
    """Проверяет, чтобы введенная строка была числом"""
    while not string.isnumeric():
        string = input("Введите год (целое число от 0 до 2023): ")
    while not (0 <= int(string) <= 2023):
        string = input("Введите год (целое число от 0 до 2023): ")
        check(string)
    else:
        return int(string)


with open("books.csv", encoding='utf-8') as books:
    file_reader = csv.DictReader(books, delimiter=",")
    first = check(input("Введите начало диапазона: "))
    last = check(input("Введите конец диапазона: "))
    count = 0
    for row in file_reader:
        if first <= int(row["Year"]) <= last:
            print(row["Name"])
            count += 1
    if count == 0:
        print("В списке нет ни одной книги в этом диапазоне дат!")
