l = list(map(int, input().split()))
i = len(l) - 1
while i >= 0:
    if l[i] == 0:
        l.pop(i)
        l.append(0)
    i -= 1
print(*l)
