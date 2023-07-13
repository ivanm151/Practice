import csv

with open("books.csv", mode="a", encoding='utf-8') as books:
    book = ["Name", "Author", "Year"]
    file_writer = csv.DictWriter(books, delimiter=",", lineterminator="\r", fieldnames=book)
    n = int(input("Сколько записей добавить? "))
    for i in range(n):
        print("Добавленная книга №", i + 1)
        file_writer.writerow({"Name": input("Название: "), "Author": input("Автор: "), "Year": input("Год выпуска: ")})

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
