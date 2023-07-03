r = lambda lim, n1, n2, sp: [sp.append(n1+n2), r(lim, n2, n1+n2, sp) if (n1+n2) < (lim-n2) else sp.insert(1, 1)]
f = [0]
r(int(input("Введите число: ")), 0, 1, f)
print(list(f))
