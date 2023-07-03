s = input("Введите строку: ")
a = ''.join(c for c in s if c.isalpha())
ans = {i: a.count(i) for i in set(a)}
print(ans)
