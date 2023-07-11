string = input("Введите строку: ")
result = ""
for letter in string:
    if 'n' > letter >= 'a' or 'N' > letter >= 'A':
        result += chr(ord(letter) + 13)
    elif 'z' >= letter > 'm' or 'Z' >= letter > 'M':
        result += chr(ord(letter) - 13)
    else:
        result += letter
print(result)
