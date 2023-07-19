import csv
counter = 0
with open("books.csv", mode="w", encoding='utf-8') as books:
    book = ["Name", "Author", "Year"]
    file_writer = csv.DictWriter(books, delimiter=",", lineterminator="\r", fieldnames=book)
    while counter < 5:
        if counter == 0:
            file_writer.writeheader()
        print("Книга №", counter + 1)
        a = "Название: "
        b = "Автор: "
        c = "Год выпуска: "
        file_writer.writerow({"Name": input(a), "Author": input(b), "Year": input(c)})
        counter += 1
