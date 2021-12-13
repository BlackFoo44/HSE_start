a = list(map(int, input().split()))
b = min(a)
c = max(a)
a.remove(b)
a.remove(c)
b1 = min(a)
c1 = max(a)
if b * b1 > c * c1:
    print(min(b1, b), max(b1, b))
else:
    print(min(c1, c), max(c1, c))
