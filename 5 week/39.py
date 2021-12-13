a = list(map(int, input().split()))
n, s = 0, 0
for i in a:
    if a.count(i) > n:
        n = a.count(i)
        s = i
print(s)
