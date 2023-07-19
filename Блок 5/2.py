import csv

with open("books.csv", mode="a", encoding='utf-8') as bs:
    o = ["Name", "Author", "Year"]
    w = csv.DictWriter(bs, delimiter=",", lineterminator="\r", fieldnames=o)
    n = int(input("Сколько записей добавить? "))
    for i in range(n):
        print("Добавленная книга №", i + 1)
        a = "Название: "
        b = "Автор: "
        c = "Год выпуска: "
        w.writerow({"Name": input(a), "Author": input(b), "Year": input(c)})

with open("books.csv", encoding='utf-8') as books:
    file_reader = csv.DictReader(books, delimiter=",")
    author = input("По какому автору искать? ")
    count = 0
    for row in file_reader:
        if row["Author"] == author:
            count += 1
            print(row["Name"])
    if count == 0:
        print("В списке нет ни одной книги этого автора!")
