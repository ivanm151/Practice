s = input("Введите строку: ")
f = ''.join(c for c in s if c.isalpha())
glas = "aeiouyаеёиоуыэюя"
a = {i: i in glas for i in f.lower()}
print(a)
