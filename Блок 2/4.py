a = int(input("Введите коэф. А: "))
b = int(input("Введите коэф. В: "))
c = int(input("Введите коэф. С: "))
print(str(a) + "x^2 +", str(b) + "x +", str(c), "= 0")
D = b ** 2 - 4 * a * c
if D < 0:
    print("Корней нет")
elif D == 0:
    print("x =", -b/(2 * a))
else:
    print("x1 =", (-b + D ** 0.5) / (2 * a))
    print("x2 =", (-b - D ** 0.5) / (2 * a))
    
