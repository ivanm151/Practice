import csv
counter = 0
with open("books.csv", mode="w", encoding='utf-8') as bs:
    o = ["Name", "Author", "Year"]
    f = csv.DictWriter(bs, delimiter=",", lineterminator="\r", fieldnames=o)
    while counter < 5:
        if counter == 0:
            file_writer.writeheader()
        print("Книга №", counter + 1)
        a = "Название: "
        b = "Автор: "
        c = "Год выпуска: "
        f.writerow({"Name": input(a), "Author": input(b), "Year": input(c)})
        counter += 1
