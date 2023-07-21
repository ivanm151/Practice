a = list(map(chr, range(ord('a'), ord('z') + 1)))
ans = {i: a.index(i) + 1 for i in a}
print(ans)
