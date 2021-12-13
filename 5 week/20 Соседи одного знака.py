a = list(map(int, input().split()))
prev = a[0]
b = [()]
c = 1
for i in a[1::]:
    if i * prev > 0:
        b += [(prev, i)]
    elif i * prev < 0:
        c += 1
    prev = i

if c == len(a):
    print()
else:
    print(*b[1])
