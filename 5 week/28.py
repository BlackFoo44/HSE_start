a = tuple(map(int, input().split()))
k = a[0]
j = 1
for i in a:
    if i != k:
        k = i
        j += 1
print(j)
