string = input('Введите строку: ')
palindroms = []
for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        if string[i:j] == string[i:j][::-1] and len(string[i:j]) > 1:
            palindroms.append(string[i:j])
print("Палиндромы в строке:", *palindroms)
