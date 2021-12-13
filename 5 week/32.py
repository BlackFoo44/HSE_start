a = list(map(int, input().split()))
b = a.copy()
if len(a) > 3:
    c1 = max(a)
    a.remove(max(a))
    c2 = max(a)
    a.remove(max(a))
    c3 = max(a)
    d1 = min(b)
    b.remove(min(b))
    d2 = min(b)
    b.remove(min(b))
    d3 = min(b)
    if d1 * d2 * c1 > c1 * c2 * c3:
        print(d1, d2, c1)
    else:
        print(c1, c2, c3)
else:
    print(*a)
