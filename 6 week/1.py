
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
i, j = 0, 0
while i < len(a) and j < len(b):
    if a[i] == b[j]:
        c.append(a[i])
        j += 1
        i += 1
    elif a[i] > b[j]:
        j += 1
    elif a[i] < b[j]:
        i += 1
print(*c)
