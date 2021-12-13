a = list(map(int, input().split()))
k, c = map(int, input().split())
a.append('a')
while c != 'a':
    a[k], c = c, a[k]
    k += 1
print(*a)
